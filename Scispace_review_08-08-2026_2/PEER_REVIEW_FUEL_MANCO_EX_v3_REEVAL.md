# RE-EVALUATION PEER REVIEW — Fuel (Elsevier, IF ~7.0)
## Revised Manuscript v3.0: "The MANCO Exergetic Framework: Bridging Molecular Biodegradation and Thermodynamic Reservoir Abandonment in Heavy Oils"
**Author:** Jose A. Garcia, Universidad Central de Venezuela  
**Re-Evaluation Basis:** Three-panel specialist consensus (Non-equilibrium Thermodynamics; Reservoir Engineering / PVT; Petroleum Geochemistry / Scientific Writing)  
**Previous Decision (v2):** Major Revision — Overall 4/10  
**Date of Re-Evaluation:** 2026-08-08  

---
---

## UPDATED EXECUTIVE ASSESSMENT & EDITORIAL DECISION

| Criterion | v2 Score | v3 Score | Δ |
|---|:---:|:---:|:---:|
| Thermodynamic & Statistical Soundness | 2 / 5 | 3.5 / 5 | +1.5 |
| Presentation & Fuel Compliance | 3 / 5 | 4.0 / 5 | +1.0 |
| Scientific Contribution & Novelty | 3 / 5 | 4.0 / 5 | +1.0 |
| **Overall Consensus** | **4 / 10** | **7.0 / 10** | **+3.0** |

> ### DECISION: MINOR REVISION
>
> This is a substantively upgraded manuscript. The authors have directly addressed all three Priority-1 disqualifying issues identified in the v2 review: the Gouy-Stodola derivation is now complete and reproducible; the USGS Bemidji dataset provenance is explicitly clarified; and the LMM statistical narrative has been corrected. The v3 manuscript meets the threshold for consideration for publication in *Fuel* subject to the minor but non-trivial corrections listed in Section 4. The revised manuscript is recommended for **Minor Revision** rather than acceptance only due to four residual issues: (1) the Random Slopes logical inconsistency, (2) abstract non-compliance (211 words, missing R²_marginal, one typo), (3) unresolved VIF = 21.86, and (4) absence of direct numerical benchmarking against Zhong et al. (2025). These can be addressed without re-running experiments.

---
---

## SECTION 1 — COMPARISON: PREVIOUS vs. CURRENT MANUSCRIPT STRENGTHS

### 1.1 — Issues Fully and Satisfactorily Resolved

| v2 Critical Issue | v3 Status | Evidence |
|---|:---:|---|
| **Gouy-Stodola derivation incomplete/unreproducible** | ✅ RESOLVED | Control volume Ω_res at OWC defined; dead state T₀=298.15 K, P₀=1.013 bar explicitly stated; pressure exergy ex,P ≈ 0.02 kJ/mol shown to be negligible (3 orders of magnitude below ΔXd); algebraic pathway from GC-MS peak areas → Φ_cascade (Eq.12) → ΔXd (Eq.11) is now step-by-step reproducible |
| **USGS Bemidji dataset inappropriate for reservoir calibration** | ✅ RESOLVED | Explicitly declared: "utilized exclusively for calibrating the stoichiometric organic acid generation kinetics (α weighting coefficient in Tier 1)" and "not used for deep reservoir viscosity calibration" |
| **LMM R²_conditional-only reporting (misleading)** | ✅ RESOLVED | R²_marginal = 0.18 now reported in the main body alongside R²_conditional > 0.99 with correct interpretation: "marginal R² = 0.18 reflects the modest explanatory power of the fixed-effect slope alone" |
| **Gouy-Stodola theorem attribution incomplete** | ✅ RESOLVED | Now cites Gouy (1889) [40], Stodola (1910) [22], and Bejan (1982) [41] collectively |
| **Missing key citations** | ✅ RESOLVED | All 11 missing references now present: Macías-Salinas (2009) [35], Zhong (2025) [36], McCaffrey (1996) [37], Miadonye (2024) [38], De Ghetto (1995) [39], Gouy (1889) [40], Bejan (1982) [41], Szargut (1988) [42], Eyring (1936) [43], Andrade & Rajagopal (2018) [44], Hu (2014) [45] |
| **No GC-MS analytical conditions** | ✅ RESOLVED | Full protocol reported: Agilent 6890N/5975C MSD, HP-5MS column (30m × 0.25mm × 0.25μm), He 1.0 mL/min, 70 eV EI, SIM mode, temperature program (50°C → 4°C/min → 310°C), d₁₀-phenanthrene internal standard |
| **No viscometry measurement protocol** | ✅ RESOLVED | Haake RheoStress 600 rotational cone-and-plate, gap 0.105 mm, shear rate 0.1–100 s⁻¹, T = 313.15 K (40°C), atmospheric dead-oil conditions |
| **No Data/Code Availability statement** | ✅ RESOLVED | Section 6.2: GitHub repo (manco-ex-sota) + Zenodo archive (DOI: 10.5281/zenodo.21826600) + USGS open-access links |
| **No Broader Impact section** | ✅ RESOLVED | Section 6.1 addresses: GHG/SOR reduction (SAGD, Orinoco diluent blending), NPV/$/bbl break-even integration, Venezuelan/Canadian national resource strategy context |
| **Eyring model unjustified for heavy oil viscosity range** | ✅ RESOLVED | Now justified for 10³–10⁵ cP range with citations to Macías-Salinas (2009), Andrade & Rajagopal (2018), and Miadonye & Amadu (2024); pi-pi stacking of asphaltenic nano-aggregates identified as the viscous flow barrier mechanism |
| **No uncertainty on ΔXd_crit** | ✅ RESOLVED | Monte Carlo B=10,000 iterations: ΔXd_crit = 8.50 ± 0.78 kJ/mol, 95% CI [6.09, 9.20] |
| **No cascade ablation study** | ✅ RESOLVED | Table 4 provides full tier-by-tier MAE breakdown confirming Full Cascade MAE = 0.0082 ln cP (vs. 0.0299–0.0447 for single-tier configurations) |

---

### 1.2 — Substantive New Additions That Strengthen the Manuscript

| New Addition | Scientific Value |
|---|---|
| **Random Slopes LRT** (LRT = 449.05, p = 3.09 × 10⁻⁹⁸, ΔAIC = 445.05) | Formally tests and reports basin-level slope heterogeneity — a direct response to the v2 reviewer demand |
| **Monte Carlo global slope β̄_LMM = 3.05 ± 0.32, 95% CI [2.45, 3.70]** | Honest quantification of slope variability across basins; the shift from β=3.42 (random-intercept) to β=3.05 (MC mean) reflects the proper treatment of between-basin coupling heterogeneity |
| **Pressure exergy derivation** (ex,P ≈ 0.02 kJ/mol vs. ΔXd = 5.40–10.68 kJ/mol) | Definitively justifies the use of standard atmospheric dead state for subsurface reservoir application |
| **Full entropy generation accounting** (Eq. 2: ΔXd = T₀[ΔSmix + (ΔHrxn − ΔGrxn)/Tres]) | Resolves the previously flagged potential conflation between thermochemical exergy and Gouy-Stodola irreversibility — both mixing and reaction entropy components are now explicit |
| **Reservoir sample depth specification** (z_f = 800–2,500 m) | Directly addresses the concern that Bemidji conditions ≠ reservoir conditions |
| **Cascade Ablation Study (Table 4)** | Demonstrates incremental benefit of each biomarker tier; justifies the four-tier architecture quantitatively |

---
---

## SECTION 2 — REMAINING GAPS & REVIEWER OBJECTIONS (Minor Revision Items)

---

### GAP 1 [MODERATE — Must Address] — The Random Slopes LRT Creates a Logical Inconsistency in the Final Model Choice

**What the data say:** The LRT for random slopes yields LRT = 449.05, p = 3.09 × 10⁻⁹⁸, ΔAIC = −445.05. This is an extraordinarily significant result — the data overwhelmingly favor a random-slope over a random-intercept model. This confirms that the exergy-viscosity slope β varies significantly across basins.

**The contradiction:** Despite this result, the manuscript reports that "a random-intercept-only specification was utilized, and random slopes were excluded" for the final predictive model. The authors cannot simultaneously: (a) report a p-value of 10⁻⁹⁸ favoring random slopes, and (b) use a random-intercept model as the final framework without a rigorous justification.

**What this means scientifically:** The LRT result does not just confirm slope heterogeneity — it constitutes statistical evidence that the exergy-viscosity coupling constant is **not the same across basins**, undermining the key claim that β represents a universal physical constant. The global mean slope β̄ = 3.05 ± 0.32 (from Monte Carlo) with a 95% CI of [2.45, 3.70] spans a range of ±20%, which is large enough to be operationally significant for ΔXd_crit calculations.

**Required revision:** The authors must either: (a) adopt the random-slope model as the primary model and report basin-specific slopes with uncertainty, or (b) retain the random-intercept model and explicitly acknowledge that slope heterogeneity limits the universal applicability of β, with a clear explanation of why parsimony justifies the simpler model choice (e.g., Bayesian information criterion comparison, interpretability trade-off). This cannot be glossed over — it defines the scope of validity of the Thermodynamic Inutility Boundary.

---

### GAP 2 [MODERATE — Must Address] — Abstract Non-Compliance Persists on Three Counts

**Count A — Word count exceeds Fuel limit:** The abstract contains **211 words**, exceeding the *Fuel* guideline of ≤200 words. The following sentence can be trimmed without loss of critical information: "A multi-tiered biomarker cascade (methylphenanthrene isomers, triaromatic steroids, asphaltenic polar anchor) maintains diagnostic capability across all Peters & Moldowan (PM) degradation levels (PM 1–10)" — the mention of the three tiers is sufficient without "PM 1–10" being repeated.

**Count B — R²_marginal = 0.18 is absent from the abstract:** The abstract reports R²_conditional > 0.99 and ICC = 0.99 but does not include R²_marginal = 0.18. Given that the v2 review specifically identified selective reporting of these metrics as a critical flaw, their absence from the abstract remains an issue of transparency. The abstract should include: "...with R²_marginal = 0.18 (fixed effect) and R²_conditional > 0.99 (full model including basin random effects)..."

**Count C — Typographical error:** The abstract reads "Specific **Exergey** Loss Index" — this must be corrected to "Specific **Exergy** Loss Index." A typographical error in the abstract of a revised manuscript signals inadequate proofreading.

---

### GAP 3 [MODERATE — Should Address] — VIF = 21.86 Remains Unaddressed by Ridge Regression

The manuscript applies Tikhonov regularization (λ = 0.01) only for the specific case of lithology-specific recalibration of the weighting vector **w** when the predictor matrix **X** is ill-conditioned. It does **not** apply ridge regression to the main LMM model where VIF values up to 21.86 are reported among the four biomarker tier predictors.

The manuscript's position — citing O'Brien (2007) to argue that high VIF is acceptable when predictors are not inferential targets — remains problematic here because biomarker concentrations are the **primary inputs** to the ΔXd calculation. The consequence is that the individual α, β, γ, δ weights in Eq. 12 (Φ_cascade) are estimated with inflated standard errors, and small perturbations in any single biomarker tier measurement could produce non-trivial shifts in ΔXd.

**Minimum required revision:** Provide a sensitivity analysis showing how ΔXd_crit shifts when each biomarker tier is perturbed by ±1 measurement standard deviation. If the threshold remains within its Monte Carlo CI [6.09, 9.20] under such perturbations, the VIF concern is operationally mitigated. This analysis can be added as a supplementary table.

---

### GAP 4 [MODERATE — Should Address] — Direct Numerical Comparison Against Zhong et al. (2025) Is Missing

Zhong et al. (2025, *Scientific Reports*, DOI: 10.1038/s41598-025-18561-2) is now cited, but only contextually ("recent computational efforts that have attempted to bridge biomarker data with heavy oil viscosity using machine learning and artificial neural networks"). No numerical benchmarking is performed.

For a paper claiming superior framework performance, a one-paragraph comparison is expected, reporting the equivalent error metrics (R², MAE in ln cP) of the Zhong et al. neural network on a comparable dataset. Even a qualitative discussion explaining why an LMM-thermodynamic framework is preferable to a neural network approach in engineering practice (interpretability, physical grounding, small-sample reliability) would constitute adequate engagement.

---

### GAP 5 [MINOR — Recommended] — "Universal" Language Persists in Body Text

The v2 review explicitly required replacement of "universal" with qualified language such as "multi-basin" or "physically grounded." The term appears at least twice in the v3 body text ("universal physical convergence" and "universal thermodynamic coupling"). Given that the LRT result (Gap 1) confirms significant slope heterogeneity across basins, any remaining use of "universal" to describe the coupling is statistically unjustified and should be replaced.

---

### GAP 6 [MINOR — Recommended] — Dead Oil vs. Live Oil Scope Limitation Requires Explicit Acknowledgment

All validation viscosity measurements are at atmospheric dead-oil conditions (40°C, 1 atm), while the practical application target is deep reservoir conditions (P_res = 80–250 bar, T_res = 30–80°C). The framework's explicit scope is dead-oil viscosity prediction, but this limitation is not stated in the abstract or the conclusions. A one-sentence scope statement is required: e.g., "The current validation covers dead-oil viscosity at atmospheric conditions; extension to in-situ live oil requires gas solubility corrections and remains a direction for future work."

---

### GAP 7 [MINOR — Recommended] — Benchmarking Metrics Are Insufficient (R² and MAE Only)

The benchmarking against Beggs-Robinson (R² = −2.25, MAE = 2.08 ln cP) and Egbogah-Ng (R² = −2.70, MAE = 2.25 ln cP) demonstrates qualitative failure of API/T-only models clearly. However, RMSE, AAD%, and MAPE are not reported, and no statistical significance test (Diebold-Mariano or Wilcoxon signed-rank) is applied to the performance difference. Adding RMSE to Table 3 (one additional row) would bring the benchmarking to *Fuel* standards.

---
---

## SECTION 3 — DIMENSION-BY-DIMENSION RE-EVALUATION SCORECARD

---

### DIMENSION 1: METHODOLOGICAL & STATISTICAL RIGOR

| Item | v2 Status | v3 Status | Assessment |
|---|:---:|:---:|---|
| R²_marginal and R²_conditional both reported in body | ❌ | ✅ | Corrected; both reported with correct interpretation |
| R²_marginal reported in abstract | ❌ | ❌ | **Still missing** — must add |
| Random slopes formally tested (LRT) | ❌ | ✅ | LRT = 449.05, p = 3.09×10⁻⁹⁸, ΔAIC = 445.05 — fully reported |
| Random slope result consistent with final model | N/A | ⚠️ | **Logical inconsistency**: LRT overwhelmingly favors random slopes yet final model is random-intercept-only |
| ICC interpreted as basin-level progenitor variance | ❌ | ✅ | Correctly reframed |
| Monte Carlo uncertainty on ΔXd_crit | ❌ | ✅ | B=10,000, 8.50 ± 0.78 kJ/mol, 95% CI [6.09, 9.20] |
| Global slope β̄ with CI | ❌ | ✅ | β̄ = 3.05 ± 0.32, CI [2.45, 3.70] |
| Cascade Ablation Study | ❌ | ✅ | Table 4; Full cascade MAE = 0.0082 vs. 0.0299–0.0447 single-tier |
| Multicollinearity addressed (ridge regression) | ❌ | ⚠️ | VIF max = 21.86 unchanged; Tikhonov regularization applied only for recalibration, not for the main model |
| "Universal" language qualified | ❌ | ⚠️ | Still present: "universal physical convergence," "universal thermodynamic coupling" |

**Dimension 1 Score: 3.5 / 5** (from 2.0/5 in v2)

---

### DIMENSION 2: THERMODYNAMIC DERIVATION & PHYSICAL CLARITY

| Item | v2 Status | v3 Status | Assessment |
|---|:---:|:---:|---|
| Control volume defined | ❌ | ✅ | Ω_res at OWC explicitly defined |
| Dead state T₀, P₀ specified | ❌ | ✅ | T₀=298.15 K, P₀=1.013 bar with Szargut species |
| Pressure exergy component derived | ❌ | ✅ | ex,P ≈ 0.02 kJ/mol — shown negligible vs. ΔXd |
| Algebraic pathway biomarkers → ΔXd | ❌ | ✅ | Eq. 12 (Φ_cascade) → Eq. 11 (ΔXd) step-by-step |
| Entropy generation mechanisms identified | ❌ | ✅ | ΔSmix (configurational) + (ΔHrxn−ΔGrxn)/Tres (chemical) |
| Gouy (1889) + Stodola (1910) + Bejan (1982) cited | ❌ | ✅ | All three cited collectively [40][22][41] |
| Eyring justified for 10³–10⁵ cP range | ❌ | ✅ | Citations to Macías-Salinas (2009), Andrade & Rajagopal (2018), Miadonye (2024) |
| Potential thermochemical/Gouy-Stodola conflation | ⚠️ | ✅ | Resolved: Eq. 2 explicitly separates mixing entropy from reaction entropy within the Gouy-Stodola framework |

**Dimension 2 Score: 4.5 / 5** (from 2.0/5 in v2) — the most dramatically improved dimension

---

### DIMENSION 3: DATASET PROVENANCE & EXPERIMENTAL PROTOCOLS

| Item | v2 Status | v3 Status | Assessment |
|---|:---:|:---:|---|
| Bemidji dataset scope clarified (kinetics only) | ❌ | ✅ | Explicitly "exclusively for organic acid kinetics" |
| N=41 sample depth/T/P specified | ❌ | ✅ | z_f = 800–2,500 m, T_res = 313.15 K dead oil |
| GC-MS protocol complete | ❌ | ✅ | Fully specified (column, carrier, program, ionization, IS) |
| Viscometry protocol complete | ❌ | ✅ | Haake RheoStress 600, cone-and-plate, 40°C atmospheric |
| Data/Code availability statement | ❌ | ✅ | GitHub + Zenodo + USGS links |
| Broader Impact section | ❌ | ✅ | SOR/GHG, $/bbl NPV, national resource strategy context |
| Dead oil vs. live oil scope explicitly stated | ❌ | ⚠️ | Mentioned in passing; not stated in abstract or conclusions |

**Dimension 3 Score: 4.5 / 5** (from 1.5/5 in v2)

---

### DIMENSION 4: LITERATURE POSITIONING & COMPETITOR BENCHMARKING

| Item | v2 Status | v3 Status | Assessment |
|---|:---:|:---:|---|
| Macías-Salinas (2009) cited and engaged | ❌ | ✅ | Cited in Eyring section with mechanistic justification |
| Zhong et al. (2025) cited | ❌ | ✅ | Cited contextually; no direct numerical benchmarking |
| McCaffrey (1996) cited | ❌ | ✅ | Cited contextually |
| Miadonye (2024) cited | ❌ | ✅ | Cited in Eyring activation energy context |
| Hu et al. (2014) cited | ❌ | ✅ | Cited alongside Zhong (2025) |
| De Ghetto (1995) cited | ❌ | ✅ | Cited as PVT baseline reference |
| Beggs-Robinson benchmarking with error metrics | ⚠️ | ✅ | R²=−2.25, MAE=2.08 ln cP on same test set |
| Egbogah-Ng benchmarking with error metrics | ⚠️ | ✅ | R²=−2.70, MAE=2.25 ln cP on same test set |
| RMSE, AAD%, MAPE reported | ❌ | ❌ | **Still missing** — only R² and MAE |
| Diebold-Mariano or equivalent significance test | ❌ | ❌ | **Still missing** |
| Direct numerical benchmarking vs. Zhong (2025) | ❌ | ❌ | **Still missing** |

**Dimension 4 Score: 3.5 / 5** (from 2.0/5 in v2)

---

### DIMENSION 5: ELSEVIER / FUEL GUIDELINE COMPLIANCE

| Item | v2 Status | v3 Status | Assessment |
|---|:---:|:---:|---|
| Abstract ≤ 200 words | ⚠️ | ❌ | **211 words** — exceeds guideline by 11 words |
| Acronyms defined in abstract (PM, GC-MS, REML, ICC, MAE) | ❌ | ✅ | All defined; MANCO, MANCO-EX, LMM, ΔXd also defined |
| OWC defined at first use | ❌ | ⚠️ | Not in abstract; first defined in body (page 2) — acceptable |
| R²_marginal in abstract | ❌ | ❌ | **Still absent from abstract** |
| Typo in abstract ("Exergey") | N/A | ❌ | **New typo** — must correct |
| Broader Impact section present | ❌ | ✅ | Section 6.1 — comprehensive |
| Data & Code Availability | ❌ | ✅ | Section 6.2 — GitHub + Zenodo |
| "Universal" replaced with qualified language | ❌ | ⚠️ | Two residual instances in body |
| Symbol ΔXd notation consistent | ⚠️ | ✅ | Appears resolved in main body |
| Logical structure for petroleum engineering audience | ✅ | ✅ | Well-structured: geochemistry → thermodynamics → validation → case study → workflow |

**Dimension 5 Score: 3.5 / 5** (from 2.5/5 in v2)

---
---

## SECTION 4 — FINAL REVISED RATING & MANDATORY REVISION CHECKLIST

### Mandatory Revisions (Minor — No New Experiments Required)

| Priority | Action | Dimension |
|---|---|---|
| **M1** | Resolve the Random Slopes logical inconsistency: either adopt the random-slope model as the primary model and report basin-specific β_i values, OR retain the random-intercept model with an explicit methodological justification (BIC comparison, interpretability argument) and acknowledge in the Discussion that slope heterogeneity limits universality claims. | D1 |
| **M2** | Trim the abstract to ≤ 200 words AND add R²_marginal = 0.18 in the same sentence as R²_conditional > 0.99. Suggested text: "...achieves R²_marginal = 0.18 (fixed-effect ΔXd predictor) and R²_conditional > 0.99 (full model with basin random effects), with MAE < 0.01 ln cP." | D5 |
| **M3** | Correct the typo "Exergey" to "Exergy" in the abstract. | D5 |
| **M4** | Add a VIF sensitivity analysis as a supplementary table: perturb each biomarker tier input by ±1 SD and report the resulting shift in ΔXd_crit relative to the Monte Carlo CI [6.09, 9.20]. | D1 |
| **M5** | Add RMSE (in ln cP) to the benchmarking table (Table 3) alongside the existing R² and MAE metrics for Beggs-Robinson, Egbogah-Ng, and MANCO-EX. | D4 |
| **M6** | Replace all remaining instances of "universal physical convergence" and "universal thermodynamic coupling" with "multi-basin physically grounded coupling" or equivalent qualified language. | D5 |

### Strongly Recommended Revisions

| Priority | Action | Dimension |
|---|---|---|
| **R1** | Add a one-sentence scope statement in the abstract and conclusions: "The current validation covers dead-oil viscosity at atmospheric conditions (40°C); extension to live-oil in-situ conditions requires gas solubility corrections and constitutes a direction for future work." | D3 |
| **R2** | Add a brief paragraph in the Discussion comparing MANCO-EX and Zhong et al. (2025) — even a qualitative comparison of interpretability, physical grounding, and small-sample robustness vs. neural network approaches would constitute adequate engagement. | D4 |

---
---

## SUMMARY: SCORE PROGRESSION v2 → v3

| | v2 | v3 | Status |
|---|:---:|:---:|---|
| **Overall Rating** | **4.0 / 10** | **7.0 / 10** | ↑ +3.0 |
| **Editorial Decision** | Major Revision | **Minor Revision** | ↑ Upgraded |
| Priority-1 issues resolved | 0 / 4 | 4 / 4 | ✅ All resolved |
| Priority-2 issues resolved | 0 / 4 | 3 / 4 (RMSE, DM-test, Zhong comparison pending) | ✅ Mostly resolved |
| New issues introduced | — | 1 (typo "Exergey") | ⚠️ Minor |
| Abstract compliance | Non-compliant | Partially compliant (211 words, missing R²_marginal, typo) | ⚠️ Minor fix needed |
| Thermodynamic derivation reproducibility | Non-reproducible | Fully reproducible | ✅ |
| Dataset provenance clarity | Ambiguous | Unambiguous | ✅ |
| Random slopes formally tested | Not tested | Tested but model choice inconsistent with result | ⚠️ Needs clarification |

---

*This re-evaluation is based on full extraction of the v3.0 manuscript content across all 28 pages and comparison with v2 review artifacts. The revised manuscript represents a substantial, good-faith revision that addresses all disqualifying concerns. With the six mandatory minor corrections noted above, the manuscript would be suitable for acceptance in Fuel.*
