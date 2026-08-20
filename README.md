# MANCO-EX Framework (Accepted in Fuel, Q1)

[![Zenodo DOI](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.21826600-green.svg)](https://doi.org/10.5281/zenodo.21826600)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Accepted](https://img.shields.io/badge/Status-Accepted_in_Fuel_(Q1)-blue.svg)]()

**Official Open-Access Codebase and Manuscript Repository for MANCO Exergetic Framework**  
*Author:* **José A. García** (Instituto de Ciencias de la Tierra, Universidad Central de Venezuela)

---

## ⚡ Overview

**MANCO-EX** bridges reservoir organic geochemistry and classical second-law thermodynamics. It transforms molecular biomarker depletion indices (Phi_cascade) into **Exergy Destruction (Delta Xd, kJ/mol)** via Gouy-Stodola formulation and Eyring transition-state kinetics.

### Key Scientific Milestones (Accepted Version V7.4):
- **Thermodynamic Reinterpretation:** Proves that the destruction of light aromatics (maltenes) triggers severe asphaltene pi-pi orbital stacking, driving macroscopic viscosity exponentially upward.
- **Statistical Validation (PLS & LOBO-CV):** Validated on a global dataset of 41 samples from 5 geological basins. Partial Least Squares (PLS) Regression was used to resolve collinearity (VIF > 20), combined with rigorous Leave-One-Basin-Out Cross-Validation (LOBO-CV).
- **Predictive Metrics:** Out-of-sample R^2_LOBO = 0.88 and RMSE_LOBO = 0.42 ln(cP).
- **Exergoeconomic Pivot Boundary:** Monte Carlo simulations (B=10,000 at WTI ) define the thermodynamic limit of utility at Delta Xd = 8.50 +/- 0.41 kJ/mol. Beyond this threshold, the strategy pivots from high-OPEX liquid lifting to **Biogenic Methane Harvesting**.

---

## 📂 Repository Structure

`
PAPER_5_FUEL/
├── PAPER_FUEL_v7.4.pdf                         # Final Accepted Manuscript PDF (V7.4)
├── PAPER_FUEL_v7.4.tex                         # Complete LaTeX Source Code (V7.4)
├── MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv    # Consolidated multi-basin geochemical dataset
├── run_pls_lobo_cv.py                          # Main PLS and LOBO-CV validation engine
├── pls_lobo_cv_results.json                    # Exported mathematical metrics matching the paper
├── README.md                                   # Documentation
└── LICENSE                                     # MIT License
`

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- 
umpy, pandas, scikit-learn

`ash
pip install numpy pandas scikit-learn
`

### Run the Validation Engine
`ash
python run_pls_lobo_cv.py
`

### Output Example
`	ext
[SYSTEM] Initiating PLS and LOBO-CV routine...
Data Loaded: N=41 samples across 5 basins.

[RESULTS] R^2_LOBO: 0.88 | RMSE_LOBO: 0.42 ln(cP)
[SYSTEM] Results saved.
`

---

## 📝 Citation

If you use MANCO-EX or this codebase in your research, please cite the final published paper in **Fuel** (DOI pending publication).

---

## 📜 License
Distributed under the **MIT License**.
