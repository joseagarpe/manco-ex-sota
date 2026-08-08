import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
import json
import os

path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\BASES_DE_DATOS_GEOQUIMICA\MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv"
try:
    df = pd.read_csv(path)
except Exception as e:
    print(f"Error loading {path}: {e}")
    # dummy fallback
    df = pd.DataFrame({
        'log_visc': np.random.rand(20),
        'phi_cascade': np.random.rand(20),
        'tier1_org_acids': np.random.rand(20),
        'tier2_mp_ratio': np.random.rand(20),
        'tier3_tas_ratio': np.random.rand(20),
        'tier4_asphaltene_ratio': np.random.rand(20),
        'basin_location': ['A']*10 + ['B']*10
    })

df['log_visc'] = np.log(df['viscosity_measured_cp'])

configs = [
    ("Tier 1", "tier1_org_acids"),
    ("Tier 2", "tier2_mp_ratio"),
    ("Tier 3", "tier3_tas_ratio"),
    ("Tier 4", "tier4_asphaltene_ratio"),
    ("Tiers 1+2", "tier1_org_acids + tier2_mp_ratio"),
    ("Tiers 1+2+3", "tier1_org_acids + tier2_mp_ratio + tier3_tas_ratio"),
    ("Full Cascade", "phi_cascade")
]

results = []
for name, form in configs:
    cols = ['log_visc', 'basin_location'] + form.replace(' ', '').split('+')
    if 'phi_cascade' in form:
        cols = ['log_visc', 'basin_location', 'phi_cascade']
    
    missing = [c for c in cols if c not in df.columns]
    if missing:
        print(f"Skipping {name}, missing columns: {missing}")
        continue
        
    df_sub = df.dropna(subset=cols)
    
    try:
        m = smf.mixedlm(f"log_visc ~ {form}", df_sub, groups=df_sub["basin_location"]).fit()
        
        var_resid = m.scale
        var_random = m.cov_re.iloc[0, 0]
        fitted_fixed = m.predict(df_sub)
        var_fixed = np.var(fitted_fixed)
        
        tot_var = var_fixed + var_random + var_resid
        r2_marg = var_fixed / tot_var if tot_var > 0 else 0
        r2_cond = (var_fixed + var_random) / tot_var if tot_var > 0 else 0
        mae = np.mean(np.abs(df_sub['log_visc'] - m.fittedvalues))
        
        results.append({
            "Model": name,
            "Formula": form,
            "R2_marginal": float(r2_marg),
            "R2_conditional": float(r2_cond),
            "MAE": float(mae)
        })
    except Exception as e:
        print(f"Error fitting {name}: {e}")

print("| Model | Formula | R2 Marginal | R2 Conditional | MAE |")
print("|---|---|---|---|---|")
for r in results:
    print(f"| {r['Model']} | {r['Formula']} | {r['R2_marginal']:.4f} | {r['R2_conditional']:.4f} | {r['MAE']:.4f} |")

with open('ablation_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
