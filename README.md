# MANCO-EX: Global Exergetic Biodegradation Framework

[![Zenodo DOI](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.21826600-green.svg)](https://doi.org/10.5281/zenodo.21826600)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Open-Access Validation Codebase and Multi-Basin Geochemical Dataset for the MANCO Exergetic Framework**  
*Author:* **José A. García** (Instituto de Ciencias de la Tierra, Universidad Central de Venezuela)

---

## Overview

**MANCO-EX** establishes a physical link between reservoir organic geochemistry and irreversible thermodynamics. It transforms molecular biomarker depletion indices (Phi_cascade) into **Specific Chemical Exergy Destruction (Delta Xd, kJ/mol)** via Gouy-Stodola formulations and Eyring transition-state kinetics.

### Key Methodological Capabilities:
- **Colloidal Mechanics Coupling:** Links the destruction of the natural aromatic solvent phase (maltenes) to asphaltene pi-pi orbital stacking and exponential viscosity growth.
- **Statistical Validation (PLS & LOBO-CV):** Implements Partial Least Squares (PLS) Regression to handle biomarker collinearity (VIF > 20) with strict Leave-One-Basin-Out Cross-Validation (LOBO-CV) across 5 geological basins (N=41).
- **Predictive Metrics:** Out-of-sample R^2_LOBO = 0.88 and RMSE_LOBO = 0.42 ln(cP).
- **Exergoeconomic Boundary:** Quantifies the thermodynamic threshold (Delta Xd = 8.50 +/- 0.41 kJ/mol) where lifting and diluent OPEX dictate an operational pivot toward biogenic methane harvesting.

---

## Repository Structure

`
├── MANCO_GLOBAL_CHROMATOGRAPHIC_DATASET.csv    # Consolidated multi-basin geochemical dataset (N=41)
├── run_pls_lobo_cv.py                          # PLS and LOBO-CV validation engine
├── pls_lobo_cv_results.json                    # Exported mathematical metrics
└── README.md                                   # Documentation
`

---

## Quick Start

### Prerequisites
- Python 3.10+
- numpy, pandas, scikit-learn

`ash
pip install numpy pandas scikit-learn
`

### Run the Validation Engine
`ash
python run_pls_lobo_cv.py
`

### Output
`	ext
[SYSTEM] Initiating PLS and LOBO-CV routine...
Data Loaded: N=41 samples across 5 basins.

[RESULTS] R^2_LOBO: 0.88 | RMSE_LOBO: 0.42 ln(cP)
[SYSTEM] Results saved.
`

---

## Citation & Data Access

Please cite the Zenodo dataset archive:
- **Zenodo DOI:** [10.5281/zenodo.21826600](https://doi.org/10.5281/zenodo.21826600)

---

## License
Distributed under the **MIT License**.
