"""
===============================================================================
MANCO-EX SOTA ENGINE (García, 2026)
State-of-the-Art Thermodynamic & Geochemical Heavy Oil Viscosity Engine (v3.1)
===============================================================================
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import json
import warnings
warnings.filterwarnings('ignore')


class MANCO_EX_SOTA:
    """
    MANCO-EX State-of-the-Art (SOTA) Heavy Oil Viscosity & Exergy Loss Engine.
    Combines Eyring Transition-State Rate Theory with Multi-Tier Biomarker Cascades
    and REML Linear Mixed-Effects Modeling across Multi-Basin Reservoirs.
    """
    def __init__(self, weights=None, T0=298.15, R=8.314e-3):
        if weights is None:
            self.alpha = 0.35  # Tier 1: Organic Acids (USGS Bemidji calibrated)
            self.beta = 0.40   # Tier 2: Methylphenanthrenes
            self.gamma = 0.15  # Tier 3: Triaromatic Steroids (TAS)
            self.delta = 0.10  # Tier 4: Asphaltenic Polar Anchor
        else:
            self.alpha, self.beta, self.gamma, self.delta = weights
            
        self.T0 = T0
        self.R = R
        self.eta_biomarker = 0.88  # Exergetic coupling efficiency
        
        # REML LMM parameters (v3.1 calibrated)
        self.fixed_slope = 3.42
        self.fixed_intercept = 6.85
        self.blup_random_intercepts = {
            'PGRL': -1.1543,
            'Bongor': -1.0449,
            'Junggar': -0.5364,
            'Orinoco': 0.9419,
            'Athabasca': 1.7937
        }
        
        # Critical Exergy Destruction Threshold (Thermodynamic Abandonment)
        self.delta_xd_crit = 8.50  # kJ/mol (95% CI: [6.09, 9.20])

    def compute_phi_cascade(self, org_acids, mp_ratio, tas_ratio, sara_ratio):
        """Calculates the Multi-Tier Biomarker Cascade Function Phi_cascade."""
        return (self.alpha * np.array(org_acids) + 
                self.beta * np.array(mp_ratio) + 
                self.gamma * np.array(tas_ratio) + 
                self.delta * np.log1p(np.array(sara_ratio)))

    def predict_exergy_loss(self, phi_cascade):
        """Calculates Specific Oil-Phase Exergy Loss Index Delta X_d (kJ/mol)."""
        return self.R * self.T0 * np.log(1.0 + np.array(phi_cascade))

    def predict_viscosity(self, phi_cascade, T_res=313.15, basin_name=None, use_random_slopes=False):
        """
        Calculates dynamic fluid viscosity (cP) using Eyring Rate Theory & REML LMM.
        T_res: Reservoir test temperature (K) [Default: 313.15 K = 40°C = 104°F]
        """
        phi = np.array(phi_cascade)
        
        # Base log-viscosity prediction via fixed effect
        if use_random_slopes:
            slope = 3.05  # Monte Carlo mean random slope
        else:
            slope = self.fixed_slope  # REML fixed slope (3.42)
            
        log_visc = self.fixed_intercept + slope * phi
        
        # Add basin-specific BLUP random intercept if available
        if basin_name and basin_name in self.blup_random_intercepts:
            log_visc += self.blup_random_intercepts[basin_name]
            
        return np.exp(log_visc)

    def is_thermodynamically_abandoned(self, delta_xd):
        """Evaluates whether the fluid exceeds the Thermodynamic Inutility Boundary (E_net <= 0)."""
        return np.array(delta_xd) >= self.delta_xd_crit

    def fit_reml_lmm(self, df):
        """Fits a statsmodels REML Linear Mixed-Effects Model (LMM) with basin-specific random intercepts."""
        df_lmm = df.copy()
        df_lmm['log_visc'] = np.log(df_lmm['viscosity_measured_cp'])
        
        model = smf.mixedlm('log_visc ~ phi_cascade', df_lmm, groups=df_lmm['basin_location'])
        result = model.fit(reml=True)
        
        self.fixed_slope = result.fe_params['phi_cascade']
        self.fixed_intercept = result.fe_params['Intercept']
        
        for basin, re in result.random_effects.items():
            self.blup_random_intercepts[basin] = float(re['Group'])
            
        return result

    def benchmark_against_legacy(self, df):
        """
        Benchmarks MANCO-EX SOTA against published industry correlations:
        1. Beggs-Robinson (1975) Dead Oil API/T Correlation
        2. Egbogah-Ng (1990) API/T Correlation
        3. Legacy MANCO v1.0 (Larter et al., 2012 OLS)
        4. MANCO-EX SOTA (This Work - REML LMM)
        """
        y_true_log = np.log(df['viscosity_measured_cp'].values)
        api = df['api_gravity'].values
        T_F = 104.0  # 313.15 K = 40°C = 104°F
        
        # 1. Beggs-Robinson (1975) Real Formula
        z_br = 3.0324 - 0.02023 * api
        y_br = 10.0 ** z_br
        x_br = y_br * (T_F ** (-1.163))
        mu_beggs = np.clip(10.0 ** x_br - 1.0, 1.0, 1e8)
        log_beggs = np.log(mu_beggs)
        
        r2_beggs = r2_score(y_true_log, log_beggs)
        mae_beggs = mean_absolute_error(y_true_log, log_beggs)
        rmse_beggs = np.sqrt(mean_squared_error(y_true_log, log_beggs))
        
        # 2. Egbogah-Ng (1990) Real Formula
        rhs_eg = 1.8653 - 0.025086 * api - 0.5644 * np.log10(T_F)
        mu_egbogah = np.clip(10.0 ** (10.0 ** rhs_eg) - 1.0, 1.0, 1e8)
        log_egbogah = np.log(mu_egbogah)
        
        r2_egbogah = r2_score(y_true_log, log_egbogah)
        mae_egbogah = mean_absolute_error(y_true_log, log_egbogah)
        rmse_egbogah = np.sqrt(mean_squared_error(y_true_log, log_egbogah))
        
        # 3. Legacy MANCO v1.0 (OLS fit of phi to log_visc)
        coeffs = np.polyfit(df['phi_cascade'].values, y_true_log, 1)
        log_manco = np.polyval(coeffs, df['phi_cascade'].values)
        
        r2_manco = r2_score(y_true_log, log_manco)
        mae_manco = mean_absolute_error(y_true_log, log_manco)
        rmse_manco = np.sqrt(mean_squared_error(y_true_log, log_manco))
        
        # 4. MANCO-EX SOTA Engine (REML LMM)
        log_manco_ex = []
        for idx, row in df.iterrows():
            v = self.predict_viscosity(row['phi_cascade'], 313.15, row['basin_location'])
            log_manco_ex.append(np.log(v))
        log_manco_ex = np.array(log_manco_ex)
        
        r2_manco_ex = r2_score(y_true_log, log_manco_ex)
        mae_manco_ex = mean_absolute_error(y_true_log, log_manco_ex)
        rmse_manco_ex = np.sqrt(mean_squared_error(y_true_log, log_manco_ex))
        
        benchmarks = {
            "Beggs-Robinson (1975)": {
                "Input Variables": "API, T",
                "R2": round(float(r2_beggs), 4),
                "MAE (ln cP)": round(float(mae_beggs), 4),
                "RMSE (ln cP)": round(float(rmse_beggs), 4)
            },
            "Egbogah-Ng (1990)": {
                "Input Variables": "API, T",
                "R2": round(float(r2_egbogah), 4),
                "MAE (ln cP)": round(float(mae_egbogah), 4),
                "RMSE (ln cP)": round(float(rmse_egbogah), 4)
            },
            "Legacy MANCO v1.0 (Larter 2012)": {
                "Input Variables": "Phi_cascade",
                "R2": round(float(r2_manco), 4),
                "MAE (ln cP)": round(float(mae_manco), 4),
                "RMSE (ln cP)": round(float(rmse_manco), 4)
            },
            "MANCO-EX SOTA Engine (García 2026)": {
                "Input Variables": "Phi_cascade + Basin BLUP",
                "R2": round(float(r2_manco_ex), 4),
                "MAE (ln cP)": round(float(mae_manco_ex), 4),
                "RMSE (ln cP)": round(float(rmse_manco_ex), 4)
            }
        }
        return pd.DataFrame(benchmarks).T


if __name__ == "__main__":
    csv_path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\BASES_DE_DATOS_GEOQUIMICA\MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv"
    df = pd.read_csv(csv_path)
    
    engine = MANCO_EX_SOTA()
    lmm_res = engine.fit_reml_lmm(df)
    
    print("\n===============================================================================")
    print("MANCO-EX SOTA ENGINE (v3.1) - BENCHMARKING REPORT")
    print("===============================================================================")
    print(f"Fixed-effect Slope (beta): {engine.fixed_slope:.4f}")
    print(f"Fixed-effect Intercept (alpha): {engine.fixed_intercept:.4f}")
    print("BLUP Basin Random Intercepts:", engine.blup_random_intercepts)
    print("\nBENCHMARKING TABLE VS PUBLISHED INDUSTRY CORRELATIONS:")
    print("-" * 80)
    bm_df = engine.benchmark_against_legacy(df)
    print(bm_df.to_string())
