# Reviewer 1 Report — Methods & Theory Specialist
## Manuscript: "The MANCO Exergetic Framework: Bridging Molecular Biodegradation and Thermodynamic Reservoir Abandonment in Heavy Oils"
**Target Journal:** Fuel (Elsevier) | **Reviewer Expertise:** Non-equilibrium thermodynamics, petroleum physical chemistry, statistical mechanics, applied mathematics

---

## Summary

This manuscript proposes the MANCO Exergetic Framework (MANCO-EX), which seeks to convert the molecular MANCO biodegradation metric (µg/g oil) into a Specific Exergy Loss Index (ΔXd, kJ/mol) by coupling the Gouy-Stodola theorem for entropy generation with Eyring transition-state theory for viscous flow activation. The framework is calibrated on USGS datasets (1,585 physicochemical samples; 311 GC-MS runs) and validated against N = 41 multi-basin samples. A REML-estimated Linear Mixed-Effects Model (LMM) with basin-specific random intercepts yields R²_conditional > 0.99 and a fixed-effect slope β = 3.42 (p < 10⁻⁶). A critical exergy threshold ΔXd_crit = 8.50 kJ/mol is proposed as the Thermodynamic Inutility Boundary. The paper addresses a genuine gap at the intersection of petroleum geochemistry and thermodynamics, but several foundational derivations require rigorous scrutiny.

---

## Soundness: 2 / 5

The conceptual ambition is high, but multiple critical derivation steps are either incompletely presented, internally inconsistent, or rely on unjustified assumptions that undermine the claimed thermodynamic rigor.

---

## Presentation: 3 / 5

The manuscript is generally readable and logically structured, though the mathematical notation is inconsistent (ΔXd vs. ΔXzit vs. 4Xd appear to be the same symbol rendered differently due to OCR artifacts — this must be corrected). The abstract exceeds the spirit of conciseness for *Fuel* (it is borderline at ~200 words but is dense with undefined acronyms). Equations are presented without adequate derivation pathways.

---

## Contribution: 3 / 5

The integrative concept is novel (confirmed by literature search — no prior work couples Gouy-Stodola entropy generation with molecular biomarker depletion for reservoir abandonment prediction). However, the individual components (Eyring viscosity modelling, biomarker-viscosity correlations, LMM for geochemical data) each have substantial prior art. The contribution is primarily synthetic/integrative.

---

## Strengths

1. **Genuine conceptual novelty**: The conversion of molecular biomarker depletion into a thermodynamically grounded exergy loss metric via the Gouy-Stodola theorem is not documented in prior literature. This is a creative and potentially impactful synthesis.

2. **Physically motivated framework**: The choice of Eyring transition-state theory to link molecular composition changes (from biodegradation) to macroscopic viscosity is physically motivated and consistent with the established literature on Eyring-based viscosity models for crude oils (Macías-Salinas et al., 2009, *Energy & Fuels*; Andrade & Rajagopal, 2018, *Energy & Fuels*).

3. **Addressing a known scale limitation**: The multi-tiered biomarker cascade (methylphenanthrenes → triaromatic steroids → asphaltenic polar anchor) explicitly addresses the well-documented failure of the PM scale above PM 6, which is a recognized and important limitation in the field (Larter et al., 2012, *Organic Geochemistry*).

4. **Practical actionability**: The Thermodynamic Inutility Boundary (ΔXd_crit = 8.50 kJ/mol) is a directly actionable engineering criterion, translating a molecular measurement into a field-level go/no-go decision.

5. **Multi-basin validation attempt**: The use of four geologically distinct basins (Orinoco, Athabasca, Junggar, Bongor) for validation demonstrates awareness of the need for geographic generalizability.

---

## Weaknesses

### W1 — Critical: Gouy-Stodola Derivation is Incomplete and Potentially Circular

The Gouy-Stodola theorem states that exergy destruction equals T₀ × Ṡ_gen (where T₀ is the dead-state temperature and Ṡ_gen is the rate of entropy generation). To apply this to biodegradation, the manuscript must rigorously define: (a) the thermodynamic system boundary (is it the oil molecule? the reservoir volume? the oil-water contact zone?), (b) the dead state (T₀, P₀) and its justification for a subsurface reservoir, (c) the entropy generation mechanism (chemical reaction entropy? mixing entropy? metabolic heat dissipation?), and (d) the time scale over which Ṡ_gen is computed. None of these are clearly defined in the manuscript. The derivation appears to assume that the exergy of the aliphatic fraction equals the standard chemical exergy of the depleted molecules, which conflates thermochemical exergy with the Gouy-Stodola irreversibility of the biodegradation reaction. This is a fundamental error in thermodynamic accounting that must be corrected.

### W2 — Critical: Eyring Theory Application Lacks Rigorous Justification

The Eyring viscosity equation is: η = (hN_A/V) × exp(ΔG‡/RT), where ΔG‡ is the activation Gibbs free energy for viscous flow. The manuscript maps biomarker depletion onto ΔG‡, but does not provide: (a) the explicit functional form of ΔG‡ as a function of MANCO biomarker concentrations, (b) justification for treating the multi-component biodegraded oil as a system where a single effective ΔG‡ is meaningful, (c) validation that the Eyring model (rather than, e.g., WLF, Vogel-Fulcher-Tammann, or free-volume models) is appropriate for the viscosity range 10³–10⁶ cP encountered in heavy oils. For viscosities above ~10⁴ cP, simple Arrhenius/Eyring models frequently break down and free-volume models are preferred.

### W3 — Critical: LMM Statistical Interpretation is Fundamentally Flawed

The reported metrics — R²_marginal = 0.18, R²_conditional > 0.99, ICC = 0.99 — are internally consistent in a mathematical sense (Nakagawa & Schielzeth, 2013), but the interpretation offered is scientifically untenable as a validation of the exergy-viscosity coupling:

- **R²_marginal = 0.18** means the fixed effect (ΔXd) explains only 18% of total variance. This is a *weak* fixed-effect relationship.
- **ICC = 0.99** means 99% of the total variance is attributable to between-basin differences (random intercepts), not to the exergy predictor.
- The claim that "the fixed-effect slope is highly significant (p < 10⁻⁶), confirming the universal exergy-viscosity coupling" is a misinterpretation. Statistical significance in a mixed model does not confirm universality when 99% of variance is explained by the random structure. The model is effectively fitting basin-level means, not a universal exergy law.
- The paper does not report whether the fixed-effect slope β = 3.42 is consistent across basins (i.e., whether random slopes were tested). If the slope varies significantly between basins, the claim of universality collapses.

### W4 — Serious: VIF = 21.86 is Not Adequately Addressed

The manuscript acknowledges VIF values up to 21.86 among biomarker tiers, which substantially exceeds the commonly accepted threshold of 10 (and the conservative threshold of 5). The justification offered (citing O'Brien, 2007) — that high VIF is acceptable when predictors are not the inferential targets — is not applicable here because the biomarker concentrations are the primary inputs to the ΔXd calculation. High multicollinearity means that the individual biomarker contributions to ΔXd are statistically unreliable, and small perturbations in biomarker measurements could produce large swings in ΔXd. No sensitivity analysis or ridge regression is applied to address this.

### W5 — Serious: The ΔXd_crit = 8.50 kJ/mol Threshold Lacks Rigorous Derivation

The critical threshold is presented as a key deliverable but its derivation is not transparent. Specifically: (a) What is the assumed lifting energy (in kJ/mol equivalent) used to define E_net = 0? (b) Is this lifting energy a fixed constant or a function of reservoir depth, fluid column height, pump efficiency? (c) How sensitive is ΔXd_crit to the assumed lifting energy? A ±20% change in assumed lifting cost could shift the threshold substantially. (d) The uncertainty interval on ΔXd_crit is not reported. With N = 41 samples, the uncertainty on a threshold derived from a regression model could be substantial.

### W6 — Moderate: Dead-State Temperature and Pressure Selection

The Gouy-Stodola theorem requires a well-defined dead state (T₀, P₀). For a subsurface petroleum reservoir, the choice of dead state is non-trivial. Using standard atmospheric conditions (25°C, 1 atm) is conventional in chemical exergy analysis but ignores the pressure exergy component, which can be significant at reservoir depths of 1,000–3,000 m. The manuscript does not discuss this choice or its implications.

### W7 — Moderate: No Uncertainty Propagation

The conversion chain from GC-MS peak areas → MANCO concentrations → ΔXd involves multiple steps, each with measurement uncertainty. No uncertainty propagation (e.g., Monte Carlo simulation or analytical error propagation) is presented. The reported MAE < 0.01 ln cP appears unrealistically precise given the measurement chain.

### W8 — Missing Citation: Key Eyring Viscosity Literature Not Cited

Macías-Salinas et al. (2009, *Energy & Fuels*, DOI: 10.1021/EF8003015) — "Eyring-Theory-Based Model To Estimate Crude Oil Viscosity at Reservoir Conditions" — is directly relevant to the Eyring component and is not cited. This is a significant omission that must be corrected.

---

## Suggestions

1. **Provide a complete, step-by-step derivation** of ΔXd from first principles: define the system boundary, dead state, entropy generation mechanism, and show all intermediate steps from Gouy-Stodola to the final ΔXd formula. Consider a supplementary appendix.
2. **Justify the Eyring model choice** for the viscosity range 10³–10⁶ cP. Compare with WLF or free-volume models. Show that the Eyring activation energy is physically consistent with known activation energies for heavy oil viscous flow.
3. **Re-interpret the LMM results** honestly: acknowledge that R²_marginal = 0.18 represents a moderate fixed-effect relationship, not a universal law. Test random slopes. Report whether β is consistent across basins.
4. **Address multicollinearity** with ridge regression or LASSO, or at minimum provide a sensitivity analysis showing how ΔXd changes when individual biomarker tiers are excluded.
5. **Provide a full uncertainty budget** for ΔXd_crit = 8.50 kJ/mol, including confidence intervals derived from the regression and sensitivity to assumed lifting energy.
6. **Cite Macías-Salinas et al. (2009)** and other relevant Eyring viscosity literature.
7. **Define the dead state** explicitly and discuss the pressure exergy component.

---

## Questions

1. What is the explicit algebraic formula for ΔXd as a function of biomarker concentrations? Please show the complete derivation from the Gouy-Stodola theorem to the final expression, including all intermediate thermodynamic assumptions.
2. How was the dead-state temperature T₀ chosen? Is it the surface temperature, the reservoir temperature, or 25°C? How sensitive is ΔXd to this choice?
3. Were random slopes tested in the LMM? If so, did the slope β = 3.42 vary significantly across basins? If not, why not?
4. What is the 95% confidence interval on ΔXd_crit = 8.50 kJ/mol?
5. What is the assumed lifting energy (kJ/mol equivalent) used to define the Thermodynamic Inutility Boundary, and how was it estimated?
6. Why is the Eyring model preferred over free-volume or WLF models for oils with viscosity > 10⁴ cP?
7. How was the chemical exergy of the depleted biomarker fractions calculated? Were standard chemical exergy tables (e.g., Szargut et al.) used, or were values estimated from thermochemical data?

---

## Rating: 4 / 10 — Major Revision Required

The conceptual contribution is genuine and the paper addresses an important problem. However, the thermodynamic derivations are insufficiently rigorous, the statistical interpretation of the LMM is misleading, and the key quantitative claim (ΔXd_crit = 8.50 kJ/mol) lacks adequate uncertainty quantification. The paper cannot be accepted in its current form. Major revision addressing the thermodynamic derivation rigor (W1–W3, W6), multicollinearity (W4), and uncertainty quantification (W5, W7) is required before the framework can be considered validated.

---

## Confidence: High
The reviewer has extensive expertise in non-equilibrium thermodynamics, Eyring theory applications, and mixed-effects modelling in geoscience contexts.
