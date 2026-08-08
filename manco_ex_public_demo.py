# ==============================================================================
# MANCO-EX PUBLIC DEMONSTRATION SCRIPT (García, 2026)
# Open-Access Evaluation Suite for Exergy Destruction (Delta X_d) & Eyring Viscosity
# ==============================================================================
# Note: This is the public demonstration suite for external evaluation.
# Proprietary fitting engines and commercial optimization algorithms remain 
# protected under technical intellectual property (A-IP Acervo Tecnológico).
# ==============================================================================

import os
import numpy as np
import pandas as pd

def calculate_manco_ex_public_demo(csv_path):
    """
    Public demonstration function for the MANCO Exergetic Framework (MANCO-EX).
    Evaluates Exergy Loss (Delta X_d, kJ/mol) and predicts baseline Eyring dynamic viscosity.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset file not found at: {csv_path}")

    df = pd.read_csv(csv_path)
    print("=" * 80)
    print(f"MANCO-EX PUBLIC DEMONSTRATION SUITE (N = {len(df)} Muestras Multi-Cuenca)")
    print("=" * 80)

    # 1. Exergy Loss Index Delta X_d (kJ/mol) - Public Form
    # Combined cascade weighting across Organic Acids, Methylphenanthrenes, TAS Steroids, & SARA
    df['calculated_delta_xd_kj_mol'] = (
        0.35 * df['tier1_org_acids'] +
        0.40 * df['tier2_mp_ratio'] +
        0.15 * df['tier3_tas_ratio'] +
        0.10 * df['tier4_asphaltene_ratio']
    ) * 16.5  # Bounded physical scaling

    # 2. Public Eyring Viscosity Approximation (cP)
    # Demonstration baseline model for public verification
    alpha_demo = 7.46
    beta_demo = 3.42
    df['demo_log_viscosity'] = alpha_demo + beta_demo * df['phi_cascade']
    df['demo_viscosity_cp'] = np.exp(df['demo_log_viscosity'])

    # 3. Thermodynamic Limit of Utility Evaluation (Delta X_d >= 8.50 kJ/mol)
    df['thermo_utility'] = df['calculated_delta_xd_kj_mol'].apply(
        lambda x: 'UNECONOMIC (Enet <= 0)' if x >= 8.50 else 'PRODUCIBLE (Enet > 0)'
    )

    # 4. Display Results
    cols_to_show = [
        'sample_id', 'basin_location', 'pm_level', 'phi_cascade',
        'delta_xd_kj_mol', 'viscosity_measured_cp', 'demo_viscosity_cp', 'thermo_utility'
    ]

    print("\nMATRIZ DE EVALUACIÓN PÚBLICA (Muestras Representativas):")
    print("-" * 80)
    print(df[cols_to_show].head(10).to_string(index=False))
    print("-" * 80)
    print("\nEvaluación demostrativa pública completada con éxito.")
    print("Para licencias comerciales, integración PVT/EOS o algoritmos de cuenca completos,")
    print("contactar a: contacto@josegarciaphd.com")
    print("=" * 80)

if __name__ == "__main__":
    csv_file = os.path.join("BASES_DE_DATOS_GEOQUIMICA", "MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv")
    if not os.path.exists(csv_file):
        csv_file = "MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv"
    
    calculate_manco_ex_public_demo(csv_file)
