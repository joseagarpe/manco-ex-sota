# Reviewer 2 Report — Experiments & Practical Impact Specialist
## Manuscript: "The MANCO Exergetic Framework: Bridging Molecular Biodegradation and Thermodynamic Reservoir Abandonment in Heavy Oils"
**Target Journal:** Fuel (Elsevier) | **Reviewer Expertise:** Petroleum reservoir engineering, experimental PVT characterization, heavy oil production, geochemical field studies, applied statistics

---

## Summary

The manuscript introduces MANCO-EX, a thermodynamic framework converting molecular biomarker depletion (MANCO metric, µg/g oil) into a Specific Exergy Loss Index (ΔXd, kJ/mol) to predict viscosity and define a critical abandonment threshold (ΔXd_crit = 8.50 kJ/mol) in biodegraded heavy oil reservoirs. The calibration uses USGS Bemidji physicochemical data (1,585 samples) and USGS PGRL GC-MS data (311 runs), validated on N = 41 samples from four basins. The framework is benchmarked against Beggs-Robinson and Egbogah-Ng PVT correlations. While the engineering motivation is sound and the multi-basin scope is commendable, the experimental validation is severely underpowered, the dataset provenance is inadequately documented, and the benchmarking methodology contains critical flaws that prevent reliable assessment of the framework's practical utility.

---

## Soundness: 2 / 5

The experimental design has fundamental deficiencies: the validation sample size (N = 41) is too small for the claims made, the USGS Bemidji dataset is an aquifer contamination study not a petroleum reservoir dataset, and the benchmarking against PVT correlations is not conducted on a common test set with reported error metrics.

---

## Presentation: 3 / 5

The manuscript is reasonably well-written for a technical audience. However, key experimental details (sample preparation, GC-MS conditions, viscosity measurement protocol, temperature/pressure conditions for viscosity measurements) are absent. Tables summarizing dataset characteristics are inadequate. The figures (viscosity vs. ΔXd scatter plot, biomarker cascade diagram) are described but their quality and information density cannot be fully assessed from the text alone.

---

## Contribution: 3 / 5

The practical contribution — a GC-MS-to-abandonment-decision pipeline — is potentially valuable for heavy oil reservoir management. However, the validation is insufficient to support the claimed universal applicability across global heavy oil provinces.

---

## Strengths

1. **Addresses a real operational problem**: The inability to integrate molecular geochemical data (MANCO scale, GC-MS outputs) into reservoir simulators is a genuine and long-standing operational gap in heavy oil field management. The paper correctly identifies this as the target problem.

2. **Multi-basin scope**: The inclusion of four geologically distinct basins (Orinoco Belt, Athabasca, Junggar Basin, Bongor Basin) spanning different geological ages, source rock types, and biodegradation histories is the right approach for demonstrating generalizability.

3. **Benchmarking against industry-standard PVT correlations**: The comparison with Beggs-Robinson (1975) and Egbogah-Ng (1990) is appropriate and practically relevant. The demonstration that API/T-only models fail for biodegraded oils is consistent with the broader literature (De Ghetto et al., 1995; Pertuz-Parra et al., 2014) and provides useful context.

4. **Dual-dataset calibration**: Using both physicochemical (USGS Bemidji) and GC-MS (USGS PGRL) datasets for calibration shows methodological awareness of the need to separate chemical and physical property data streams.

5. **Practical threshold concept**: The Thermodynamic Inutility Boundary is a practically actionable concept that could be incorporated into field development decision frameworks if robustly validated.

---

## Weaknesses

### W1 — Critical: The USGS Bemidji Dataset is Fundamentally Inappropriate for Petroleum Reservoir Calibration

The USGS Bemidji Crude Oil Research Site is a well-documented aquifer contamination study site in Minnesota, USA, where crude oil was spilled from a pipeline into a shallow glacial aquifer in 1979. The 1,585 "physicochemical samples" are groundwater and sediment samples from a contaminated aquifer, not from petroleum reservoirs. The physicochemical conditions (near-surface, atmospheric pressure, groundwater chemistry, aerobic/anaerobic transition zones) are fundamentally different from those of deep petroleum reservoirs (high temperature, high pressure, saline formation water, confined geology). Using this dataset to calibrate a framework intended for deep reservoir application is a critical methodological error that must be explained and justified. If the Bemidji data were used only for biomarker degradation kinetics calibration (not for reservoir-condition viscosity), this must be stated explicitly and the limitation acknowledged.

### W2 — Critical: Validation Sample Size N = 41 is Severely Underpowered

The validation of a "universal" exergy-viscosity framework across four geologically distinct basins on only N = 41 samples is statistically insufficient. With 4 basins, this averages ~10 samples per basin — far too few to characterize the within-basin variability of biodegradation severity, progenitor fluid composition, reservoir temperature, and depth. For comparison, published biomarker-viscosity prediction models (e.g., Zhong et al., 2025, *Scientific Reports*) use substantially larger datasets with cross-validation. The high R²_conditional > 0.99 with N = 41 and ICC = 0.99 is consistent with the model fitting 4 basin-level means with minimal within-basin discrimination — not a meaningful validation of predictive power.

### W3 — Critical: No Cross-Validation or Hold-Out Test Set

The manuscript does not describe a train/validation/test split. With N = 41 total validation samples, it is unclear how many were used to fit the LMM parameters versus how many were held out for independent prediction testing. If all 41 samples were used in model fitting, the reported R²_conditional > 0.99 is an in-sample fit metric, not a predictive validation. Leave-one-out cross-validation (LOOCV) or k-fold cross-validation should be reported.

### W4 — Critical: Benchmarking Against Beggs-Robinson and Egbogah-Ng is Not Properly Conducted

The manuscript claims to demonstrate that MANCO-EX outperforms Beggs-Robinson and Egbogah-Ng, but does not report: (a) the specific error metrics (RMSE, MAE, MAPE, AAD%) for each model on the same test set, (b) whether the PVT correlations were applied at the actual measured reservoir temperature and pressure conditions of the validation samples, (c) whether the PVT correlations were applied to dead oil or live oil viscosity (Beggs-Robinson was developed for live oil systems), (d) statistical tests of significance for the performance difference. Without these details, the benchmarking claim cannot be evaluated. The literature shows that Beggs-Robinson can achieve AAD ≈ 9.6% for some datasets (Edreder & Rahuma, 2012) — it is not uniformly poor, and the comparison must be fair and dataset-specific.

### W5 — Serious: Viscosity Measurement Conditions Not Specified

The manuscript reports viscosity values for validation samples but does not specify: (a) whether viscosities are dead oil (atmospheric, stock tank) or live oil (reservoir conditions) measurements, (b) the temperature at which viscosity was measured, (c) the measurement method (rotational viscometer, capillary viscometer, falling sphere), (d) the uncertainty/repeatability of the measurements. For heavy oils where viscosity varies by orders of magnitude over a 20°C temperature range, this information is essential for evaluating the MAE < 0.01 ln cP claim.

### W6 — Serious: No Ablation Study on the Three-Tier Biomarker Cascade

The manuscript proposes a three-tier biomarker cascade but does not provide an ablation study showing: (a) the predictive performance of each tier individually, (b) whether all three tiers are necessary or whether one or two tiers suffice, (c) the degradation range (PM levels) over which each tier is active and how tier transitions are handled algorithmically. Without this, the practical implementation of the cascade is unclear.

### W7 — Serious: GC-MS Analytical Conditions Not Reported

The 311 GC-MS chromatographic runs (USGS PGRL) are described without specifying: column type, carrier gas, temperature program, injection volume, ionization mode (EI vs. CI), quantification method (internal standard, external standard, or peak area ratio), or detection limits. These are essential for reproducibility and for assessing whether the biomarker concentrations are comparable across samples from different basins analyzed at different times.

### W8 — Moderate: Potential Cherry-Picking of Validation Basins

The four validation basins (Orinoco, Athabasca, Junggar, Bongor) are all major, well-characterized heavy oil provinces with extensive published geochemical data. The framework has not been tested on less well-characterized basins or on oils with unusual source rock signatures (e.g., lacustrine, carbonate-sourced). This limits the claimed universality.

### W9 — Moderate: No Statistical Comparison with Zhong et al. (2025)

Zhong et al. (2025, *Scientific Reports*, DOI: 10.1038/s41598-025-18561-2) published a neural network model linking heavy oil viscosity to molecular markers using ridge regression for multicollinearity. This is a direct methodological competitor that is not cited or compared. The manuscript must benchmark against this work.

---

## Suggestions

1. **Clarify the role of the USGS Bemidji dataset**: If it was used only for kinetic calibration of biodegradation rates (not for reservoir viscosity calibration), state this explicitly and justify why near-surface aquifer biodegradation kinetics are transferable to deep reservoir conditions.
2. **Expand the validation dataset**: A minimum of N ≥ 100 samples across ≥ 6 basins is recommended for a "universal" framework claim. Consider incorporating published datasets from the Liaohe Basin (Hu et al., 2014) and Cymric Field (McCaffrey et al., 1996).
3. **Implement cross-validation**: Report LOOCV or k-fold (k = 5 or 10) cross-validation metrics, including RMSE, MAE, and R² on held-out data.
4. **Conduct a rigorous benchmarking study**: Apply Beggs-Robinson, Egbogah-Ng, and MANCO-EX to the same test set under identical conditions. Report AAD%, RMSE, and bias for each model. Include statistical significance tests.
5. **Report viscosity measurement conditions**: Specify temperature, pressure, measurement method, and uncertainty for all validation viscosity data.
6. **Provide an ablation study** for the three-tier biomarker cascade.
7. **Cite and compare with Zhong et al. (2025)** and other recent biomarker-viscosity ML models.
8. **Report GC-MS analytical conditions** in a methods table.

---

## Questions

1. What were the exact temperature and pressure conditions at which viscosity was measured for the N = 41 validation samples? Were these dead oil or live oil measurements?
2. How many of the 41 validation samples were used in model fitting versus held out for independent prediction testing?
3. Why was the USGS Bemidji aquifer contamination dataset selected for calibration? What is the justification for transferring near-surface biodegradation kinetics to deep petroleum reservoir conditions?
4. What are the error metrics (RMSE, MAE, AAD%) for Beggs-Robinson and Egbogah-Ng on the same validation set where MANCO-EX achieves MAE < 0.01 ln cP?
5. How are tier transitions handled in the biomarker cascade? Is there a defined PM level at which Tier 1 (methylphenanthrenes) is replaced by Tier 2 (triaromatic steroids)?
6. Were the GC-MS analyses of the four validation basins conducted in the same laboratory under identical conditions, or were they compiled from published literature? If the latter, how were inter-laboratory calibration differences handled?
7. What is the minimum sample volume required for GC-MS analysis within the MANCO-EX framework, and is this achievable from standard drill cuttings or sidewall cores?

---

## Rating: 4 / 10 — Major Revision Required

The paper addresses a genuinely important problem in heavy oil reservoir management and proposes a creative framework. However, the experimental validation is critically underpowered (N = 41, no cross-validation), the dataset provenance is questionable (USGS Bemidji), and the benchmarking is inadequately conducted. The practical utility of MANCO-EX cannot be assessed from the current evidence base. Major revision with substantially expanded validation, rigorous benchmarking, and complete experimental reporting is required.

---

## Confidence: High
The reviewer has extensive experience in heavy oil PVT characterization, reservoir geochemistry, and experimental design for petroleum engineering studies.
