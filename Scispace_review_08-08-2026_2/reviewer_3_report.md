# Reviewer 3 Report — Clarity, Positioning & Broader Impact Specialist
## Manuscript: "The MANCO Exergetic Framework: Bridging Molecular Biodegradation and Thermodynamic Reservoir Abandonment in Heavy Oils"
**Target Journal:** Fuel (Elsevier) | **Reviewer Expertise:** Petroleum geochemistry, reservoir geochemistry, scientific writing, research ethics, broader energy-sector impact assessment

---

## Summary

This manuscript by a single author from Universidad Central de Venezuela presents the MANCO Exergetic Framework (MANCO-EX), which aims to bridge the gap between molecular-scale biodegradation characterization (MANCO scale) and thermodynamic reservoir abandonment criteria for heavy oils. The framework converts molecular biomarker depletion into a Specific Exergy Loss Index (ΔXd, kJ/mol) and validates it using a Linear Mixed-Effects Model on 41 multi-basin samples. The paper tackles a relevant and practical problem in the context of global heavy oil production challenges, particularly for the Orinoco Belt and Athabasca Oil Sands. While the framing is ambitious and the problem statement is compelling, the manuscript has significant shortcomings in its positioning relative to the existing literature, its structural compliance with *Fuel* journal standards, and its broader impact discussion.

---

## Soundness: 2 / 5

The soundness is limited by the disconnect between the paper's ambitious claims (a "universal" framework) and the narrow empirical basis supporting them (N = 41 samples, single author, no independent replication). The theoretical framework, while creative, contains unresolved derivation gaps identified by thermodynamic scrutiny.

---

## Presentation: 3 / 5

The manuscript is written in generally clear English with a logical narrative arc. However, it has several structural and formatting issues that must be addressed for *Fuel* compliance. The abstract is at the upper limit of acceptable length and contains several undefined acronyms (PM, GC-MS, REML, ICC, MAE) that reduce accessibility for the full breadth of the *Fuel* readership (which spans petroleum engineering, combustion science, and energy policy). The introduction is well-structured with appropriate subsections (1.1, 1.2) but the related work positioning is incomplete.

---

## Contribution: 3 / 5

The contribution is original in concept but insufficiently validated to be considered a major advance. The framework represents a promising research direction that, with broader validation and more rigorous derivation, could become a significant contribution to the field.

---

## Strengths

1. **Compelling problem framing**: The introduction effectively motivates the problem — the disconnect between molecular geochemical data and thermodynamic reservoir simulators is a real and consequential gap in the heavy oil production workflow. The paper correctly identifies this as a barrier to optimal field development decision-making.

2. **Relevance to *Fuel* readership**: The paper sits squarely within the scope of *Fuel* (Elsevier), bridging petroleum geochemistry, thermodynamics, and reservoir engineering. The topic — heavy oil biodegradation and its thermodynamic consequences — is timely given global energy transition pressures on unconventional resource development.

3. **Clear practical motivation**: The Thermodynamic Inutility Boundary concept (ΔXd_crit = 8.50 kJ/mol) provides a concrete, communicable engineering deliverable that is accessible to reservoir engineers and field operators who may not be familiar with molecular geochemistry.

4. **Geographic diversity of validation basins**: The inclusion of Orinoco (Venezuela), Athabasca (Canada), Junggar (China), and Bongor (Chad/Niger) basins demonstrates awareness of the global scope of heavy oil production and provides geographic diversity in the validation set.

5. **The MANCO scale citation is accurate**: The paper correctly cites Larter et al. (2012, *Organic Geochemistry*) as the source of the MANCO scale and positions MANCO-EX as an extension of this established framework. The positioning relative to the Peters & Moldowan (1993) PM scale is also accurate and well-argued.

6. **The Orinoco Belt context is well-described**: The author's institutional affiliation (Universidad Central de Venezuela) and clear familiarity with Venezuelan heavy oil geochemistry lend credibility to the Orinoco Basin component of the validation.

---

## Weaknesses

### W1 — Critical: Related Work Section is Incomplete and Misses Key Competitors

The manuscript's literature review (Section 1) fails to cite or engage with several directly relevant and recent works:

- **Zhong et al. (2025)** — *Scientific Reports* — "Establishing the relationship between heavy oil viscosity and molecular markers using an enhanced neural network model." This is the most direct methodological competitor, published in 2025, and its absence from the reference list suggests either a literature gap or selective citation. The paper must compare MANCO-EX against this approach.
- **McCaffrey et al. (1996)** — *AAPG Bulletin* — "Using Biomarkers to Improve Heavy Oil Reservoir Management." This is a seminal work on biomarker-based reservoir management that predates MANCO-EX and should be acknowledged.
- **Macías-Salinas et al. (2009)** — *Energy & Fuels* — Eyring-theory-based model for crude oil viscosity at reservoir conditions. Directly relevant to the Eyring component of MANCO-EX and not cited.
- **Miadonye et al. (2024)** — *International Journal of Chemistry* — Activation energy for viscous flow in heavy oil-diluent systems. Relevant Eyring application.

The absence of these works creates a misleading impression that MANCO-EX operates in a vacuum of prior art on biomarker-viscosity modelling and Eyring-based petroleum viscosity prediction.

### W2 — Critical: Abstract Does Not Comply with *Fuel* Standards

The abstract contains several issues relative to *Fuel* author guidelines:
- It uses undefined acronyms: "PM 1-10," "GC-MS," "REML," "ICC," "MAE," "OWC" (the last in the body). *Fuel* requires all acronyms to be defined at first use.
- The abstract reports R²_conditional > 0.99 without reporting R²_marginal = 0.18, creating a misleading impression of model performance. Both should be reported or neither.
- The abstract states "critical exergy threshold (ΔXd_crit = 8.50 kJ/mol)" without providing context for what this number means to a reader unfamiliar with the framework.
- The abstract is borderline in length (~200 words) and would benefit from trimming the methodological detail to make room for a clearer statement of the key finding and its significance.

### W3 — Serious: Single-Author Study Without Independent Replication

The manuscript is authored by a single researcher from a single institution. For a paper claiming to establish a "universal" thermodynamic framework applicable to global heavy oil reserves, the absence of co-authors with complementary expertise (e.g., a thermodynamicist, a statistician, an independent geochemist from a different basin) is a significant limitation. This is not a disqualifying issue in itself, but it means the manuscript has not benefited from internal peer review across disciplines, which is reflected in the thermodynamic and statistical gaps identified by Reviewers 1 and 2. The single-author nature also raises questions about the independence of the validation data — were the N = 41 multi-basin samples analyzed by the author or compiled from published literature? If the latter, the validation is essentially a literature-data exercise, not an independent experimental validation.

### W4 — Serious: Broader Impact Discussion is Absent

*Fuel* (Elsevier) and most major energy journals now expect a discussion of the broader societal, environmental, and economic implications of the research. The manuscript does not address:
- **Environmental implications**: Biodegraded heavy oil production is associated with high GHG emissions intensity (steam injection for SAGD in Athabasca, diluent use in Orinoco). Does the MANCO-EX framework have implications for emissions accounting or carbon intensity assessment?
- **Economic implications**: The Thermodynamic Inutility Boundary could have significant economic consequences for field development decisions. The relationship between ΔXd_crit and economic break-even ($/barrel) should be discussed.
- **Geopolitical implications**: The framework is directly relevant to Venezuelan (Orinoco) and Canadian (Athabasca) national resource strategies. This context deserves acknowledgment.
- **Ethical considerations**: The use of USGS public datasets should be acknowledged with appropriate data availability statements.

### W5 — Serious: Figures and Tables Are Inadequately Described

The manuscript references figures and tables but the captions and descriptions in the text are insufficient to evaluate them independently. Specifically:
- The scatter plot of ln(viscosity) vs. ΔXd should show: data points color-coded by basin, the LMM fixed-effect regression line with 95% confidence interval, and individual basin regression lines to illustrate the ICC = 0.99 structure. It is unclear from the text whether this information is presented.
- The biomarker cascade diagram should show: the PM degradation level at which each tier activates, the specific biomarker compounds in each tier, and the mapping to ΔXd. The text description is insufficient.
- No table comparing MANCO-EX performance metrics (RMSE, MAE, R²) against Beggs-Robinson and Egbogah-Ng on the same test set is provided.

### W6 — Moderate: The Term "Universal" is Overused and Unjustified

The manuscript uses the term "universal" or implies universality for the exergy-viscosity coupling in multiple places. With N = 41 samples from 4 basins, no claim of universality is scientifically defensible. The authors should replace "universal" with "multi-basin" or "geographically diverse" throughout, and explicitly acknowledge the limitations of the current validation scope.

### W7 — Moderate: No Code or Data Availability Statement

The manuscript does not include a data availability statement or code availability statement. *Fuel* (Elsevier) requires these. The USGS datasets used are publicly available and should be cited with their specific URLs and access dates. If the MANCO-EX calculation code is not publicly available, this should be stated.

### W8 — Moderate: The "Stodola (1910)" Citation is Incorrect

Reference [22] cites "Stodola, A. (1910). Steam and gas turbines. McGraw-Hill" as the source for the Gouy-Stodola theorem. The correct attribution is to both Gouy (1889) and Stodola (1910). More importantly, the modern formulation of the Gouy-Stodola theorem used in exergy analysis is typically attributed to Bejan (1982) or Dincer & Rosen (2021), both of which should be cited. The historical attribution to Stodola alone is incomplete and potentially misleading.

### W9 — Minor: Inconsistent Symbol Notation

The symbol for the Specific Exergy Loss Index appears variously as "ΔXd," "4Xd," "ΔXzit," and "ΔXd_crit" throughout the manuscript (some of these appear to be OCR artifacts from the PDF conversion). A consistent, properly typeset notation must be used throughout. The subscript notation should be standardized in LaTeX/Word before resubmission.

---

## Suggestions

1. **Expand the related work section** to include Zhong et al. (2025), McCaffrey et al. (1996), Macías-Salinas et al. (2009), and Miadonye et al. (2024). Explicitly compare and contrast MANCO-EX with these approaches.
2. **Revise the abstract**: Define all acronyms, report both R²_marginal and R²_conditional, and trim methodological detail to make room for a clearer impact statement.
3. **Add a Broader Impact section** discussing environmental, economic, and geopolitical implications of the framework.
4. **Add a Data and Code Availability statement** with specific URLs for the USGS datasets.
5. **Replace "universal" with appropriately qualified language** throughout the manuscript.
6. **Improve figure quality and captions**: Ensure the viscosity-ΔXd scatter plot shows basin-coded data, confidence intervals, and individual basin lines. Provide a performance comparison table.
7. **Correct the Gouy-Stodola attribution** to include Gouy (1889) and Bejan (1982).
8. **Fix all symbol notation inconsistencies** (ΔXd must be consistent throughout).
9. **Seek co-authorship or at minimum formal acknowledgment** from a thermodynamicist and a statistician who reviewed the derivations and statistical analysis. This is not a formal requirement but would substantially strengthen the manuscript's credibility.

---

## Questions

1. Were the N = 41 validation samples physically analyzed by the author, or were they compiled from published literature? If the latter, which publications were the data sources?
2. Is the MANCO-EX calculation code available for public access? If so, where?
3. What is the intended workflow for a reservoir engineer to apply MANCO-EX in practice? Is a software tool or spreadsheet implementation available?
4. How does MANCO-EX perform on lacustrine-sourced oils (e.g., Bohai Bay, China) where the biomarker assemblage differs fundamentally from marine-sourced oils?
5. Does the Thermodynamic Inutility Boundary (ΔXd_crit = 8.50 kJ/mol) vary with reservoir depth, temperature, and production method (SAGD vs. CSS vs. cold production)? If so, how?
6. How does the framework handle oils that have undergone both biodegradation and thermal maturation (i.e., where high maturity partly masks biodegradation signals in the biomarker record)?

---

## Rating: 4 / 10 — Major Revision Required

The paper presents a creative and practically relevant framework for a genuinely important problem in heavy oil reservoir management. However, it falls short of *Fuel* publication standards in its related work positioning (missing key competitors), its abstract compliance, the absence of a broader impact discussion, and inadequate figure/table presentation. The single-author, single-institution nature of the study, combined with the small validation dataset, limits the credibility of the "universal framework" claim. Major revision addressing the positioning gaps, presentation issues, and validation limitations is required.

---

## Confidence: High
The reviewer has broad expertise in petroleum geochemistry, reservoir geochemistry, and scientific writing for energy journals, with particular familiarity with the Orinoco Belt and Athabasca heavy oil systems.
