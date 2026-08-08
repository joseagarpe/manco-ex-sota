# ==============================================================================
# MANCO-EX PUBLIC DEMONSTRATION SCRIPT (v3.1 - García, 2026)
# Evaluation of Exergy Loss (Delta X_d) & REML LMM Eyring Dynamic Viscosity
# ==============================================================================

import os
import numpy as np
import pandas as pd

# Basin-specific Random Intercepts (BLUPs) from REML MixedLM (v3.1)
BLUP_BASIN_INTERCEPTS = {
    'Athabasca': 1.7937,
    'Orinoco': 0.9419,
    'Junggar': -0.5364,
    'Bongor': -1.0449,
    'PGRL': -1.1543
}

def calculate_manco_ex_v31_demo(csv_path):
    """
    Demonstrates the MANCO-EX v3.1 framework on multi-basin crude oil datasets.
    Calculates Exergy Destruction (Delta X_d) and predicts dynamic viscosity (mu, cP).
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset not found at {csv_path}")

    df = pd.read_csv(csv_path)
    print("=" * 80)
    print(f"MANCO-EX v3.1 PUBLIC DEMONSTRATION SUITE (N = {len(df)})")
    print("=" * 80)

    # 1. FIXED & RANDOM EFFECTS PARAMETERS (REML LMM v3.1)
    beta_fixed = 3.4185      # Fixed-effect slope (d(ln mu)/d(phi))
    alpha_fixed = 7.4598     # Fixed-effect global intercept
    delta_xd_crit = 8.50     # Thermodynamic Limit of Utility (kJ/mol)

    # 2. Exergy Destruction Index Delta X_d (kJ/mol)
    # Delta X_d = 0.35*Tier1 + 0.40*Tier2 + 0.15*Tier3 + 0.10*Tier4
    df['calculated_delta_xd_kj_mol'] = (
        0.35 * df['tier1_org_acids'] +
        0.40 * df['tier2_mp_ratio'] +
        0.15 * df['tier3_tas_ratio'] +
        0.10 * df['tier4_asphaltene_ratio']
    ) * 16.5  # Bounded scaling to [0, 16.5 kJ/mol]

    # 3. LMM REML Dynamic Viscosity Prediction (ln mu & mu)
    log_visc_pred = []
    for _, row in df.iterrows():
        basin = row['basin_location']
        blup = 0.0
        for b_name, b_val in BLUP_BASIN_INTERCEPTS.items():
            if b_name.lower() in basin.lower():
                blup = b_val
                break
        
        # ln(mu) = (alpha_global + blup) + beta_fixed * phi_cascade
        ln_mu = (alpha_fixed + blup) + beta_fixed * row['phi_cascade']
        log_visc_pred.append(ln_mu)

    df['pred_log_viscosity'] = log_visc_pred
    df['pred_viscosity_cp'] = np.exp(df['pred_log_viscosity'])
    df['thermo_utility'] = df['calculated_delta_xd_kj_mol'].apply(
        lambda x: 'UNECONOMIC (Enet <= 0)' if x >= delta_xd_crit else 'PRODUCIBLE (Enet > 0)'
    )

    # 4. Display Results
    cols_to_show = [
        'sample_id', 'basin_location', 'pm_level', 'phi_cascade',
        'delta_xd_kj_mol', 'viscosity_measured_cp', 'pred_viscosity_cp', 'thermo_utility'
    ]
    
    print("\nSAMPLE EVALUATION MATRIX (Top 10 Samples):")
    print("-" * 80)
    print(df[cols_to_show].head(10).to_string(index=False))

    # Metrics
    mae_log = np.mean(np.abs(np.log(df['viscosity_measured_cp']) - df['pred_log_viscosity']))
    print("\n" + "=" * 80)
    print(f"REML LMM CONDITIONAL PREDICTION PERFORMANCE:")
    print(f"  - Fixed-effect Slope (beta):     {beta_fixed:.4f} (p < 1e-6)")
    print(f"  - Conditional Error (MAE):       {mae_log:.4f} ln cP")
    print(f"  - Critical Abandonment Threshold: {delta_xd_crit:.2f} kJ/mol (Enet <= 0)")
    print("=" * 80)

if __name__ == "__main__":
    csv_file = os.path.join("BASES_DE_DATOS_GEOQUIMICA", "MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv")
    if not os.path.exists(csv_file):
        csv_file = "MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv"
    
    calculate_manco_ex_v31_demo(csv_file)
