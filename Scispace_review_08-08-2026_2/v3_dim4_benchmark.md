## Benchmarking and Comparative Analysis of MANCO-EX

Based on the provided manuscript, the benchmarking and comparative analysis of the MANCO-EX framework against legacy models and literature are detailed below:

### 1. Error Metrics and Numerical Benchmarking Values
The performance of the Beggs-Robinson, Egbogah-Ng, and MANCO-EX models was evaluated on the same global multi-basin dataset ($N = 41$, $T_{\text{res}} = 313.15\text{ K}$) [1]. The reported error metrics are the coefficient of determination ($R^2$) and the Mean Absolute Error (MAE in $\ln\text{ cP}$) [1]:

*   **Beggs-Robinson (1975):** Reports $R^2 = -2.25$ and $\text{MAE} = 2.08\ln\text{ cP}$ [1]. These dead-oil correlations yield negative $R^2$ values, indicating catastrophic failure when applied to biodegraded heavy oils [2]. Their predicted viscosity ranges (122–3,452 cP) systematically underestimate measured viscosities (1,977–90,347 cP) by up to two orders of magnitude [3].
*   **Egbogah-Ng (1990):** Reports $R^2 = -2.70$ and $\text{MAE} = 2.25\ln\text{ cP}$ [1]. Similar to Beggs-Robinson, it fails catastrophically due to the lack of molecular degradation input [1] [2].
*   **MANCO-EX (REML LMM):** Reports $R^2 > 0.99$ and $\text{MAE} < 0.01\ln\text{ cP}$ [1]. This near-perfect conditional prediction confirms that combining the geochemical degradation gradient with basin-specific progenitor fluid calibration is essential [4].

No other error metrics (such as RMSE, AAD%, or MAPE) are reported in the text or tables for these models.

---

### 2. Statistical Significance Tests on Performance Differences
There is no mention of statistical significance tests (such as the Diebold-Mariano test) being applied specifically to compare the performance differences between the models.

---

### 3. Citation and Comparison of Zhong et al. (2025)
**Zhong et al. (2025)**  is cited in the introduction to acknowledge recent computational efforts that "have attempted to bridge biomarker data with heavy oil viscosity using machine learning and artificial neural networks" [5]. However, the manuscript does not perform a direct numerical benchmarking comparison against the model proposed by Zhong et al. (2025).

---

### 4. Citation and Discussion of McCaffrey et al. (1996)
**McCaffrey et al. (1996)**  is cited in the introduction, noting that researchers have attempted to bridge biomarker data with heavy oil viscosity "by using individual biomarker ratios for reservoir compartment management" [6]. It is not discussed in detail beyond this contextual citation.

---

### 5. Citation of Macías-Salinas et al. (2009) in the Eyring Section
Yes, **Macías-Salinas et al. (2009)**  is cited in the Eyring section. It is first introduced as a study where "physical chemistry researchers have applied Eyring transition-state theory to estimate reservoir-condition crude oil viscosities" [7]. In the Eyring derivation section, it is cited to justify applying "Eyring's transition-state rate theory for viscous flow" [8] and to support the physical validity of the theory at reservoir temperatures (30–80°C), where viscous dissipation is "governed by the thermal activation energy required for molecules to jump past structural obstacles created by pi-pi stacking of asphaltenic nano-aggregates" [9].

---

### 6. Citation of Miadonye & Amadu (2024)
Yes, **Miadonye & Amadu (2024)**  is cited. It is referenced in relation to estimating "viscous flow activation energy in heavy oil-diluent systems" [10] and to support the physical validity of Eyring transition-state theory regarding the thermal activation energy required to overcome structural obstacles from pi-pi stacking of asphaltenic nano-aggregates [9].

---

### 7. Citation of Hu et al. (2014)
Yes, **Hu et al. (2014)**  is cited alongside Zhong et al. (2025) to reference "recent computational efforts [that] have attempted to bridge biomarker data with heavy oil viscosity using machine learning and artificial neural networks" [5].

---

### 8. Citation of De Ghetto et al. (1995) for PVT Baselines
Yes, **De Ghetto et al. (1995)**  is cited as an example of standard empirical PVT correlations [11]. The text states that while these correlations "operate effectively on conventional light oils, they lack molecular composition input and fail catastrophically under advanced biodegradation" [11].