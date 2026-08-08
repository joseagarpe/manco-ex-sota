## TL;DR

Heavy oil viscosity prediction has used empirical PVT correlations, regression and neural-network approaches, and compositional/biomarker‑informed ML that mitigates multicollinearity. The supplied literature contains no direct evaluation of linear mixed‑effects models vs Beggs‑Robinson or Egbogah for heavy oils, so a comparison is insufficient evidence.

----

## Methods used

Several statistical and modeling approaches have been applied to predict heavy or extra‑heavy oil viscosity from compositional or geochemical inputs. Empirical PVT correlations built on bulk properties (API gravity, temperature, gas content) remain common, while machine learning and regression adaptations have been used to handle nonlinearities and high‑dimensional compositional signals.

- **Empirical PVT correlations** — Beggs‑Robinson and modified temperature‑viscosity correlations (Egbogah & Ng and others) are widely used to estimate dead/saturated/undersaturated viscosities from API gravity and temperature data [1] [2] [3].  
- **Statistical regression and model adjustments** — Regression and parameter‑fitting approaches have been used to tailor or extend empirical formulas for extra‑heavy oils and specific basins, reducing average errors through dataset‑specific calibration [3] [4].  
- **Artificial neural networks and AI** — ANN models trained on PVT datasets have outperformed many conventional correlations in reported cases, providing more accurate viscosity estimates when richer input sets are available [5].  
- **Compositional and biomarker ML with regularization** — Combining L2‑regularized (ridge) feature selection to mitigate multicollinearity with feedforward neural networks allowed high‑accuracy mapping from molecular marker signatures (biomarkers) to viscosity in biodegraded heavy oils [6].

----

## Model comparisons

Direct, in‑corpus quantitative comparisons between linear mixed‑effects models and specific PVT correlations for heavy oil viscosity are not available in the supplied literature, so assessment of comparative performance is insufficient evidence. The literature does, however, allow comparisons between empirical correlations and machine learning / calibrated regression approaches.

- **Empirical correlations characteristics**  
  - **Beggs‑Robinson** is an empirical, API/temperature‑based correlation frequently used for dead and reservoir viscosities and often reported as a baseline comparator in regional studies [1] [7].  
  - **Egbogah & Ng** provide a modified temperature‑viscosity correlation intended to improve on Beggs‑Robinson for some conditions [2].  
- **Reported accuracy and variability**  
  - **Variable error levels**: Beggs‑Robinson produced low absolute average deviation (AAD ≈ 9.6%) for one Libyan dataset in a reported evaluation [7], while other regional evaluations have reported larger AADs (≈21%) for Beggs‑Robinson on different sample sets [8]. These results illustrate that empirical correlation performance is dataset‑dependent [7] [8].  
- **Machine learning and calibrated regression advantages**  
  - **ANN and AI** models trained on sufficient PVT data have shown systematic accuracy improvements compared with several empirical correlations in the cited studies [5].  
  - **Biomarker‑driven ML** that pairs ridge regression (to control multicollinearity) with a feedforward neural network produced substantially better predictive fits for biodegraded heavy oils in the supplied study, indicating compositional signals can add predictive power beyond bulk properties [6].  
- **Practical implication**  
  - Empirical correlations remain useful as engineering defaults but their accuracy varies with oil type and API class; ML and calibrated regressions can reduce errors when richer compositional or laboratory datasets are available [3] [5] [6].

----

## API gravity limitations for biodegraded oils

API‑gravity‑only or bulk‑property models have recognized limitations when applied to biodegraded or compositionally heterogeneous heavy oils; the supplied literature highlights these constraints and reasons why compositional or biomarker information can be necessary.

- **Composition changes not captured**  
  - **Bulk metrics omit molecular detail** — Biodegradation alters molecular composition (e.g., biomarker distributions) in ways that API gravity does not capture, which can decouple viscosity from API alone and reduce predictive accuracy [6].  
- **Heterogeneity and nonlinearity**  
  - **Large within‑class variability** — Heavy and extra‑heavy oils show heterogeneous viscosity behavior within the same API range, prompting bespoke correlations or adjustments for extra‑heavy oils [3] [4].  
- **Multicollinearity and high‑dimensional signals**  
  - **Geochemical predictors are multicollinear** — High‑dimensional biomarker datasets exhibit multicollinearity that must be managed (e.g., ridge regularization) before using nonlinear models, a requirement not addressed by API‑only formulas [6].  
- **Empirical error examples**  
  - **Dataset dependence** — Evaluations report substantial and variable AADs for API‑based correlations across regions and oil types, indicating limited generalizability for biodegraded/heavy oils without recalibration [7] [8] [3].  
- **What the supplied studies recommend**  
  - **Use compositional inputs when available** — Studies that integrate biomarker/compositional data with regularized regression and neural networks obtain much better fits for biodegraded heavy oils than bulk‑property correlations alone [6] [5].