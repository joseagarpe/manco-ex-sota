# MANCO-EX SOTA Engine (v3.1)

[![SSRN Preprint](https://img.shields.io/badge/SSRN-Abstract--7243483-blue.svg)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7243483)
[![Zenodo DOI](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.21826600-green.svg)](https://doi.org/10.5281/zenodo.21826600)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Official Open-Access Codebase and Manuscript Repository for MANCO Exergetic Framework (MANCO-EX v3.1)**  
*Author:* **José A. García** (Instituto de Ciencias de la Tierra, Universidad Central de Venezuela)

---

## 📌 Overview

**MANCO-EX** bridges reservoir organic geochemistry and classical second-law thermodynamics. It transforms molecular biomarker depletion indices ($\Phi_{\text{cascade}}$) into **Exergy Destruction ($\Delta X_d$, kJ/mol)** via Gouy-Stodola formulation and Eyring transition-state kinetics.

### Key Scientific Milestones (v3.1):
- **REML Linear Mixed-Effects Model (LMM):** $R^2_{\text{marginal}} = 0.18$, $R^2_{\text{conditional}} > 0.99$, $\text{MAE} = 0.0082\text{ ln cP}$, $\text{RMSE} = 0.012\text{ ln cP}$.
- **Random Slopes Likelihood Ratio Test:** $\text{LRT} = 449.05$ ($p < 10^{-15}$).
- **Thermodynamic Limit of Utility:** Bounded critical exergy loss $\Delta X_d^{\text{crit}} = 8.50 \pm 0.78\text{ kJ/mol}$ (95% CI: $[6.09, 9.20]$).
- **Benchmarking vs. Legacy Correlations:** Beggs-Robinson (1975) ($R^2 = -2.25$) and Egbogah-Ng (1990) ($R^2 = -2.70$) fail on biodegraded heavy crude suites, whereas MANCO-EX achieves ultra-low prediction error across 5 major global geological basins (Orinoco, Athabasca, Junggar, Bongor, PGRL).

---

## 📁 Repository Structure

```
PAPER_5_FUEL/
├── PAPER_FUEL_v3.1.pdf                         # Final Compiled Manuscript PDF (v3.1)
├── PAPER_FUEL_v3.1.tex                         # Complete LaTeX Source Code (v3.1)
├── MANCO_EX_SOTA_Engine.py                     # Main SOTA Engine (REML LMM & Benchmarks)
├── BASES_DE_DATOS_GEOQUIMICA/                  # Consolidated multi-basin geochemical datasets
├── run_real_lmm.py                             # REML MixedLM statistical script
├── run_random_slopes_test.py                   # Random Slopes LRT statistical test script
├── run_cascade_ablation.py                     # 4-Tier Cascade ablation study script
├── run_ridge_vif_analysis.py                   # Ridge regression & VIF diagnostic script
├── run_uncertainty_budget.py                   # Monte Carlo uncertainty propagation script
├── real_benchmarks.py                          # Empirical evaluation of Beggs-Robinson & Egbogah-Ng
├── STATISTICAL_TABLES.md                       # Consolidated statistical tables
├── LinkedIn SOTA.md                            # Technical outreach summary
├── README.md                                   # Documentation
└── LICENSE                                     # MIT License
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- `numpy`, `pandas`, `statsmodels`, `scikit-learn`

```bash
pip install numpy pandas statsmodels scikit-learn
```

### Run the SOTA Engine
```bash
python MANCO_EX_SOTA_Engine.py
```

### Output Example
```text
===============================================================================
MANCO-EX SOTA ENGINE (v3.1) - BENCHMARKING REPORT
===============================================================================
Fixed-effect Slope (beta): 3.4185
Fixed-effect Intercept (alpha): 7.4598
BLUP Basin Random Intercepts:
  - Athabasca: +1.7937
  - Orinoco:   +0.9419
  - Junggar:   -0.5364
  - Bongor:    -1.0449
  - PGRL:      -1.1543

BENCHMARKING TABLE VS PUBLISHED INDUSTRY CORRELATIONS:
--------------------------------------------------------------------------------
                                             Input Variables      R2 MAE (ln cP) RMSE (ln cP)
Beggs-Robinson (1975)                                 API, T -2.2536      2.0773       2.2035
Egbogah-Ng (1990)                                     API, T -2.6992      2.2473       2.3496
Legacy MANCO v1.0 (Larter 2012)                  Phi_cascade  0.4134      0.8264       0.9357
MANCO-EX SOTA Engine (García 2026)  Phi_cascade + Basin BLUP  0.9999      0.0082        0.0120
```

---

## 📖 Citation

If you use MANCO-EX or this codebase in your research, please cite the official SSRN preprint:

```bibtex
@article{garcia2026manco,
  author    = {Garc{\'\i}a, Jos{\'e} A.},
  title     = {Thermodynamic Limit of Utility in Biodegraded Heavy Oils: The MANCO Exergetic Framework (MANCO-EX)},
  journal   = {SSRN Electronic Journal},
  year      = {2026},
  note      = {Available at SSRN: https://ssrn.com/abstract=7243483},
  doi       = {10.2139/ssrn.7243483}
}
```

---

## 📄 License
Distributed under the **MIT License**.
