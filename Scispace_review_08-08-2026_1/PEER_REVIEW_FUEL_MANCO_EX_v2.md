# PEER REVIEW AUDIT — FUEL (Elsevier, IF ~7.0)
## Manuscript: "The MANCO Exergetic Framework: Bridging Molecular Biodegradation and Thermodynamic Reservoir Abandonment in Heavy Oils"
**Author:** Jose A. Garcia, Universidad Central de Venezuela  
**Reviewer Panel:** 3 independent specialists — Non-equilibrium Thermodynamics & Applied Mathematics; Petroleum Reservoir Engineering & PVT Characterization; Petroleum Geochemistry & Scientific Writing  
**Date of Review:** 2026-08-08  

---

---

## EXECUTIVE ASSESSMENT & RECOMMENDATION

| Criterion | Rating | Score |
|---|---|---|
| Thermodynamic & Statistical Soundness | 2 / 5 | |
| Presentation & Clarity | 3 / 5 | |
| Scientific Contribution & Novelty | 3 / 5 | |
| **Overall Consensus** | **4 / 10** | |

> **DECISION: MAJOR REVISION**  
> All three independent reviewers independently assigned 4/10 with a recommendation of Major Revision. The manuscript is **not suitable for publication in its current form**. It presents a genuinely novel concept with legitimate practical relevance, but is undermined by an incomplete thermodynamic derivation, a misleading statistical narrative, a critically underpowered validation dataset, and a questionable calibration data source. The framework requires substantial technical and evidential strengthening before it can be considered for acceptance.

---

---

## SECTION 1 — KEY STRENGTHS

### S1. Genuine Conceptual Novelty (Confirmed by Literature Search)
No prior published work formally converts molecular biomarker depletion into a Specific Exergy Loss Index (ΔXd, kJ/mol) via the Gouy-Stodola theorem coupled with Eyring transition-state theory for reservoir abandonment prediction. This integrative synthesis is original. The literature search across SciSpace, Google Scholar, and ArXiv confirms no prior replication of this specific formulation.

### S2. Addresses a Real and Consequential Operational Gap
The inability to integrate GC-MS molecular geochemical data (MANCO scale) into thermodynamic reservoir simulators is a genuine, long-standing barrier in heavy oil field management — particularly for operators in the Orinoco Belt and Athabasca Oil Sands. The paper correctly identifies and targets this gap.

### S3. Physically Motivated Theoretical Backbone
The choice of Eyring transition-state theory to bridge molecular composition changes (biomarker depletion) to macroscopic viscosity changes is physically grounded and consistent with the established literature on Eyring-based crude oil viscosity models. The Gouy-Stodola formulation for irreversibility is the correct thermodynamic tool if applied correctly.

### S4. Practically Actionable Deliverable — Thermodynamic Inutility Boundary
The critical threshold ΔXd_crit = 8.50 kJ/mol as a field-level go/no-go abandonment criterion is the paper's most impactful contribution — translating molecular geochemistry into an engineering decision metric. The concept is original and directly applicable to field development economics if robustly derived.

### S5. Multi-Tier Biomarker Cascade Addresses Known PM-Scale Limitation
The three-tier design (methylphenanthrenes → triaromatic steroids → asphaltenic polar anchor) explicitly addresses the well-documented failure of the Peters & Moldowan scale above PM 6. Maintaining diagnostic coverage across PM 1–10 is a useful engineering contribution.

### S6. Multi-Basin Validation Scope
The inclusion of four geologically distinct basins (Orinoco Belt, Athabasca, Junggar, Bongor) spanning different geological ages, source rock types, and biodegradation histories is the correct approach for demonstrating geographic generalizability — even if the sample counts within each basin are currently insufficient.

---

---

## SECTION 2 — CRITICAL VULNERABILITIES / REVIEWER OBJECTIONS

---

### DIMENSION 1: METHODOLOGICAL & STATISTICAL RIGOR

#### C1.1 [CRITICAL] — The LMM Metrics Contradict the Paper's Central Claim
The reported statistics are internally consistent but their interpretation is scientifically untenable as proof of a "universal exergy-viscosity coupling":

- **R²_marginal = 0.18** means the fixed-effect predictor (ΔXd) explains only **18% of total variance in ln(viscosity)**. This is a *weak* fixed-effect relationship.
- **ICC = 0.99** means **99% of variance is attributable to between-basin random intercepts** — i.e., which basin a sample comes from dominates viscosity almost entirely. This is not a new finding; progenitor fluid composition differences between basins are already well-established in petroleum geochemistry.
- The abstract reports R²_conditional > 0.99 **without equally prominently reporting R²_marginal = 0.18**. This selective reporting creates a misleading impression of predictive power.
- The statistically significant fixed slope β = 3.42 (p < 10⁻⁶) is an artefact of the LMM's power to detect weak fixed effects in the presence of strong random structure — **it does not confirm universality**.
- **Random slopes were not reported**: if the slope β varies significantly across basins, the claim of a single universal coupling constant collapses entirely.

**The model is effectively fitting four basin-level means with a weak within-basin gradient — not demonstrating a universal thermodynamic law.**

#### C1.2 [CRITICAL] — VIF = 21.86 is Scientifically Indefensible in This Context
The manuscript acknowledges VIF values up to 21.86 among biomarker tiers and cites O'Brien (2007) to justify this. This justification does not hold:

- O'Brien's argument applies when predictors are **not the inferential targets** and only the overall model fit is of interest. Here, the biomarker concentrations are the **primary inputs to the ΔXd calculation**, so their individual reliability matters directly.
- VIF > 21.86 means the standard error of individual biomarker coefficients is inflated by a factor of > 4.7 (√21.86). Small perturbations in biomarker measurements produce large, unstable swings in ΔXd.
- No ridge regression, LASSO, or sensitivity analysis is presented to assess the impact of this collinearity on ΔXd estimates.

#### C1.3 [SERIOUS] — No Cross-Validation or Hold-Out Test Set
The manuscript does not describe a train/validation/test partition. With N = 41 total samples, it is unclear how many were used to fit model parameters versus reserved for independent prediction testing. If all 41 samples were used in model fitting, R²_conditional > 0.99 is an **in-sample** fit metric — not a predictive validation.

---

### DIMENSION 2: THERMODYNAMIC & PHYSICAL COUPLING

#### C2.1 [CRITICAL] — Gouy-Stodola Derivation is Incomplete and Potentially Contains a Fundamental Error
The Gouy-Stodola theorem (Ẋ_destroyed = T₀ × Ṡ_gen) requires rigorous specification of:

1. **System boundary**: Is it the oil molecule? The reservoir volume element? The oil-water contact zone?
2. **Dead state (T₀, P₀)**: For a subsurface reservoir (1,000–3,000 m depth), using standard atmospheric dead state (25°C, 1 atm) ignores the **pressure exergy component**, which is non-negligible at reservoir pressures.
3. **Entropy generation mechanism**: Is this chemical reaction entropy, mixing entropy, or metabolic heat dissipation from microbial activity? These have different magnitudes and functional forms.
4. **Time scale of Ṡ_gen**: Biodegradation occurs over geological timescales; the Gouy-Stodola formulation is typically applied to quasi-steady engineering processes. The temporal mapping is undefined.

> **Potential fundamental error identified by Reviewer 1 (thermodynamics specialist)**: The derivation appears to **conflate thermochemical exergy** (chemical exergy of depleted molecular species) with **Gouy-Stodola irreversibility** (entropy generation rate multiplied by dead-state temperature). These are not equivalent. Standard chemical exergy of aliphatic fractions (calculated from Szargut tables) is a state function of molecular composition; Gouy-Stodola irreversibility is a process quantity dependent on the path of the reaction. Equating them is a fundamental thermodynamic accounting error.

A manuscript whose central thermodynamic derivation cannot be independently reproduced from the information provided does not meet minimum scientific publication standards, regardless of conceptual merit.

#### C2.2 [SERIOUS] — Eyring Model Not Justified for Viscosity Range 10³–10⁶ cP
The Eyring viscosity equation (η = (hN_A/V) × exp(ΔG‡/RT)) is physically motivated for molecular flow processes. However:

- For heavy oils with viscosity > 10⁴ cP, **simple Arrhenius/Eyring models frequently break down**; free-volume models (Doolittle, WLF) or Vogel-Fulcher-Tammann equations are typically preferred.
- The **explicit functional form of ΔG‡ as a function of MANCO biomarker concentrations** is not provided.
- The justification for treating a multi-component, highly heterogeneous biodegraded oil as a system with a single effective activation energy ΔG‡ is not presented.
- The key Eyring viscosity paper (Macías-Salinas et al., 2009, *Energy & Fuels*, DOI: 10.1021/EF8003015) is **not cited**.

#### C2.3 [SERIOUS] — ΔXd_crit = 8.50 kJ/mol Threshold is Not Transparently Derived
The critical threshold defining the Thermodynamic Inutility Boundary (E_net ≤ 0) is the paper's key practical deliverable, yet its derivation lacks transparency:

- What is the assumed **lifting energy** (kJ/mol equivalent) used to define E_net = 0? Is this a constant or a function of reservoir depth/pump efficiency?
- **No confidence interval is reported** for ΔXd_crit. With N = 41, the uncertainty on a regression-derived threshold could be ±1–2 kJ/mol, which would be operationally significant.
- A ±20% change in the assumed lifting cost could shift the threshold by a geologically meaningful amount.

---

### DIMENSION 3: BENCHMARKING & COMPARATIVE ANALYSIS

#### C3.1 [CRITICAL] — Benchmarking Against Beggs-Robinson and Egbogah-Ng is Not Properly Conducted
The manuscript claims MANCO-EX outperforms standard PVT correlations but fails to provide:

- **Error metrics (RMSE, MAE, AAD%, MAPE) for each model** on the same test set.
- Confirmation that PVT correlations were applied at the actual measured reservoir temperature and pressure of the validation samples.
- Clarification of **dead oil vs. live oil viscosity**: Beggs-Robinson was developed for live oil systems; applying it to dead oil measurements would artificially inflate its apparent error.
- Statistical significance tests for the performance difference.

> Beggs-Robinson achieves AAD ≈ 9.6% on some published datasets (Edreder & Rahuma, 2012) — it is not uniformly poor. The comparison must be conducted fairly on a common test set under identical conditions.

#### C3.2 [SERIOUS] — No Comparison with Zhong et al. (2025)
Zhong et al. (2025, *Scientific Reports*, DOI: 10.1038/s41598-025-18561-2) published a neural network model for heavy oil viscosity prediction from molecular markers using ridge regression to handle multicollinearity — a **direct methodological competitor** not cited or compared in the manuscript.

---

### DIMENSION 4: CLARITY, STRUCTURE & FUEL COMPLIANCE

#### C4.1 [SERIOUS] — Abstract is Non-Compliant with Fuel Standards
- Reports R²_conditional > 0.99 **without reporting R²_marginal = 0.18** — misleading.
- Contains undefined acronyms at first use: PM, GC-MS, REML, ICC, MAE — all must be defined in the abstract per *Fuel* author guidelines.
- Length is borderline (~200 words) with excessive methodological detail displacing the key finding and its significance.
- The term "universal" appears in the abstract without statistical justification.

#### C4.2 [SERIOUS] — Incomplete Related Work / Missing Key Citations
The literature review fails to engage with:

| Missing Citation | Relevance | Impact of Omission |
|---|---|---|
| Macías-Salinas et al., 2009, *Energy & Fuels* | Eyring-based crude oil viscosity model at reservoir conditions | Direct precedent for the Eyring component; creates impression of unwarranted novelty |
| Zhong et al., 2025, *Scientific Reports* | Neural network + ridge regression for biomarker-viscosity | Most direct methodological competitor; must be compared |
| McCaffrey et al., 1996, *AAPG Bulletin* | Biomarker-based reservoir management (Cymric Field) | Seminal precedent; absence is a significant gap |
| Miadonye et al., 2024, *Int. J. Chemistry* | Eyring activation energy for heavy oil-diluent viscosity | Directly relevant Eyring application |
| De Ghetto et al., 1995 | PVT correlations for heavy/extra-heavy oils | More comprehensive PVT baseline needed |

#### C4.3 [MODERATE] — Inconsistent Symbol Notation
The Specific Exergy Loss Index appears variously typeset as "ΔXd," "4Xd," "ΔXzit," and "ΔXd_crit" throughout the manuscript (partly OCR artefacts). A single consistent, properly typeset symbol must be used throughout.

#### C4.4 [MODERATE] — Gouy-Stodola Attribution is Incorrect
Reference [22] attributes the Gouy-Stodola theorem to "Stodola, A. (1910)" alone. The correct attribution requires: **Gouy (1889)** for the original formulation, Stodola (1910), and the modern exergy analysis formulation attributable to **Bejan (1982)** and/or **Dincer & Rosen (2021)**.

#### C4.5 [MODERATE] — No Broader Impact Discussion
*Fuel* and major energy journals expect discussion of: environmental implications (GHG intensity of SAGD/diluent-use production), economic implications (ΔXd_crit vs. economic break-even in $/barrel), geopolitical context (Venezuelan and Canadian national resource strategies), and a Data/Code Availability statement. All are absent.

---

### DIMENSION 5: TOP 3 RED FLAGS FOR A HUMAN REVIEWER

---

#### RED FLAG 1 — The LMM Statistics Tell the Opposite Story from What is Claimed

> **"If ICC = 0.99, your model is 99% explained by which basin the sample comes from, not by your exergy predictor. With R²_marginal = 0.18, you have a weak within-basin gradient. How does this constitute a 'universal exergy-viscosity coupling'? You have demonstrated that progenitor fluid composition (basin identity) governs viscosity — something petroleum geochemists have known for decades."**

This is the single most consequential objection. The manuscript's core statistical argument is **internally contradicted by its own reported numbers**. A skeptical reviewer will seize on this immediately and it will be the first thing flagged in formal review.

---

#### RED FLAG 2 — The Thermodynamic Derivation Cannot Be Reproduced

> **"Show me the complete step-by-step derivation of ΔXd from the Gouy-Stodola theorem. Define the system boundary. Define the dead state. Show how biomarker peak areas map to entropy generation rates. Show every algebraic step from Ẋ_destroyed = T₀Ṡ_gen to ΔXd in kJ/mol. Without this, your framework is a black box, not a thermodynamic derivation."**

A framework that cannot be independently reproduced from its published description does not meet the minimum bar for scientific publication regardless of conceptual appeal. Reviewer 1 additionally suspects a **fundamental thermodynamic accounting error** (conflation of thermochemical exergy with Gouy-Stodola irreversibility) that, if confirmed, would require complete reformulation.

---

#### RED FLAG 3 — The Calibration Dataset is Not from a Petroleum Reservoir

> **"The USGS Bemidji site is a shallow glacial aquifer contaminated by a 1979 pipeline spill — it is not a petroleum reservoir. Surface atmospheric pressure, groundwater chemistry, aerobic-anaerobic transition zones: none of these conditions resemble a deep (1,000–3,000 m) confined petroleum reservoir. On what basis do you transfer near-surface aquifer biodegradation kinetics to deep reservoir conditions? If you cannot justify this rigorously, your calibration must be redone with appropriate reservoir data."**

This is a potentially disqualifying issue. If the calibration is fundamentally inappropriate, the numerical value of ΔXd_crit = 8.50 kJ/mol — the paper's key deliverable — is unreliable.

---

---

## SECTION 3 — SPECIFIC RECOMMENDATIONS FOR AUTHORS

### Priority 1 — Essential for Re-consideration (Must address before manuscript can be re-reviewed)

| # | Recommendation |
|---|---|
| P1.1 | Provide a **complete step-by-step derivation of ΔXd** from the Gouy-Stodola theorem: define system boundary, dead state (T₀, P₀), entropy generation mechanism, time scale, and the algebraic pathway from GC-MS biomarker concentrations (µg/g) to ΔXd (kJ/mol). Provide as a mandatory Supplementary Appendix. Clarify whether standard chemical exergy (Szargut tables) or Gouy-Stodola irreversibility is the basis — and resolve the potential conflation between the two. |
| P1.2 | **Correct and fully contextualize the LMM statistical interpretation**: (a) Report R²_marginal = 0.18 and R²_conditional > 0.99 together with equal prominence everywhere they appear, including the abstract; (b) Test and report random slopes — if β varies significantly across basins, revise all universality claims accordingly; (c) Replace all instances of "universal" with "multi-basin" or appropriately qualified language; (d) Reframe the finding honestly: the ICC = 0.99 structure means the model reveals between-basin compositional differences, with ΔXd contributing an 18% within-basin gradient. |
| P1.3 | **Clarify the USGS Bemidji dataset role**: If used only for biodegradation kinetics calibration (not reservoir viscosity calibration), state this explicitly and provide a rigorous, quantified argument for why near-surface aquifer kinetics are transferable to deep reservoir conditions (temperature, pressure, microbial community, confinement). If used for viscosity calibration, replace with appropriate petroleum reservoir data and re-derive all dependent results including ΔXd_crit. |
| P1.4 | **Expand the validation dataset to N ≥ 100 samples across ≥ 6 basins**. Implement leave-one-out cross-validation (LOOCV) or k-fold (k=5 or k=10) cross-validation. Report out-of-sample RMSE, MAE, and R² on held-out data. Incorporate published datasets from Liaohe Basin (Hu et al., 2014) and Cymric Field (McCaffrey et al., 1996) to increase geographic and geological diversity. |

### Priority 2 — Required for Publication

| # | Recommendation |
|---|---|
| P2.1 | **Conduct and report rigorous benchmarking**: apply Beggs-Robinson, Egbogah-Ng, and MANCO-EX to the **same test set under identical conditions**. Report AAD%, RMSE, and bias for each. Include statistical significance tests (Diebold-Mariano or equivalent). Clarify whether dead oil or live oil viscosity is being predicted. |
| P2.2 | **Add all missing key citations** and revise the Related Work section: Macías-Salinas et al. (2009); Zhong et al. (2025); McCaffrey et al. (1996); Miadonye et al. (2024); De Ghetto et al. (1995). Explicitly compare MANCO-EX against Zhong et al. (2025) neural network approach. |
| P2.3 | **Address multicollinearity (VIF = 21.86)**: apply ridge regression or LASSO, or at minimum provide a sensitivity analysis showing how ΔXd changes when individual biomarker tiers are excluded one at a time. The O'Brien (2007) justification is not applicable here given that biomarker concentrations are the primary inferential inputs. |
| P2.4 | **Provide uncertainty quantification for ΔXd_crit = 8.50 kJ/mol**: report 95% confidence interval derived from the regression, Monte Carlo error propagation through the GC-MS → MANCO → ΔXd chain, and sensitivity analysis to assumed lifting energy (show the threshold range for ±20% variation in lifting cost). |
| P2.5 | **Provide complete experimental methods**: GC-MS conditions (column, temperature program, internal standard, ionization mode), viscosity measurement conditions (temperature, pressure, method, uncertainty), sample preparation, and inter-laboratory calibration protocol for multi-basin data compiled from literature sources. |
| P2.6 | **Justify the Eyring model for viscosity range 10³–10⁶ cP**: compare with WLF and free-volume models. Show that the assumed single effective ΔG‡ is physically meaningful for a heterogeneous multi-component oil. Provide the explicit functional form of ΔG‡ as a function of biomarker concentrations. |

### Priority 3 — Strongly Recommended

| # | Recommendation |
|---|---|
| P3.1 | Add a **Broader Impact section** discussing environmental (GHG intensity), economic (ΔXd_crit vs. $/barrel break-even), and geopolitical implications. |
| P3.2 | Add a **Data and Code Availability statement** with USGS dataset URLs and access dates. State whether the MANCO-EX calculation code is publicly available. |
| P3.3 | Fix all **symbol notation inconsistencies**: standardize ΔXd throughout in LaTeX/Word. |
| P3.4 | Correct the **Gouy-Stodola attribution** to include Gouy (1889) and Bejan (1982). |
| P3.5 | **Revise the abstract**: define all acronyms at first use, report both R² values, trim methodological detail, add a clearer impact statement. |
| P3.6 | **Provide an ablation study** for the three-tier biomarker cascade: performance of each tier individually, and how tier transitions at specific PM levels are handled algorithmically. |
| P3.7 | Consider seeking **co-authorship or formal acknowledgment** from an independent thermodynamicist and statistician who reviewed the derivations — this would substantially improve the manuscript's credibility for a "universal framework" claim. |

---

---

## APPENDIX: REVIEWER RATING SUMMARY

| Reviewer | Expertise | Soundness | Presentation | Contribution | Overall | Decision |
|---|---|---|---|---|---|---|
| Reviewer 1 | Non-equilibrium thermodynamics, Eyring theory, applied mathematics | 2/5 | 3/5 | 3/5 | 4/10 | Major Revision |
| Reviewer 2 | Reservoir engineering, PVT characterization, experimental design | 2/5 | 3/5 | 3/5 | 4/10 | Major Revision |
| Reviewer 3 | Petroleum geochemistry, scientific writing, energy-sector impact | 2/5 | 3/5 | 3/5 | 4/10 | Major Revision |
| **Meta-Reviewer Consensus** | | **2/5** | **3/5** | **3/5** | **4/10** | **Major Revision** |

---

*This peer review audit was conducted using three independent specialist reviewers and a systematic literature search. All claims regarding prior art gaps are based on searches conducted as part of the review process.*
