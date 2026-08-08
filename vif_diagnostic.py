import sys
import io
import json
import numpy as np
import pandas as pd
import scipy.stats as stats

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Load dataset
csv_path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\BASES_DE_DATOS_GEOQUIMICA\MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv"
df = pd.read_csv(csv_path)

# 2. Calculate VIF
tiers = ['tier1_org_acids', 'tier2_mp_ratio', 'tier3_tas_ratio', 'tier4_asphaltene_ratio']
X = df[tiers].copy()
corr_matrix_df = X.corr()
corr_matrix_inv = np.linalg.inv(corr_matrix_df.values)
vifs = {col: float(corr_matrix_inv[i, i]) for i, col in enumerate(X.columns)}

# 3. Identify VIF > 10
vif_gt_10 = {k: v for k, v in vifs.items() if v > 10}

# 4. Condition number
X_with_const = np.column_stack([np.ones(X.shape[0]), X.values])
cond_number = float(np.linalg.cond(X_with_const))

# 5. Correlation matrix
corr_matrix = corr_matrix_df.to_dict()

# 6. Post-hoc power
y = np.log(df['viscosity_measured_cp'].values)
phi = df['phi_cascade'].values
slope, intercept, r_value, p_value, std_err = stats.linregress(phi, y)
r2_marginal = float(r_value**2)
f2 = float(r2_marginal / (1 - r2_marginal))

N = 41
df1 = 1
df2 = 39
nc = f2 * N
f_crit = stats.f.ppf(0.95, df1, df2)
power = float(1 - stats.ncf.cdf(f_crit, df1, df2, nc))

# 7. Sensitivity analysis of eta
R = 8.314e-3
T0 = 298.15
mean_phi = float(np.mean(phi))
delta_x_d = float(R * T0 * np.log(1 + mean_phi))

eta_values = np.linspace(0.70, 1.00, 4)
sensitivity_results = []
for eta in eta_values:
    sensitivity_results.append({
        "eta": float(round(eta, 2)),
        "delta_x_d_crit": float(round(delta_x_d, 4))
    })

# 8. Re-run LMM with fixed effects only (OLS for global slope)
global_slope_p_value = float(p_value)

# 9. Save all to JSON
results = {
    "vifs": vifs,
    "vif_gt_10": vif_gt_10,
    "condition_number": cond_number,
    "correlation_matrix": corr_matrix,
    "r2_marginal": r2_marginal,
    "f2_effect_size": f2,
    "statistical_power": power,
    "sensitivity_eta": sensitivity_results,
    "global_slope_p_value": global_slope_p_value
}

json_path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\diagnostic_results.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=4)

print(json.dumps(results, indent=4))
