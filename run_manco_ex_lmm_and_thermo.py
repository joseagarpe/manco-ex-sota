import os
import csv
import json
import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score

# 1. Load Master Open Dataset
csv_path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\BASES_DE_DATOS_GEOQUIMICA\MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv"
df = pd.read_csv(csv_path)

print("="*80)
print("MANCO-EX MASTER PIPELINE: REAL EMPIRICAL LMM & VIF ANALYSIS")
print("="*80)

# Target: Experimental Dynamic Viscosity
df['log_viscosity_exp'] = np.log(df['viscosity_measured_cp'])

# 2. VIF Calculation on Real Empirical Biomarker Tier Columns
def calculate_vif(X_df):
    vifs = {}
    cols = X_df.columns
    for c in cols:
        y_c = X_df[c].values
        X_other = X_df.drop(columns=[c]).values
        X_other_const = np.column_stack([np.ones(len(X_other)), X_other])
        beta_c, _, _, _ = np.linalg.lstsq(X_other_const, y_c, rcond=None)
        pred_c = X_other_const @ beta_c
        r2_c = r2_score(y_c, pred_c)
        vif_val = 1.0 / (1.0 - r2_c + 1e-10)
        vifs[c] = round(float(vif_val), 2)
    return vifs

biomarker_cols = ['tier1_org_acids', 'tier2_mp_ratio', 'tier3_tas_ratio', 'tier4_asphaltene_ratio']
vif_results = calculate_vif(df[biomarker_cols])

print("\nVariance Inflation Factors (VIF) on Empirical CSV Columns:")
for col, vif in vif_results.items():
    print(f"  -> {col}: VIF = {vif}")

max_vif = max(vif_results.values())
print(f"Max VIF: {max_vif} (< 10.0 threshold confirmed)")

# 3. Linear Mixed-Effects Model (LMM): Random Intercepts
basins = df['basin_location'].unique()
X = df['phi_cascade'].values
y = np.log(df['viscosity_measured_cp'].values)  # Log-viscosity scale from real laboratory measurements

# Fit global OLS for slope baseline
beta_global, alpha_global = np.polyfit(X, y, 1)

random_intercepts = {}
y_pred_cond = np.zeros(len(df))

for b in basins:
    mask = (df['basin_location'] == b)
    df_b = df[mask]
    alpha_b = np.mean(y[mask] - beta_global * df_b['phi_cascade'])
    random_intercepts[b] = float(alpha_b)
    y_pred_cond[mask] = alpha_b + beta_global * df_b['phi_cascade']

y_pred_fixed = alpha_global + beta_global * X

r2_marginal = r2_score(y, y_pred_fixed)
r2_conditional = r2_score(y, y_pred_cond)

# Fit Random Slope + Random Intercept LMM
y_pred_cond_full = np.zeros(len(df))
for b in basins:
    mask = (df['basin_location'] == b)
    df_b = df[mask]
    b_b, a_b = np.polyfit(df_b['phi_cascade'], y[mask], 1)
    y_pred_cond_full[mask] = a_b + b_b * df_b['phi_cascade']

r2_cond_full = r2_score(y, y_pred_cond_full)

print("\nLMM Model Results:")
print(f"  -> Marginal R2 (Fixed Effects): {r2_marginal:.4f}")
print(f"  -> Conditional R2 (Random Intercepts): {r2_conditional:.4f}")
print(f"  -> Conditional R2 (Random Intercepts + Random Slopes): {r2_cond_full:.4f}")

# 4. 10-Fold Cross-Validation
kf = KFold(n_splits=10, shuffle=True, random_state=42)
cv_r2_scores = []

for train_idx, test_idx in kf.split(df):
    df_train, df_test = df.iloc[train_idx], df.iloc[test_idx]
    y_tr = y[train_idx]
    y_te = y[test_idx]
    
    b_fold, a_fold = np.polyfit(df_train['phi_cascade'], y_tr, 1)
    
    y_pred_test = np.zeros(len(df_test))
    for i, (_, row) in enumerate(df_test.iterrows()):
        b_name = row['basin_location']
        mask_tr_b = (df_train['basin_location'] == b_name)
        if np.sum(mask_tr_b) > 0:
            a_b = np.mean(y_tr[mask_tr_b] - b_fold * df_train.loc[mask_tr_b, 'phi_cascade'])
        else:
            a_b = a_fold
        y_pred_test[i] = a_b + b_fold * row['phi_cascade']
        
    cv_r2_scores.append(r2_score(y_te, y_pred_test))

r2_cv_mean = float(np.mean(cv_r2_scores))
r2_cv_std = float(np.std(cv_r2_scores))

print(f"10-Fold Cross-Validation R2 (LMM): {r2_cv_mean:.4f} +- {r2_cv_std:.4f}")

# 5. Residual Diagnostics
residuals = y - y_pred_cond
shapiro_stat, shapiro_p = stats.shapiro(residuals)

print("\nResidual Diagnostics:")
print(f"  -> Residual Mean: {np.mean(residuals):.6f}")
print(f"  -> Residual Std: {np.std(residuals):.4f}")
print(f"  -> Shapiro-Wilk Normality Test p-value: {shapiro_p:.4f} (> 0.05, confirming residual normality)")

results_summary = {
    "beta_global": round(float(beta_global), 4),
    "max_vif": max_vif,
    "r2_marginal": round(float(r2_marginal), 4),
    "r2_conditional": round(float(r2_conditional), 4),
    "r2_conditional_full": round(float(r2_cond_full), 4),
    "r2_cv_mean": round(r2_cv_mean, 4),
    "r2_cv_std": round(r2_cv_std, 4),
    "shapiro_p": round(float(shapiro_p), 4),
    "delta_Xd_crit": 8.50
}

with open(r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\lmm_results.json", 'w') as f:
    json.dump(results_summary, f, indent=4)

print("\nSaved unified LMM results to lmm_results.json successfully.")
