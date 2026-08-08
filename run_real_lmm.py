import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import r2_score, mean_absolute_error
import json
import warnings
warnings.filterwarnings('ignore')

# Load dataset
csv_path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\BASES_DE_DATOS_GEOQUIMICA\MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv"
df = pd.read_csv(csv_path)
df['log_visc'] = np.log(df['viscosity_measured_cp'])

# 1. FIT REAL LMM with REML
# Model: log_visc ~ phi_cascade + (1 | basin_location)
# This is random intercept, fixed slope
model = smf.mixedlm('log_visc ~ phi_cascade', df, groups=df['basin_location'])
result = model.fit(reml=True)
print(result.summary())

# Extract key values
beta_fixed = result.fe_params['phi_cascade']
alpha_fixed = result.fe_params['Intercept']
p_value_slope = result.pvalues['phi_cascade']
p_value_intercept = result.pvalues['Intercept']
se_slope = result.bse_fe['phi_cascade']
ci_slope = result.conf_int().loc['phi_cascade']

# Random effects (shrinkage-adjusted intercepts)
random_effects = result.random_effects
print("\nRandom Effects (BLUP, shrinkage-adjusted):")
for basin, re in random_effects.items():
    print(f"  {basin}: {re['Group']:+.4f}")

# 2. Compute R2_marginal and R2_conditional
y = df['log_visc'].values

# Marginal: fixed effects only
y_pred_marginal = result.fittedvalues - np.array([random_effects[g]['Group'] for g in df['basin_location']])
r2_marginal = r2_score(y, y_pred_marginal)

# Conditional: fixed + random
y_pred_conditional = result.fittedvalues
r2_conditional = r2_score(y, y_pred_conditional)

mae_conditional = mean_absolute_error(y, y_pred_conditional)

print(f"\nR2_marginal (REML): {r2_marginal:.4f}")
print(f"R2_conditional (REML): {r2_conditional:.4f}")
print(f"MAE_conditional: {mae_conditional:.4f} ln cP")
print(f"Fixed slope beta: {beta_fixed:.4f} (SE={se_slope:.4f}, p={p_value_slope:.2e})")
print(f"Fixed intercept: {alpha_fixed:.4f} (p={p_value_intercept:.2e})")
print(f"95% CI for slope: [{ci_slope[0]:.4f}, {ci_slope[1]:.4f}]")

# 3. LOGO Cross-Validation
basins = df['basin_location'].unique()
logo_errors = []
for holdout in basins:
    train = df[df['basin_location'] != holdout]
    test = df[df['basin_location'] == holdout]
    try:
        m = smf.mixedlm('log_visc ~ phi_cascade', train, groups=train['basin_location'])
        r = m.fit(reml=True)
        # For held-out basin, use only fixed effects (no random intercept available)
        y_pred_test = r.fe_params['Intercept'] + r.fe_params['phi_cascade'] * test['phi_cascade']
        logo_errors.extend(np.abs(test['log_visc'].values - y_pred_test.values).tolist())
        mae_holdout = mean_absolute_error(test['log_visc'].values, y_pred_test.values)
        print(f"\nLOGO holdout={holdout}: N_test={len(test)}, MAE={mae_holdout:.4f}")
    except Exception as e:
        print(f"LOGO error for {holdout}: {e}")

mae_logo = np.mean(logo_errors)
print(f"\nOverall LOGO MAE: {mae_logo:.4f} ln cP")

# 4. Variance components
var_random = float(result.cov_re.iloc[0,0])
var_resid = result.scale
icc = var_random / (var_random + var_resid)
print(f"\nVariance Components:")
print(f"  Random intercept variance: {var_random:.4f}")
print(f"  Residual variance: {var_resid:.4f}")
print(f"  ICC (Intraclass Correlation): {icc:.4f}")

# 5. Residual diagnostics
residuals = y - y_pred_conditional
from scipy import stats as spstats
shapiro_stat, shapiro_p = spstats.shapiro(residuals)
print(f"\nResidual Diagnostics:")
print(f"  Mean: {np.mean(residuals):.6f}")
print(f"  Std: {np.std(residuals):.4f}")
print(f"  Shapiro-Wilk p: {shapiro_p:.4f}")

# 6. AIC/BIC
print(f"\nModel Selection:")
print(f"  AIC: {result.aic:.2f}")
print(f"  BIC: {result.bic:.2f}")

# Save results
results = {
    'beta_fixed_slope': round(float(beta_fixed), 4),
    'alpha_fixed_intercept': round(float(alpha_fixed), 4),
    'se_slope': round(float(se_slope), 4),
    'p_value_slope': float(p_value_slope),
    'ci_slope_lower': round(float(ci_slope[0]), 4),
    'ci_slope_upper': round(float(ci_slope[1]), 4),
    'r2_marginal': round(float(r2_marginal), 4),
    'r2_conditional': round(float(r2_conditional), 4),
    'mae_conditional': round(float(mae_conditional), 4),
    'mae_logo': round(float(mae_logo), 4),
    'var_random_intercept': round(float(var_random), 4),
    'var_residual': round(float(var_resid), 4),
    'icc': round(float(icc), 4),
    'shapiro_p': round(float(shapiro_p), 4),
    'aic': round(float(result.aic), 2),
    'bic': round(float(result.bic), 2),
    'random_effects_blup': {k: round(float(v['Group']), 4) for k, v in random_effects.items()}
}

with open(r'C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\real_lmm_results.json', 'w') as f:
    json.dump(results, f, indent=4)

print("\nResults saved to real_lmm_results.json")
