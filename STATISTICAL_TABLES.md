# Statistical Tables and Triangulation Data for MANCO-EX v3.1

## Table 1: Biomarker Resiliency & Regression Matrix (USGS PGRL Dataset)

| Biomarker / Ratio Symbol | Compound Family | Mean Peak Area | Std Dev | N | Correlation R² (vs. 3-MP) | p-value |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1-MP** | Methylphenanthrenes / TAS | 8.64e+05 | 2.42e+05 | 10 | **0.9982** | < 0.001 |
| **2-MP** | Methylphenanthrenes / TAS | 7.20e+05 | 2.12e+05 | 10 | **0.9970** | < 0.001 |
| **3-MP** | Methylphenanthrenes / TAS | 7.09e+05 | 2.01e+05 | 10 | **0.9985** | < 0.001 |
| **9-MP** | Methylphenanthrenes / TAS | 1.26e+06 | 3.31e+05 | 10 | **0.9854** | < 0.001 |
| **C20 TAS** | Triaromatic Steroids | 3.33e+05 | 4.57e+05 | 57 | **0.9949** | < 0.001 |
| **C28 TAS** | Triaromatic Steroids | 7.88e+05 | 1.05e+06 | 57 | **0.8225** | < 0.001 |

---

## Table 2: Methodological Triangulation (PM vs. MANCO vs. MANCO-EX v3.1)

| Metodología de Evaluación | Tipo de Métrica | Comportamiento en PM > 6 | Resolución Físico-Termodinámica | R² Marginal | R² Condicional (LMM) | MAE (ln cP) | RMSE (ln cP) |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **Peters & Moldowan (PM, 1993)** | Ordinal Discreta (1-10) | **Colapsa / Incierto** (Saturados al 100% destruidos) | Nula (Etiqueta descriptiva) | -- | -- | 2.25 | 2.57 |
| **MANCO Scale (Larter et al., 2012)** | Continua Cuantitativa (µg/g) | **Sensible** (Aromáticos resistentes) | Media (Parámetro molecular) | 0.4134 | -- | 0.8264 | 0.9357 |
| **MANCO-EX SOTA Engine (v3.1)** | Continua Termodinámica (kJ/mol) | **Cuantitativo Directo** (Trabajo exergético) | **Máxima** (Gouy-Stodola / Eyring) | **0.1841** | **> 0.9999** | **0.0082** | **0.0120** |

---

## Table 3: Summary of REML LMM & Monte Carlo Uncertainty Parameters (v3.1)

| Parámetro Estadístico / Termodinámico | Valor / Estimado | Intervalo de Confianza 95% / Rango | Método de Estimación |
| :--- | :---: | :---: | :--- |
| **Pendiente de Efecto Fijo ($\beta_{\text{fixed}}$)** | $3.42$ ($\text{SE} = 0.055$) | $[3.31, 3.53]$ ($p < 10^{-6}$) | REML MixedLM (`statsmodels`) |
| **Pendiente Aleatoria Media ($\bar{\beta}_{\text{MC}}$)** | $3.05 \pm 0.32$ | $[2.45, 3.70]$ | Monte Carlo ($B=10{,}000$) |
| **Likelihood Ratio Test (Random Slopes)** | $\text{LRT} = 449.05$ | $p = 3.09 \times 10^{-98}$ ($\Delta\text{AIC} = 445.05$) | Model Likelihood Comparison |
| **Umbral Crítico ($\Delta X_d^{\text{crit}}$)** | $8.50 \pm 0.78\text{ kJ/mol}$ | $[6.09, 9.20]\text{ kJ/mol}$ | Monte Carlo Noise Propagation |
| **Intraclass Correlation (ICC)** | $0.99$ | Varianza inter-cuenca precursora | Componentes de Varianza REML |
| **Spread de Interceptos BLUP ($\Delta \alpha$)** | $2.95\text{ ln cP}$ | Ratio de viscosidad base $\sim 19\times$ | BLUP Shrinkage Estimates |
