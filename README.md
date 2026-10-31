# MANCO-EX: Thermodynamic Coupling between Biomarker Biodegradation Cascades and Heavy Oil Colloidal Rheology

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23826470.svg)](https://doi.org/10.5281/zenodo.23826470)
[![Preprint: SSRN](https://img.shields.io/badge/Preprint-SSRN--7243483-blue.svg)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7243483)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Validation Codebase and Harmonized Multi-Basin Geochemical Dataset ($N=59$) for Revision v9.1 (`JFUE-D-26-10837`, *Fuel*)**  
*Author:* **Dr. José A. García** (Instituto de Ciencias de la Tierra, Facultad de Ciencias, Universidad Central de Venezuela)  
*ORCID:* `0000-0003-2873-2281`

---

## Overview

**MANCO-EX** links molecular biomarker biodegradation cascades (`Phi_casc`, tracking sequential consumption of carboxylic acids, alkylnaphthalenes/methylphenanthrenes, triaromatic steroids, and SARA fractions) to macroscopic dynamic viscosity (`ln mu` at $20^\circ\text{C}$) via a thermodynamically motivated composite index of cumulative specific chemical exergy destruction (`Delta X_d`, kJ/mol) grounded in the Gouy–Stodola theorem and Eyring transition-state rate theory.

### Principal Quantitative Findings ($N=59$ across 4 Sedimentary Basins)
- **Harmonized Multi-Basin Dataset ($N=59$):** Western Canada Athabasca ($N=15$; Larter et al., 2012), Junggar Basin Chepaizi Uplift ($N=15$; Chang et al., 2022), Eastern Venezuelan Basin Orinoco Oil Belt ($N=15$; Hernández et al., 1983; López, 2014), and Songliao Basin ($N=14$; Zhong et al., 2025), all standardized to $T_{\text{ref}} = 20^\circ\text{C}$ ($293.15\text{ K}$).
- **Intra-Basin Thermodynamic Scaling:** Common slope $\beta = 2.19 \pm 0.25\text{ mol/kJ}$ (dimensionless activation coupling $\beta_{\text{ex}} = 5.33 \pm 0.61$, baseline activation energy $E_{a0} = 42.1 \pm 2.3\text{ kJ/mol}$).
- **Cross-Validation Performance:**
  - Pooled Multi-Basin ANCOVA: $R^2 = 0.88$, $\text{RMSE} = 0.94\ln(\text{cP})$.
  - Stratified 5-Fold Cross-Validation: $R^2 = 0.86$, $\text{RMSE} = 1.02\ln(\text{cP})$.
  - Unanchored Leave-One-Basin-Out (LOBO-CV): $R^2 < 0$, $\text{RMSE} = 3.22\ln(\text{cP})$ (regional baseline intercepts $\alpha_j$ account for $72.2\%$ of total viscosity variance).
  - Single-Anchor ($N=1$) LOBO-CV: $R^2 = 0.83$, $\text{RMSE} = 1.15\ln(\text{cP})$.
- **Exergoeconomic Abandonment Boundary:** Discounted Net Present Value ($\text{NPV} = 0$, $B = 10{,}000$ Monte Carlo iterations) identifies a baseline screening threshold at $\Delta X_d^* = 6.85 \pm 0.35\text{ kJ/mol}$ (95% CI: $[6.15, 7.55]\text{ kJ/mol}$) marking the operational transition from viscous bitumen lifting to subsurface biogenic methane recovery.

---

## Repository Contents

```text
├── delta_Xd_derivation.xlsx       # Step-by-step tier proxies (f1-f4), Phi_casc, Delta_Xd, and ANCOVA predictions (N=59)
├── delta_Xd_derivation.csv        # CSV mirror of the derivation table
├── source_traceability.xlsx       # Primary literature citations, DOIs, well IDs, and ASTM viscometry protocols (N=59)
├── source_traceability.csv        # CSV mirror of the provenance table
├── run_pls_lobo_cv.py             # Reproducible validation & Monte Carlo NPV breakeven script
├── pls_lobo_cv_results.json       # Exported validation metrics for Revision v9.1
└── README.md                      # Repository documentation
```

---

## Quick Start

```bash
python run_pls_lobo_cv.py
```

### Expected Output
```text
[INFO] Loaded N=59 heavy oil and bitumen samples across 4 sedimentary basins.
[RESULTS] Multi-Basin ANCOVA: R^2 = 0.88, RMSE = 0.94 ln(cP) (beta = 2.19 mol/kJ, max Cook's D = 0.14)
[RESULTS] Stratified 5-Fold CV: R^2 = 0.86, RMSE = 1.02 ln(cP)
[RESULTS] Unanchored LOBO-CV: R^2 = -0.38, RMSE = 3.22 ln(cP)
[RESULTS] Single-Anchor LOBO (N=1): R^2 = 0.83, RMSE = 1.15 ln(cP)
[RESULTS] Exergoeconomic Abandonment Threshold: Delta_Xd* = 6.85 +/- 0.35 kJ/mol (95% CI: [6.15, 7.55])
```

---

## License
Distributed under the **MIT License**.
