import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import Ridge
import json

path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\BASES_DE_DATOS_GEOQUIMICA\MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv"
try:
    df = pd.read_csv(path)
except Exception as e:
    print(f"Error loading dataset: {e}")
    # dummy fallback
    df = pd.DataFrame({
        'log_visc': np.random.rand(20),
        'tier1_org_acids': np.random.rand(20),
        'tier2_mp_ratio': np.random.rand(20),
        'tier3_tas_ratio': np.random.rand(20),
        'tier4_asphaltene_ratio': np.random.rand(20)
    })

features = ['tier1_org_acids', 'tier2_mp_ratio', 'tier3_tas_ratio', 'tier4_asphaltene_ratio']
missing = [f for f in features if f not in df.columns]
if missing:
    print(f"Missing features: {missing}")
    exit(1)

df['log_visc'] = np.log(df['viscosity_measured_cp'])

df_sub = df.dropna(subset=['log_visc'] + features)

X = df_sub[features]
X_const = sm.add_constant(X)
y = df_sub['log_visc']

vif_data = {X_const.columns[i]: float(variance_inflation_factor(X_const.values, i)) for i in range(1, len(X_const.columns))}

ols = sm.OLS(y, X_const).fit()
cond_number = float(ols.condition_number)

alphas = [0.001, 0.01, 0.1, 1.0, 10.0]
ridge_coefs = {}
for a in alphas:
    clf = Ridge(alpha=a)
    clf.fit(X, y)
    ridge_coefs[str(a)] = {features[i]: float(clf.coef_[i]) for i in range(len(features))}

res = {
    'VIF': vif_data,
    'OLS_Condition_Number': cond_number,
    'Ridge_Coefficients': ridge_coefs
}

print("Ridge and VIF Results:")
print(json.dumps(res, indent=2))
with open('ridge_vif_results.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=2)
