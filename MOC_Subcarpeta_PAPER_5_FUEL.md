# Map of Content (MOC) — PAPER_5_FUEL (MANCO-EX v3.1)

## 📌 Manuscrito Principal & PDF Compilado
- **LaTeX Source:** `fuel_manco_v2_manuscript.tex` (601 líneas, v3.1 final)
- **PDF Compilado:** `fuel_manco_v2_manuscript.pdf` (540.0 KB, 0 errores, 0 warnings)

## 🛠️ Motor SOTA & Suite de Diagnóstico Python
- `MANCO_EX_SOTA_Engine.py`: Motor de cálculo SOTA con REML MixedLM real, Beggs-Robinson real y Egbogah-Ng real.
- `run_real_lmm.py`: Ejecución de LMM con `statsmodels.MixedLM` (REML).
- `run_random_slopes_test.py`: Test LRT de pendientes aleatorias ($\text{LRT} = 449.05, p < 10^{-15}$).
- `run_cascade_ablation.py`: Estudio de ablación de los 4 Tiers ($\text{MAE} = 0.0082\text{ ln cP}$).
- `run_ridge_vif_analysis.py`: Regresión Ridge ($\lambda = 0.01$) y análisis de VIF ($VIF = 21.86$).
- `run_uncertainty_budget.py`: Propagación de incertidumbre Monte Carlo ($B=10{,}000$).
- `real_benchmarks.py`: Evaluación comparativa empírica de Beggs-Robinson y Egbogah-Ng.

## 📊 Tablas & Resultados JSON
- `real_lmm_results.json`: Parámetros REML LMM y BLUPs por cuenca.
- `random_slopes_results.json`: Estadísticos Likelihood Ratio Test.
- `ablation_results.json`: Matriz de ablación por Tiers.
- `ridge_vif_results.json`: Coeficientes Ridge y VIF.
- `uncertainty_budget_results.json`: Intervalos de confianza Monte Carlo ($95\%\text{ CI}$).
- `STATISTICAL_TABLES.md`: Tablas estadísticas consolidada v3.1.
- `LinkedIn SOTA.md`: Post oficial de divulgación técnica v3.1.

## 🔍 Informes de Peer Review (SciSpace)
- `Scispace_review_08-08-2026_1/`: Auditoría inicial (v2, 4.0/10 Major Revision).
- `Scispace_review_08-08-2026_2/`: Re-evaluación v3.0 (**7.0/10 Minor Revision**) y matriz v3.1 (**9.8/10 Accept**).