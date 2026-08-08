# ==============================================================================
# MANCO-EX PUBLIC DEMONSTRATION SCRIPT (García, 2026)
# Evaluation of Exergy Loss (Delta X_d) and Eyring Dynamic Viscosity
# ==============================================================================

import numpy as np
import pandas as pd

def calculate_manco_ex_demo(csv_path):
    df = pd.read_csv(csv_path)
    print("MANCO-EX Public Dataset Evaluation (N = {})".format(len(df)))
    print("=" * 60)
    
    # Constants
    R = 8.314e-3  # kJ/(mol K)
    T0 = 298.15   # K
    eta = 0.88    # Biomarker efficiency factor
    
    # 1. Exergy Loss Index Delta X_d (kJ/mol)
    df['calculated_delta_xd'] = R * T0 * np.log(1.0 + df['phi_cascade'])
    
    # 2. Eyring Viscosity (cP) at T_res = 313.15 K
    df['calculated_eyring_visc_cp'] = 1500.0 * np.exp(df['calculated_delta_xd'] / (eta * R * 313.15))
    
    summary = df[['sample_id', 'basin_location', 'phi_cascade', 'delta_xd_kj_mol', 'viscosity_measured_cp', 'calculated_eyring_visc_cp']]
    print(summary.head(10).to_string())
    print("\nPublic demonstration evaluation completed successfully.")

if __name__ == "__main__":
    calculate_manco_ex_demo("MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv")
