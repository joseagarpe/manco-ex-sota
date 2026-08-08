import pandas as pd
import numpy as np
import json

path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\BASES_DE_DATOS_GEOQUIMICA\MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv"
try:
    df = pd.read_csv(path)
except Exception as e:
    print(f"Error loading dataset: {e}")
    # dummy fallback
    df = pd.DataFrame({
        'log_visc': np.random.rand(20),
        'phi_cascade': np.random.rand(20),
        'basin_location': ['A']*10 + ['B']*10
    })

df['log_visc'] = np.log(df['viscosity_measured_cp'])

df = df.dropna(subset=['log_visc', 'phi_cascade', 'basin_location']).copy()

B = 10000
np.random.seed(42)

def fast_slope(x, y):
    x_mean = np.mean(x, axis=0)
    y_mean = np.mean(y, axis=0)
    num = np.sum((x - x_mean) * (y - y_mean), axis=0)
    den = np.sum((x - x_mean)**2, axis=0)
    return num / den

N = len(df)
y_orig = df['log_visc'].values.reshape(-1, 1)
x_orig = df['phi_cascade'].values.reshape(-1, 1)

noise_x = np.random.normal(0, 0.05, size=(N, B))
x_sim = x_orig * (1 + noise_x)

noise_y = np.random.normal(0, 0.03, size=(N, B))
y_sim = y_orig * (1 + noise_y)

slopes_sim = fast_slope(x_sim, y_sim)
slope_baseline = fast_slope(x_orig, y_orig)[0]
relative_shift = slopes_sim / slope_baseline

beta_nominal = 3.42
delta_x_nominal = 8.50

beta_sim = beta_nominal * relative_shift
delta_x_sim = delta_x_nominal * relative_shift

res = {
    'beta_LMM': {
        'mean': float(np.mean(beta_sim)),
        'std': float(np.std(beta_sim)),
        'ci_95_lower': float(np.percentile(beta_sim, 2.5)),
        'ci_95_upper': float(np.percentile(beta_sim, 97.5))
    },
    'delta_X_d_crit': {
        'mean': float(np.mean(delta_x_sim)),
        'std': float(np.std(delta_x_sim)),
        'ci_95_lower': float(np.percentile(delta_x_sim, 2.5)),
        'ci_95_upper': float(np.percentile(delta_x_sim, 97.5))
    }
}

print("Uncertainty Budget Results (B=10000):")
print(json.dumps(res, indent=2))

with open('uncertainty_budget_results.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=2)
