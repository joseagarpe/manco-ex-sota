# -*- coding: utf-8 -*-
"""
Reproducible validation script for:
"Thermodynamic Coupling between Biomarker Biodegradation Cascades and Heavy Oil
Colloidal Rheology: An Irreversible Exergy Destruction Framework"
Journal: Fuel (Elsevier), Manuscript Ref: JFUE-D-26-10837 (Revision v9.1)
Author: Dr. Jose A. Garcia (Universidad Central de Venezuela)
"""
import csv
import json
import math
import random
import re
import numpy as np


def load_dataset(csv_path="delta_Xd_derivation.csv"):
    with open(csv_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows


def r2_and_rmse(y_true, y_pred):
    yt = np.asarray(y_true, dtype=float)
    yp = np.asarray(y_pred, dtype=float)
    ss_res = float(np.sum((yt - yp) ** 2))
    ss_tot = float(np.sum((yt - np.mean(yt)) ** 2))
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else float("nan")
    rmse = math.sqrt(ss_res / len(yt))
    return r2, rmse


def parse_pm_level(pm_str):
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", pm_str)]
    return sum(nums) / len(nums)


def run_validation(csv_path="delta_Xd_derivation.csv"):
    rows = load_dataset(csv_path)
    n_samples = len(rows)
    basins = sorted(list({r["basin"] for r in rows}))
    print(f"[INFO] Loaded N={n_samples} heavy oil and bitumen samples across {len(basins)} sedimentary basins.")

    # 1. Verify affine mapping: Delta_Xd = 5.10 + 3.20 * Phi_casc
    weights = (0.35, 0.40, 0.15, 0.10)
    dxd_0 = 5.10
    gamma_map = 3.20
    for r in rows:
        f1 = float(r["tier1_acid_or_polar"])
        f2 = float(r["tier2_norhopane_or_mp"])
        f3 = float(r["tier3_tas_ratio"])
        f4 = float(r["tier4_asphaltene_or_sa"])
        phi_calc = weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4
        dxd_calc = dxd_0 + gamma_map * phi_calc
        assert abs(phi_calc - float(r["phi_cascade"])) < 1e-3, f"Phi mismatch in {r['sample_id']}"
        assert abs(dxd_calc - float(r["delta_xd_kj_mol"])) < 1e-2, f"Delta_Xd mismatch in {r['sample_id']}"

    # 2. Multi-Basin ANCOVA via Ordinary Least Squares on Design Matrix
    x_dxd = np.asarray([float(r["delta_xd_kj_mol"]) for r in rows], dtype=float)
    X_ancova = np.asarray(
        [[1.0 if r["basin"] == b else 0.0 for b in basins] + [float(r["delta_xd_kj_mol"])] for r in rows],
        dtype=float,
    )
    y_obs = np.asarray([float(r["ln_visc_20c"]) for r in rows], dtype=float)
    theta_ancova, _, _, _ = np.linalg.lstsq(X_ancova, y_obs, rcond=None)
    beta_raw = float(theta_ancova[-1])
    beta_slope = round(beta_raw, 2)
    r_gas_kj = 0.0083144626
    t_ref_k = 293.15
    beta_ex = round(beta_raw * r_gas_kj * t_ref_k, 2)

    basin_intercepts = {}
    for b in basins:
        b_idx = [i for i, r in enumerate(rows) if r["basin"] == b]
        basin_intercepts[b] = round(float(np.mean(y_obs[b_idx]) - beta_slope * np.mean(x_dxd[b_idx])), 2)

    y_ancova_pred = np.asarray(
        [basin_intercepts[r["basin"]] + beta_slope * float(r["delta_xd_kj_mol"]) for r in rows],
        dtype=float,
    )
    for i, r in enumerate(rows):
        assert abs(y_ancova_pred[i] - float(r["ln_mu_pred"])) < 1e-2, f"ln_mu_pred mismatch in {r['sample_id']}"

    r2_ancova, rmse_ancova = r2_and_rmse(y_obs, y_ancova_pred)

    # Cook's distance diagnostic on multi-basin ANCOVA
    hat_matrix = X_ancova @ np.linalg.inv(X_ancova.T @ X_ancova) @ X_ancova.T
    h_ii = np.diag(hat_matrix)
    residuals = y_obs - y_ancova_pred
    p_params = X_ancova.shape[1]
    mse_ancova = float(np.sum(residuals ** 2)) / (n_samples - p_params)
    cooks_d = (residuals ** 2 / (p_params * mse_ancova)) * (h_ii / ((1.0 - h_ii) ** 2))
    max_cooks_d = float(np.max(cooks_d))

    # Basin-by-basin ANCOVA metrics (Table S2)
    basin_metrics = {}
    for b in basins:
        b_mask = [i for i, r in enumerate(rows) if r["basin"] == b]
        r2_b, rmse_b = r2_and_rmse(y_obs[b_mask], y_ancova_pred[b_mask])
        basin_metrics[b] = {
            "N": len(b_mask),
            "R2": round(r2_b, 2),
            "RMSE_ln_cP": round(rmse_b, 2),
        }

    # 3. Stratified 5-Fold Cross-Validation (out-of-fold OLS fits)
    rng_cv = random.Random(1)
    folds = [[] for _ in range(5)]
    for b in basins:
        b_indices = [i for i, r in enumerate(rows) if r["basin"] == b]
        rng_cv.shuffle(b_indices)
        for k, idx in enumerate(b_indices):
            folds[k % 5].append(idx)

    y_cv_pred = np.zeros(n_samples, dtype=float)
    for k in range(5):
        test_set = set(folds[k])
        train_idx = [i for i in range(n_samples) if i not in test_set]
        theta_k, _, _, _ = np.linalg.lstsq(X_ancova[train_idx], y_obs[train_idx], rcond=None)
        for idx in folds[k]:
            y_cv_pred[idx] = float(X_ancova[idx] @ theta_k)
    r2_cv5, rmse_cv5 = r2_and_rmse(y_obs, y_cv_pred)

    # 4. Unanchored Leave-One-Basin-Out CV (zero-shot cross-basin transfer)
    y_lobo_unanchored = np.zeros(n_samples, dtype=float)
    beta_lobo_train = {}
    for test_b in basins:
        train_basins = [b for b in basins if b != test_b]
        train_idx = [i for i, r in enumerate(rows) if r["basin"] != test_b]
        test_idx = [i for i, r in enumerate(rows) if r["basin"] == test_b]
        X_tr = np.asarray(
            [
                [1.0 if rows[i]["basin"] == b else 0.0 for b in train_basins]
                + [float(rows[i]["delta_xd_kj_mol"])]
                for i in train_idx
            ],
            dtype=float,
        )
        theta_tr, _, _, _ = np.linalg.lstsq(X_tr, y_obs[train_idx], rcond=None)
        mean_alpha_tr = float(np.mean(theta_tr[:-1]))
        beta_tr = float(theta_tr[-1])
        beta_lobo_train[test_b] = beta_tr
        for idx in test_idx:
            y_lobo_unanchored[idx] = mean_alpha_tr + beta_tr * float(rows[idx]["delta_xd_kj_mol"])
    r2_lobo_raw, rmse_lobo_raw = r2_and_rmse(y_obs, y_lobo_unanchored)

    # 5. Single-Anchor (N=1) LOBO-CV evaluated strictly on the N=55 non-anchor test fluids
    anchor_ids = {
        "Eastern Venezuela (Orinoco)": "Hernandez1983_Crude_06",
        "Junggar Basin (China)": "Chang2022_P2-40",
        "Songliao Basin (China)": "Zhong2025_Du53",
        "Western Canada (Athabasca)": "Larter2012_Case_34",
    }
    y_lobo_anchor_obs = []
    y_lobo_anchor_pred = []
    for test_b in basins:
        beta_tr = beta_lobo_train[test_b]
        anchor_row = next(r for r in rows if r["sample_id"] == anchor_ids[test_b])
        alpha_local = float(anchor_row["ln_visc_20c"]) - beta_tr * float(anchor_row["delta_xd_kj_mol"])
        for r in rows:
            if r["basin"] == test_b and r["sample_id"] != anchor_ids[test_b]:
                y_lobo_anchor_obs.append(float(r["ln_visc_20c"]))
                y_lobo_anchor_pred.append(alpha_local + beta_tr * float(r["delta_xd_kj_mol"]))
    r2_lobo_anchor, rmse_lobo_anchor = r2_and_rmse(y_lobo_anchor_obs, y_lobo_anchor_pred)

    # 6. Empirical Literature Benchmarks evaluated at T_ref = 20 C (68 F) (Table 2)
    t_ref_f = 68.0
    api_vals = [float(r["api_gravity"]) for r in rows]
    pred_beggs = []
    pred_deghetto = []
    for a in api_vals:
        # Beggs & Robinson (1975)
        z_br = 3.0324 - 0.02023 * a
        x_br = (10.0 ** z_br) * (t_ref_f ** (-1.163))
        mu_br = max(1.0, min(1e8, (10.0 ** x_br) - 1.0))
        pred_beggs.append(math.log(mu_br))
        # De Ghetto et al. (1995) SPE-30316 piecewise Modified Egbogah dead-oil correlation
        if a < 10.0:
            val_dg = 1.90296 - 0.012619 * a - 0.61748 * math.log10(t_ref_f)
        else:
            val_dg = 2.06492 - 0.0179 * a - 0.70226 * math.log10(t_ref_f)
        mu_dg = (10.0 ** (10.0 ** val_dg)) - 1.0
        pred_deghetto.append(math.log(mu_dg))
    r2_beggs, rmse_beggs = r2_and_rmse(y_obs, pred_beggs)
    r2_deghetto, rmse_deghetto = r2_and_rmse(y_obs, pred_deghetto)

    pm_vals = np.asarray([parse_pm_level(r["pm_level"]) for r in rows], dtype=float)
    X_pm = np.column_stack([np.ones_like(pm_vals), pm_vals])
    theta_pm, _, _, _ = np.linalg.lstsq(X_pm, y_obs, rcond=None)
    r2_pm, rmse_pm = r2_and_rmse(y_obs, X_pm @ theta_pm)

    # 7. Monte Carlo NPV breakeven simulation (Equation 4, B = 10,000 iterations)
    p_oil_nom = 75.0
    c_dil_nom = 65.0
    q_prod = 500000.0
    a1 = 12500.0
    b1_nom = 0.32
    k_dil = 0.067
    capex = 25.0e6
    r_disc_nom = 0.10
    n_years = 20
    alpha_ref = -6.39

    # Analytical baseline breakeven (NPV = 0 at nominal parameters)
    pv_nom = (1.0 - (1.0 + r_disc_nom) ** (-n_years)) / r_disc_nom
    target_opex_nom = p_oil_nom * q_prod - (capex / pv_nom)
    mu_star_nom = (target_opex_nom / (a1 + q_prod * c_dil_nom * k_dil)) ** (1.0 / b1_nom)
    dxd_star_baseline = (math.log(mu_star_nom) - alpha_ref) / round(beta_slope, 2)

    # Stochastic propagation (B = 10,000 iterations)
    rng_mc = random.Random(21)
    mu_pivot = math.exp(8.40)
    rho_price_dil = 0.37
    dxd_stars = []
    for _ in range(10000):
        z1 = rng_mc.gauss(0.0, 1.0)
        z2 = rng_mc.gauss(0.0, 1.0)
        p_oil = max(25.0, p_oil_nom + 15.0 * z1)
        c_dil = max(
            20.0,
            c_dil_nom + 12.0 * (rho_price_dil * z1 + math.sqrt(1.0 - rho_price_dil ** 2) * z2),
        )
        b1 = max(0.20, min(0.45, rng_mc.gauss(b1_nom, 0.04)))
        r_disc = max(0.03, min(0.20, rng_mc.gauss(r_disc_nom, 0.02)))
        pv_factor = (1.0 - (1.0 + r_disc) ** (-n_years)) / r_disc
        target_opex = p_oil * q_prod - (capex / pv_factor)
        if target_opex > 0:
            denom = (a1 + q_prod * c_dil * k_dil) * (mu_pivot ** (b1_nom - b1))
            mu_star = (target_opex / denom) ** (1.0 / b1)
            dxd_star = (math.log(mu_star) - alpha_ref) / round(beta_slope, 2)
            dxd_stars.append(dxd_star)

    mc_arr = np.asarray(dxd_stars, dtype=float)
    mean_dxd_star = float(np.mean(mc_arr))
    std_dxd_star = float(np.std(mc_arr))
    ci_95_low = mean_dxd_star - 2.0 * std_dxd_star
    ci_95_high = mean_dxd_star + 2.0 * std_dxd_star

    results = {
        "Manuscript_Reference": "JFUE-D-26-10837 (Revision v9.1)",
        "N_Samples": n_samples,
        "N_Basins": len(basins),
        "Common_Slope_beta_mol_per_kJ": round(beta_slope, 2),
        "Dimensionless_Coupling_beta_ex": round(beta_ex, 2),
        "Max_Cooks_Distance_D": round(max_cooks_d, 2),
        "Global_Multi_Basin_ANCOVA": {
            "R2": round(r2_ancova, 2),
            "RMSE_ln_cP": round(rmse_ancova, 2),
        },
        "Stratified_5Fold_CV": {
            "R2": round(r2_cv5, 2),
            "RMSE_ln_cP": round(rmse_cv5, 2),
        },
        "Unanchored_LOBO_CV": {
            "R2": round(r2_lobo_raw, 2),
            "RMSE_ln_cP": round(rmse_lobo_raw, 2),
        },
        "Single_Anchor_LOBO_CV_N1": {
            "R2": round(r2_lobo_anchor, 2),
            "RMSE_ln_cP": round(rmse_lobo_anchor, 2),
        },
        "Literature_Benchmarks_Table_2": {
            "Beggs_Robinson_1975": {
                "R2": round(r2_beggs, 2),
                "RMSE_ln_cP": round(rmse_beggs, 2),
            },
            "De_Ghetto_1995_Piecewise": {
                "R2": round(r2_deghetto, 2),
                "RMSE_ln_cP": round(rmse_deghetto, 2),
            },
            "Linear_PM_Scale": {
                "R2": round(r2_pm, 2),
                "RMSE_ln_cP": round(rmse_pm, 2),
            },
        },
        "Basin_Metrics_Table_S2": basin_metrics,
        "Exergoeconomic_Abandonment_Threshold_kJ_per_mol": {
            "Baseline_Breakeven": round(dxd_star_baseline, 2),
            "Monte_Carlo_Mean": round(mean_dxd_star, 2),
            "Std_Dev": round(std_dxd_star, 2),
            "CI_95": [round(ci_95_low, 2), round(ci_95_high, 2)],
        },
    }

    with open("pls_lobo_cv_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(
        f"[RESULTS] Multi-Basin ANCOVA: R^2 = {results['Global_Multi_Basin_ANCOVA']['R2']}, "
        f"RMSE = {results['Global_Multi_Basin_ANCOVA']['RMSE_ln_cP']} ln(cP) "
        f"(beta = {results['Common_Slope_beta_mol_per_kJ']} mol/kJ, max Cook's D = {results['Max_Cooks_Distance_D']})"
    )
    print(
        f"[RESULTS] Stratified 5-Fold CV: R^2 = {results['Stratified_5Fold_CV']['R2']}, "
        f"RMSE = {results['Stratified_5Fold_CV']['RMSE_ln_cP']} ln(cP)"
    )
    print(
        f"[RESULTS] Unanchored LOBO-CV: R^2 = {results['Unanchored_LOBO_CV']['R2']}, "
        f"RMSE = {results['Unanchored_LOBO_CV']['RMSE_ln_cP']} ln(cP)"
    )
    print(
        f"[RESULTS] Single-Anchor LOBO (N=1): R^2 = {results['Single_Anchor_LOBO_CV_N1']['R2']}, "
        f"RMSE = {results['Single_Anchor_LOBO_CV_N1']['RMSE_ln_cP']} ln(cP)"
    )
    print(
        f"[RESULTS] Exergoeconomic Abandonment Threshold: Delta_Xd* = "
        f"{results['Exergoeconomic_Abandonment_Threshold_kJ_per_mol']['Monte_Carlo_Mean']} +/- "
        f"{results['Exergoeconomic_Abandonment_Threshold_kJ_per_mol']['Std_Dev']} kJ/mol "
        f"(95% CI: {results['Exergoeconomic_Abandonment_Threshold_kJ_per_mol']['CI_95']})"
    )


if __name__ == "__main__":
    run_validation()
