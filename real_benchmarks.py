import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error
import json

csv_path = r'C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\BASES_DE_DATOS_GEOQUIMICA\MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv'
df = pd.read_csv(csv_path)

y_true = df['viscosity_measured_cp'].values
y_true_log = np.log(y_true)
api = df['api_gravity'].values

# Reservoir temperature assumption
T_F = 104.0  # 313.15 K = 40°C = 104°F
T_R = T_F + 459.67  # Rankine

# ============================================
# 1. BEGGS-ROBINSON (1975) - REAL CORRELATION
# Dead oil viscosity:
# mu_od = 10^x - 1
# x = y * T^(-1.163)
# y = 10^z  
# z = 3.0324 - 0.02023 * API
# T in °F
# ============================================
z_br = 3.0324 - 0.02023 * api
y_br = 10.0 ** z_br
x_br = y_br * (T_F ** (-1.163))
mu_beggs = 10.0 ** x_br - 1.0  # cP
mu_beggs = np.clip(mu_beggs, 1.0, 1e8)  # safety clip
log_mu_beggs = np.log(mu_beggs)

r2_beggs = r2_score(y_true_log, log_mu_beggs)
mae_beggs = mean_absolute_error(y_true_log, log_mu_beggs)

print(f"Beggs-Robinson (1975) REAL:")
print(f"  R2: {r2_beggs:.4f}")
print(f"  MAE: {mae_beggs:.4f} ln cP")
print(f"  Predicted range: {mu_beggs.min():.1f} - {mu_beggs.max():.1f} cP")
print(f"  Measured range: {y_true.min():.1f} - {y_true.max():.1f} cP")
print()

# ============================================
# 2. EGBOGAH-NG (1990) - API + T correlation
# (Replaces Pedersen since Pedersen requires
#  full compositional EOS data not available)
# log(log(mu_od + 1)) = 1.8653 - 0.025086*API - 0.5644*log10(T)
# T in °F
# ============================================
rhs_eg = 1.8653 - 0.025086 * api - 0.5644 * np.log10(T_F)
mu_egbogah = 10.0 ** (10.0 ** rhs_eg) - 1.0
mu_egbogah = np.clip(mu_egbogah, 1.0, 1e8)
log_mu_egbogah = np.log(mu_egbogah)

r2_egbogah = r2_score(y_true_log, log_mu_egbogah)
mae_egbogah = mean_absolute_error(y_true_log, log_mu_egbogah)

print(f"Egbogah-Ng (1990) REAL:")
print(f"  R2: {r2_egbogah:.4f}")
print(f"  MAE: {mae_egbogah:.4f} ln cP")
print(f"  Predicted range: {mu_egbogah.min():.1f} - {mu_egbogah.max():.1f} cP")
print()

# ============================================
# 3. MANCO-EX (This work) - REML LMM
# Using real_lmm_results.json
# ============================================
with open(r'C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\real_lmm_results.json') as f:
    lmm = json.load(f)

beta = lmm['beta_fixed_slope']
alpha_global = lmm['alpha_fixed_intercept']
blups = lmm['random_effects_blup']

# Conditional prediction (fixed + random)
log_pred_mex = []
for _, row in df.iterrows():
    basin = row['basin_location']
    re = blups.get(basin, 0.0)
    log_pred_mex.append(alpha_global + beta * row['phi_cascade'] + re)
log_pred_mex = np.array(log_pred_mex)

r2_mex = r2_score(y_true_log, log_pred_mex)
mae_mex = mean_absolute_error(y_true_log, log_pred_mex)

print(f"MANCO-EX (REML LMM conditional):")
print(f"  R2: {r2_mex:.4f}")
print(f"  MAE: {mae_mex:.4f} ln cP")
print()

# ============================================
# 4. LEGACY MANCO (Larter 2012)
# Simple phi_cascade → viscosity correlation
# We fit OLS: log(mu) = a + b * phi_cascade
# ============================================
from numpy.polynomial.polynomial import polyfit as npfit
coeffs_manco = np.polyfit(df['phi_cascade'].values, y_true_log, 1)
log_pred_manco = np.polyval(coeffs_manco, df['phi_cascade'].values)
r2_manco = r2_score(y_true_log, log_pred_manco)
mae_manco = mean_absolute_error(y_true_log, log_pred_manco)

print(f"Legacy MANCO v1.0 (OLS phi_cascade):")
print(f"  R2: {r2_manco:.4f}")
print(f"  MAE: {mae_manco:.4f} ln cP")
print(f"  Coefficients: slope={coeffs_manco[0]:.4f}, intercept={coeffs_manco[1]:.4f}")
print()

# Save benchmark results
benchmark_results = {
    'beggs_robinson_1975': {'r2': round(r2_beggs, 4), 'mae': round(mae_beggs, 4), 'real_implementation': True, 'note': 'Dead oil correlation with T=104F'},
    'egbogah_ng_1990': {'r2': round(r2_egbogah, 4), 'mae': round(mae_egbogah, 4), 'real_implementation': True, 'note': 'Replaced Pedersen (requires full EOS compositional data not available)'},
    'legacy_manco_ols': {'r2': round(r2_manco, 4), 'mae': round(mae_manco, 4), 'real_implementation': True, 'note': 'OLS fit of phi_cascade to log(viscosity)'},
    'manco_ex_reml': {'r2': round(r2_mex, 4), 'mae': round(mae_mex, 4), 'real_implementation': True, 'note': 'REML LMM conditional prediction'}
}

results_path = r'C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\real_benchmark_results.json'
with open(results_path, 'w') as f:
    json.dump(benchmark_results, f, indent=4)
print(f"Results saved to {results_path}")

# ============================================
# FIGURE DATA: Residual plot for LMM
# ============================================
residuals = y_true_log - log_pred_mex
resid_data_path = r'C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\residual_data.dat'
with open(resid_data_path, 'w') as f:
    f.write('fitted residual basin\n')
    for i, (_, row) in enumerate(df.iterrows()):
        basin_short = row['basin_location'].split('(')[0].strip()[:10]
        f.write(f"{log_pred_mex[i]:.4f} {residuals[i]:.6f} {basin_short}\n")

print(f"\nResidual data saved to {resid_data_path}")

# ============================================
# FIGURE DATA: BLUP caterpillar plot  
# ============================================
blup_data_path = r'C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\blup_data.dat'
with open(blup_data_path, 'w') as f:
    f.write('basin_id basin_name blup\n')
    for i, (name, val) in enumerate(sorted(blups.items(), key=lambda x: x[1])):
        short = name.split('(')[0].strip()
        f.write(f"{i} {short.replace(' ','_')} {val:.4f}\n")

print(f"BLUP data saved to {blup_data_path}")
print("\nDONE")
