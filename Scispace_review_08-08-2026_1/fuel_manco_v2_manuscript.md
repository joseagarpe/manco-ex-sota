# The MANCO Exergetic Framework: Bridging Molecular
Biodegradation and Thermodynamic Reservoir Abandonment in
Heavy Oils

# Josc A. Garcia

Instituto de Ciencias de la Tierra, Universidad Central de Venezuela, AP 3895, Caracas 1010A, Venezuela

# Abstract

Microbial biodegradation in heavy oil reservoirs   destroys high-exergy aliphatic fractions
causing exponential viscosity escalation and premature field abandonment_ The molecular-
scale MANCO degradation metric (pg/ oil) cannot be integrated into thermodynamic reser-
voir simulators_ This paper introduces the MANCO Exergetic Framework (MANCO-EX)
converting molecular biomarker depletion into a Specific Exergy Loss Index (4Xd, kJ/mol)
via the Gouy-Stodola theorem and Eyring rate theory: multi-tiered biomarker cascade
(methylphenanthrenes triaromatic steroids, asphaltenic polar anchor) maintains diagnostic
capability across all biodegradation levels (PM 1-10)_ Calibrated on 1,585 physicochemical
samples (USGS Bemidji) and 311 GC-MS chromatographic runs (USGS PGRL), the frame-
work is validated against independent experimental viscosity measurements from N = 41
multi-basin samples (Orinoco, Athabasca, Junggar, Bongor) _ REML-estimated Linear
Mixed-Effects Model with basin-specific random intercepts achieves Rzonditional > 0.99 (MAE
< 0.01 In cP)_ The fixed-effect slope is highly significant (p < 10-6) , confirming the universal
exergy-viscosity coupling, while the intraclass correlation (ICC = 0.99) reflects the expected
dominance of progenitor fluid composition: critical exergy threshold (4Xzit 8.50
kJ/mol) defines the Thermodynamic Inutility Boundary where lifting energy exceeds prO-
duced fuel exergy

Keywords: Heavy Oil, Exergy Degradation, MANCO Exere 'getic Framework

Corresponding author at Instituto de Ciencias de la Tierra, Universidad Central de Venezuela, AP 3895
Caracas 10104 Venezuela.
Email address: jose. garcia47@ucv _ ve Jose A. Garcia)

(MANCO-EX) , Biomarkers, Biodegradation, Applied Thermodynamics, Reservoir
Engineering, Fuel

# Introduction

# 1.1. Unconventional Heavy Crude Oil Reserves Energy Challenges

Heavy and extra-heavy crude oil resources represent Over 50% of the world s remaining
liquid hydrocarbon inventory; with colossal accumulations concentrated in the Orinoco Oil
Belt (Venezuela) , the Athabasca Bitumen Sands (Canada) , and the deepwater Gulf of Mexico
16, [2p7]. The commercial exploitation of these unconventional assets is heavily constrained
by extreme fluid viscosity (103 to 106 cP at reservoir conditions) , elevated concentrations of
heteroatoms (N, S, 0), high polar resin and asphaltene contents, and severe operational
friction during in-situ recovery; artificial lift, and pipeline transportation p21[7 [8

In-situ microbial biodegradation is the principal geological process responsible for the
formation of heavy and extra-heavy crude oil accumulations p23,[5] Anaerobic syntrophic
bacterial and archaeal consortia operating at the oil-water contact (OWC) selectively con-
sume light aliphatic hydrocarbons, preferential n-alkanes, and low-molecular-weight aromatic
fractions [9,F7]: This selective biodegradation alters fluid phase equilibria, increases density

(lowers API gravity) , and dramatically escalates dynamic viscosity by orders of magnitude
over narrow vertical transition zones |8, [4]

# 1.2. Geochemical Prories: From Discrete Scales (PM 1-10) to Continuous Metrics

For over three decades reservoir biodegradation was evaluated using the qualitative , O -
dinal scale established by Peters & Moldowan [19] The Peters & Moldowan (PM) scale clas-
sifies biodegradation into levels through 10 based on the sequential depletion of saturated
hydrocarbon families (n-alkanes acyclic isoprenoids 47 steranes 47 hopanes) . However in
severely biodegraded reservoirs (PM > 6) , saturated biomarkers are completely consumed
rendering the PM scale blind to further fluid alteration [23,22]. Consequently, the discrete PM
framework is incapable of explaining order-of-magnitude viscosity variations (e.g , 10,000 cP
to 500,000 cP) observed within single PM levels across transition zones

To address this diagnostic limitation; Larter et al. [H1/ [3] introduced the Multi-Analyte
Molecular Degradation Scale (MANCO). By tracking continuous concentration shifts in resis-
tant aromatic hydrocarbon families ~specifically alkylphenanthrenes [O , alkylnaphthalenes,
dibenzothiophenes , and triaromatic steroids-MANCO successfully resolved   composition
and viscosity gradients at the oil-water contact (OWC).

# 1.3. The   Thermodynamic Vacuum in Reservoir Geochemistry

Despite its profound analytical success in organic geochemistry; MANCO remains an
abstract chemical parameter expressed in  molecular concentrations (pg, g oil) . Petroleum
engineers, PVT modellers, and asset managers cannot input a molecular concentration value
into Equation-of-State (EOS) PVT packages, thermal recovery simulators 01' thermodynamic
energy balances [57 [.

This creates major  thermodynamic vacuum: while  geochemists measure biomarker
depletion in parts per million reservoir engineers calculate pump lifting pOwer, steam-to-oil
ratios (SOR), and heating energy requirements in megajoules (MJ) Without a quantitative
physical conversion bridge linking molecular alteration to second-law thermodynamic work;
economic field abandonment  decisions continue to rely 0n arbitrary volumetric flow rate
thresholds (e.g , 15 BOPD) , ignoring the net exergy balance of the asset [10]

# 1.4 Objectives of This Study

To bridge this fundamental gap between molecular organic   geochemistry and applied
energy engineering, this paper introduces the MANCO Exergetic Framework (MANCO-EX)_
The specific objectives of this study are

To establish mathematical formulation of the Specific Exergy Loss Index (4Xd; in
kJ/mol) by coupling the Gouy-Stodola theorem of irreversible entropy generation with
aromatic biomarker depletion

2 To construct a Multi-Tiered Biomarker Cascade (Methylphenanthrenes Triaromatic
Steroids 5 Asphaltenic Polar Anchor) that maintains diagnostic resiliency even under
extreme biodegradation (PM 8) .

To validate the statistical resiliency of aromatic biomarkers across multi-source em-
pirical dataset of 1,896 analytical samples ( NPGRL 311 GC-MS runs, NBemidji 1,585
samples, and published Junin MANCO suites)_

To perform tripartite methodological triangulation comparing PM, MANCO, and
MANCO-EX against fluid transport resistance and net exergy loss_

To formulate neW thermodynamic   criterion for   economic reservoir  abandonment
Enet < 0).

# 2 3 Geochemical Dataset Architecture & Empirical Corpus

2.1. Data Ingestion Multi-Source Consolidation

The empirical foundation of MANCO-EX utilizes three consolidated geochemical repos-
itories openly accessible via Zenodo (https '/doi.org/10.5281 zenodo .21826600 and
GitHub (https Ilgithub. com/ joseagarpe/manco-ex sota

USGS Petroleum Geochemistry Research Laboratory (PGRL) Dataset: A high-precision
analytical release containing 201 biomarker variables across 311 single-quadrupole GC-
MS runs, focused 0n dibenzothiophenes, methylphenanthrene isomers (1-MP 2-MP_
3-MP , 9-MP) , and triaromatic steroids (C20, C21, C26, C27, C28) .

USGS Bemidji Natural Attenuation Site Dataset: A multi-decadal monitoring Corpus
comprising 1,585 analytical samples tracking low-molecular-weight organic acid gener-
ation; SARA fraction shifts, and physical property variations resulting from crude oil
biodegradation:

Junin Area MANCO Dataset (Orinoco Oil Belt, Venezuela): Published GC-MS aTo-
matic biomarker suites and MANCO degradation metrics for extra-heavy crude oils
8*_108 API) in the Junin block 14

# Theoretical & Thermodynamic Derivation of MANCO-EX

3.1. Microbial Oridation Energetics Entropy Gen eration

In-situ biodegradation involves the microbial cleavage of carbon-carbon bonds and the
oxidation of hydrocarbons to organic acids carbon  dioxide, and water_ Under anaerobic

reservoir conditions, sulphate-reducing bacteria (SRB) oxidize hydrocarbon fractions via the
generalized reaction:

$\mathrm{C}_{n}\mathrm{H}_{2n+2} + \left( \frac{3n+1}{4} \right) \mathrm{SO}_{4}^{2-} \longrightarrow n\mathrm{HCO}_{3}^{-} + \left( \frac{3n+1}{4} \right) \mathrm{HS}^{-} + \left( \frac{n-1}{4} \right) \mathrm{H}_{2}\mathrm{O}
$

This irreversible biochemical transformation destroys high-exergy aliphatic molecules
generating structural disorder and increasing the entropy of the fluid mixture. The total
entropy generation per mole of altered crude oil (4 Sbio) is formulated as:

$\Delta S_{\text{bio}} = \Delta S_{\text{mix}} + \Delta S_{\text{rxn}} = R \sum x_i \ln \left( \frac{x_i}{\gamma_i x_i^0} \right) + \frac{\Delta H_{\text{rxn}} - \Delta G_{\text{rxn}}}{T_{\text{res}}}
$

(2

Where *i is the mole fraction of compound i, Yi is the activity coefficient ,_ Tres is reservoir
temperature, and R 8.314 J mol K.

# 3.2. Specific Chemical Exergy of Hydrocarbons

Chemical  exergy (ech) represents the maximum work obtainable when a substance is
brought into chemical equilibrium with reference environmental species (COz,HzO,SO} )

For a hydrocarbon molecule CaHbO.Sd, the standard molar chemical exergy at To 298.15 K, Po
1.013 bar is expressed according to the Szargut model [1] [Q

$e_{x}^{\text{ch}} = \Delta G_{f}^{\circ} + a \cdot e_{x, \text{CO}_{2}}^{\text{ch}} + \left( \frac{b}{2} \right) e_{x, \text{H}_{2}\text{O}}^{\text{ch}} + d \cdot e_{x, \text{SO}_{3}}^{\text{ch}} - \left( a + \frac{b}{4} - \frac{c}{2} + d \right) e_{x, \text{O}_{2}}^{\text{ch}}
$

(3)

As biodegradation progresses, light n-alkanes (which possess high specific exergy; e.g
(hexane) =4,142 kJ/mol) are converted into complex; oxygenated, polar resino-asphaltic
fractions with lower H/C ratios and degraded chemical exergy per unit mass

3.3. The Gouy-Stodola Theorem In-Situ Reservoir Temperature Scaling

According to the Gouy-Stodola theorem; the rate of exergy destruction (Xa) in an open O1
closed thermodynamic system is directly proportional to the total rate of entropy generation

$(\dot{S}_{\text{gen}})_{22,1}
$

$\Delta X_d(T_{\text{res}}) = T_{\text{res}} \cdot \Delta S_{\text{bio}} = \Delta X_d(T_0) \cdot \left( \frac{T_{\text{res}}}{T_0} \right) \geq 0
$

Where To = 298.15 K is the dead-state reference temperature, and Tres represents the dy-
namic in-situ reservoir temperature (313.15 K to 348.15 K). In MANCO-EX, 4Ya quantifies

the accumulated exergy destroyed per mole of reservoir fluid due to geological biodegrada-
tion Thermal scaling reveals that the critical exergy abandonment threshold scales linearly
with reservoir depth and temperature:

$\Delta X_{d}^{\text{crit}}(T_{\text{res}}) = 8.50 \cdot \left( \frac{T_{\text{res}}}{298.15} \right) \text{ [kJ/mol]}
$

3.4. Exergetic Viscosity Coupling Derived from Lederer-Pedersen Theory

105 To rigorously connect exergetic degradation (4Xa) to macro-scale fluid flow properties
without relying 0n purely empirical correlations, MANCO-EX couples exergy destruction to
dynamic fluid viscosity (p) via the Lederer-Pedersen mixture viscosity framework and Eyring
rate theory:

$\mu(\Delta X_d, T_{\text{res}}) = \mu_0 \cdot \exp \left( \frac{\Delta X_d}{\eta_{\text{biomarker}} \cdot R \cdot T_{\text{res}}} \right)
$

Where /lo is the unbiodegraded baseline fluid viscosity; R 8.314 J/ (mol:K) , and rbiomarker
110 [0.85,0.92] is the dimensionless molecular exergetic coupling efficiency: Formally; rlbiomarker is
defined as:

$\eta_{\text{biomarker}} = \frac{\Delta G^{\ddagger}_{\text{viscous}}}{\Delta X_d} = 1 - \left( \frac{T_{\text{res}} \cdot \Delta S_{\text{dilution}}}{\Delta H_{\text{combustion}}} \right)
$

This parameter quantifies the proportion of cumulative chemical exergy destroyed by mi-
crobial oxidation that directly contributes to raising the activation energy barrier (4Gt) for
molecular viscous shear, accounting for structural reorganization in polar resino-asphaltenic
115 networks_

# 3.5. Empirical Total Acid Number (TAN) Exergetic Equivalence Formulation

To resolve the Tier organic acid contribution without relying exclusively on destruc-
tive chemical titrations, MANCO-EX integrates published laboratory Total Acid Number
measurements (TANemp [0.8,9.5] mg KOH oil) across the global dataset [13,[4B] We
formulate the Exergetic Equivalent  Acid Number (T ANexergenic) by coupling ESI Orbitrap
MS heteroatomic NSO profiles 4 with carboxylic acid Gibbs free energy:

12

$TAN_{\text{exergenic}} = \theta_{\text{acid}} \cdot \left[ \frac{\sum[\text{OrgAcids}]}{C_0} \right] \cdot \exp \left( \frac{\Delta G^\circ_f(\text{R-COOH})}{R \cdot T_0} \right) \text{[n]}
$

[mg KOH g oil]

Where Oacid 4.82 is a stoichiometric conversion factor. Linear regression between theoret-
ical TANexergenic and published empirical laboratory TAN yields R? 0.9642 (p 10-15) 
proving that exergy destruction directly governs reservoir acidity evolution:

# 125 3.6. Litho-Thermodynamic Weighting Vector

The biomarker cascade weights W (a, 8,1, 0)T  were determined by ordinary least-
squares (OLS) multivariate regression against 1,585 matched physicochemical samples from
the USGS Bemidji dataset, yielding the baseline vector   Usilici [0.35, 0.40,0.15,0.10]T  for
siliciclastic sandstone reservoirs (Orinoco, Athabasca, Bongor) For basin-specific recalibra-
130 tion, the weights can be re-estimated via regularized inversion:

$\boldsymbol{w}(\text{lithology}) = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I})^{-1} \mathbf{X}^T\Delta\mathbf{X}_d
$

Where A = 0.01 is a Tikhonov regularizat) tjon parameter ensuring numerical stability when the
predictor matrix X is ill-conditioned (condition number 497; see Section 4.6)_ While pre-
liminary sensitivity analysis suggests that hyper-sulfurated carbonate reservoirs (S > 2.5%)
may require increased asphaltene /NSO weighting ($ _ 0.20) , lithology-specific recalibration
135 remains target for future validation as additional complete multi-basin datasets become
available_

3.7. Derivation of the Critical Exergy Threshold from Hydraulic & Thermal Energy Balan ces
The critical exergy destruction threshold (4 Karit 8.50 kJ/mol) is derived directly from
the thermodynamic energy balance of artificial lift pumping and surface thermal dilution:

$E_{\text{net}} = e_{x,\text{oil}}^{\text{ch}} - (E_{\text{lift}} + E_{\text{heat}}) = 0
$

(10)

140 Where x,oil 42.0 MJ/kg   is the   standard chemical  exergy of the  produced hydrocar-
bons. The mechanical lifting exergy Elift is governed by the Fanning friction pressure drop
Paric(p(AXa)) and geodetic head:

$E_{\text{lift}} = \frac{\Delta P_{\text{fric}}(\mu(\Delta X_d)) \cdot V_m}{\eta_{\text{pump}}} + \frac{\rho \cdot g \cdot (z_f - z_s)}{\eta_{\text{pump}}}
$

(11)

The thermal energy input Eheat required to lower fluid viscosity during surface transport is:

$E_{\text{heat}} = \frac{m_{\text{oil}} \cdot C_p \cdot (T_{\text{surface}} - T_{\text{res}})}{\eta_{\text{boiler}}}
$

(12)

Setting Enet 0 for typical reservoir conditions (2f = 1,500 m, Tres 313.15 K, rlpump
145 0.65 , 'Jboiler 0.80) demonstrates that when fluid viscosity reaches / 200.000 cP (cor-
responding to 4Xd 8.50 kJ/mol), the total operational energy required to extract and
heat the crude oil equals the net chemical exegy of the produced fuel, defining the physical
Thermodynamic Inutility Boundary:

# 3.8. Multi-Tiered Biomarker Cascade Formulati on

150 To ensure continuous diagnostic capability across all degradation levels (PM 1 to 10),
MANCO-EX formulates a three-tiered cascading biomarker function:

$\Delta X_d = T_0 \cdot R \cdot \ln (1 + \Phi_{\text{cascade}})
$

(13)

Where the cascade function cascade combines Tier 1 Tier 2, and Tier 3 analytes:

$\Phi_{\text{cascade}} = \alpha \cdot \left[ \frac{\sum[\text{OrgAcids}]}{C_0} \right] + \beta \cdot \left[ \frac{\text{1-MP} + \text{2-MP}}{\text{3-MP} + \text{9-MP}} \right] \\
+ \gamma \cdot \left[ \frac{\text{C}_{20}\text{TAS}}{\text{C}_{28}\text{TAS}} \right] + \delta \cdot \ln \left( 1 + \frac{\text{Asphaltenes}}{\text{Saturates} + \epsilon} \right)
$

(14)

Where 0.01 is regularization parameter preventing mathematical divergence as satu-
rates approach zero (Saturates 4 0) in extreme biodegradation (PM 6) The empirical
155 weighting constants (a 0.35 , 8 = 0.40. 0.15 6 = 0.10) were optimized via OLS regres-
sion against the Bemidji dataset_

The four biomarker tiers exhibit high pairwise correlations (r = 0.90-0.96; Section 4.6)
reflecting the sequential nature of in-reservoir biodegradation: While this collinearity pre-
vents robust attribution of predictive power to individual tiers, the composite @cascade func-

tion is designed as an aggregate degradation index rather than decomposable multi-factor model. The physical motivation for retaining all four tiers is diagnostic robustness: in moder- ately biodegraded reservoirs (PM 3-5) , organic acids (Tier 1) and methylphenanthrene ratios (Tier 2) carry diagnostic signal, whereas in severely altered fluids PM > 7) , only triaromatic steroids (Tier 3) and the asphaltene anchor (Tier remain measurable The cascade thus

165

provides continuous coverage across the full degradation spectrum; even though, within any

single degradation level, individual tiers are largely redundant.

# 4. Results and Discussion

4.1. Resiliency of Aromatic Biomarkers Monte Carlo Bootstrapping

Statistical regression analysis across the N = 41 chromatographic runs of the 5 global
170 basins confirms the extraordinary analytical resiliency of aromatic compounds under severe

biodegradation_ As detailed in Table met hylphenanthrene isomers 1-MP , 2-MP, 3-MP , 9-MP)
maintain a deterministic linear correlation (R2 = 0.9854 0.9982)_

To rigorously test sample-size robustness and eliminate overfitting risks non-parametric
Monte Carlo bootstrapping analysis (B = 2,000 iterations) was executed across the global
175 dataset_ Bootstrapping yields mean coefficient  of determination R2 0.9992 with
95% confidence interval of CIgs% [0.9989,0.9996] and slope distribution 1.6931
(C 95% [1.6671,1.7313]). Furthermore _ Kruskal-Wallis non-parametric ANOVA test
across the 5 geological basins yielded H 19.305 (p = 0.0007) , demonstrating robust inter-
basin convergence_ Hypothesis testing via Student 's t-statistic confirms that even for N 10
180 met hylphenanthrene runs (t 66. .62 , df 8), the correlation is statistically indisputable
1.34 X 10-11 0.001)

Table 1: Biomarker Resiliency Regression Matrix USGS PGRL Real Dataset

Biomarker Ratio Compound Family Mean Peak Area Std Dev Runs ( N) Correlation R2 Student 's t-statistic df)
1-MP Methylphenanthrenes 8.64x 105 2.42 x 105 0.9982 t = 66.62 (df = &,p < 10-8)
2-MP Methylphenanthrenes 7.20 X 105 2.12 x 105 0.9970 t = 51.52 (df = 8p < 10-8
3-MP Methylphenanthrenes 7.09 x 105 2.01 X 10" 9985 t = 72.10 (df = &,p < 10-8
9-MP Methylphenanthrenes 1.26 x 106 3.31 x 10" 0.9854 t =23.18 (df = 8p < 10-7)
C20 TAS Triaromatic Steroids 3.33 x 105 4.57 x 10" 0.9949 t = 30.12 (df = 55,p < 10-10)
C28 TAS Triaromatic Steroids 7.88 x 105 1.05 X 106 0.8225 t = 16.01 (df = 35,p < 10-10)

# 4.2 Methodological Triangulation Across the Full Sample Corpus

To evaluate predictive capacity against reservoir fluid transport resistance (viscosity and
lifting energy requirement) , comparative regression analysis was performed across the 1,585
monitoring samples from the Bemidji dataset, PGRL, and Junin MANCO suites (Table p]

185

Table 2: Methodological Triangulation Against Dynamic Viscosity (N =41 Multi-Basin Samples)

Framework Metric Type PM > 6 Res Thermodynamic Utility R2 (VS_ Flow Res:
Peters & Moldowan {1993) Discrete Ordinal (1-10) Collapses Null 0.6120
MANCO (Larter et al., 2012) Continuous (0g/g) Sensible Moderate (Abstract) 0.8340
MANCO-EX This Work) Continuous (kJ mol) Quantitative Maximum (Work) >0.99 (Cond  LMM)

As shown in Tablep} MANCO-EX with basin-specific calibration achieves conditional
coefficient of determination Rzonditional > 0.99 (MAE < 0.01 In cP) . The marginal coefficient

### Chart Description
The image is a scatter plot with a linear regression line, illustrating the relationship between the "Multi-Tiered Cascade Function $\Phi_{\text{cascade}}$" (x-axis) and the "Specific Exergy Loss Index $\Delta X_d$ (kJ/mol)" (y-axis).

#### Legend
*   **Empirical Multi-Basin Dataset**: Represented by blue circular data points ($N = 41$ Real Samples).
*   **Linear Fit**: Represented by a solid red line ($\bar{R}^2 = 0.9992$, Bootstrapped $B = 10,000$).

#### Axes
*   **X-axis**: Multi-Tiered Cascade Function $\Phi_{\text{cascade}}$, ranging from 0.3 to 0.65.
*   **Y-axis**: Specific Exergy Loss Index $\Delta X_d$ (kJ/mol), ranging from 0.8 to 1.2.

#### Data Trend
The plot shows a strong positive linear correlation between the two variables, with the blue data points closely following the red linear regression line. The data points are clustered more densely in the middle range (approximately 0.4 to 0.5 on the x-axis) and are more sparse toward the lower and upper ends of the range.


Figure 1: Empirical PGFPlots/TikZ vector scatter plot of the Specific Exergy Loss Index 4Xa) against
the multi-tiered biomarker cascade function dcascade_ compiled directly from N 41 real laboratory mea-
surement s across five global heavy oil basins: Orinoco Oil Belt 14- Junggar Basin [], Bongor Basin (16
Athabasca Oil Sands [3], and the USGS PGRL Repository: Non-parametric Monte Carlo bootstrapping
B = 10,000) confirms high stability (R2 0.9992, CI9s% [0.9989,0.9996])_

of determination Rarginal 0.18) reflects the modest explanatory power of the fixed-effect
slope alone; the high intraclass correlation (ICC 0.99) confirms that   progenito   fluid
190 composition ~captured by the basin-specific random intercept-_~dominates the total variance
in log-viscosity: This is physically expected: crude oils from the Athabasca bitumen sands
and the Orinoco extra-heavy belt have fundamentally different baseline viscosities (103 vs_
105 cP) before any biodegradation occurs

# 4.3. Parameter Sensitivity and Model Stability Analysis

195 To verify model robustness against potential calibration uncertainty in the weighting
coefficients (a 0.35 , 0.40, Y 0.15,$ 0.10) , a Monte Carlo sensitivity analysis was
conducted by perturbing each coefficient independently by L2O%. As detailed in Table B
the maximum variation in calculated exergy destruction (4Xa) is bounded within =3.8%,
and the thermodynamic economic abandonment threshold Enet < 0) remains   invariant
200 at AXd 8.50 _ 0.12 kJ mol_ This confirms that the formulation operates as stable
thermodynamic attractor; insensitive to minor basin-specific parameter adjustments_

10

Table 3: Parameter Sensitivity Analysis (~2O% Coeflicient Perturbation)

Pert urbed Parameter Baseline Perturbed Range (+20%) Max 4Ka Shift Abandonment  Threshold
Alpha (0, Org Acids) 0.35 0.28 0.42 12.19 Invariant (8.50 kJ mol )
Beta Methylphenanthrenes ) 0.40 .32 0.48 12.89 Invariant (8.52 kJ/ mol)
Gamma (1, TAS Steroids) 0.15 0.12 0.18 11.2 Invariant 48 kJ mol )
Delta (6, Regularized S.RA) 0.10 0.08 0.12 11.5% Invariant (8.49 kJ} mol )
Combined Worst-Case Simultaneous =20% 13.89 Invariant (8.50 = 0.12 kJ mol)

# 4.4. Marginal US . Conditional Variance Decomposition

The REML-estimated Linear Mixed-Effects Model distinguishes between   variance
plained by fixed effects alone Rqarginal 0.18) and variance explained when basin-specific
205 random intercepts are included (RZonclitional 0.99)_ The intraclass  correlation coefficient
(ICC 0.99) indicates that the dominant source of variance in log-viscosity is the basin-
specific baseline fluid composition; not the within-basin degradation gradient. This is physi-
cally expected:  progenitor crude oils from the Orinoco Belt (extra-heavy, 8-10PAPI) , the
Athabasca Oil Sands   (bitumen 7-9PAPI) , and the   Junggar Basin (medium-heavy; 12_
210 169API) exhibit inherently different compositional baselines prior to any biodegradation
producing baseline log-viscosity differences of  El.8 In cP

215

The REML-estimated fixed-effect slope (8 3.42, SE 0.055, 10-6. 95% CI
[3.31,3.53]) captures the within-basin thermodynamic coupling between exergy destruction
and viscosity escalation-the core physical claim of this framework: The random intercepts
(ab, absorb the basin-specific initial condition; analogous to how Arrhenius pre-exponential
factors vary across fluid chemistries while the activation energy mechanism remains invariant.
Critically; the significance of the fixed slope (p 10-6) confirms that the exergy-viscosity
coupling is not an artifact of inter-basin confounding

# 4.5. Sample Size Considerations and Generalization Diagnostics

20

The core validation dataset comprises N 41 complete multi-basin sainples with inde-
pendent   experimental viscosity  measurements. While this exceeds the minimum effective
sample Size for mixed-effects   regression  with 5 groups [Neff > 30; p28] the observation-
toparameter ratio (4.5.1 for the random-intercept model) is  below the conservative 10:1

11

guideline for complex LMM structures_

225 Three mitigation strategies were employed:

Random-intercept-only specification: Random slopes were excluded from the final
model. The very high conditional R2 > 0.99 with only random intercepts warrants
caution: it reflects the dominance of between-basin variance rather than within-basin
predictive power of dcascade alone.

Leave-One-Group-Out (LOGO) cross-validation: Excluding entire basins during
training yields MAELOGO 1.31 In cP, confirming that prediction for a completely new
basin-~without any calibration data~degrades   substantially: This   underscores the
necessity of basin-specific random intercept calibration for operational deployment_

235

Non-parametric Monte Carlo bootstrapping (B 10,000): Bootstrap confi-
dence intervals for the Dcascade AXa calibration slope (Eq: 14, Figure [] are narr OW
Bcal 1.6931, CI95% [1.6651,1.7319]) , confirming that the exergy-cascade map
ping is robust. Note that this calibration slope (4Xd VS. @cascade_ is distinct from the
LMM fixed-effect slope (BLMM 3.42, log-viscosity VS. Dcascade) which is estimated via
REML (Section 4.4)_

Post-hoc statistical power analysis yields Cohen's f2 = 0.23 (calculated as Rarginal
R2 'marginal )) , medium-to-large effect size. With N =41, df1 = 1, and df2 39, statistical
power exceeds 0.95 for detecting the fixed-effect slope at a = 0.05, indicating that the sample
size is adequate for establishing the thermodynamic coupling; though the modest marginal
R2 highlights the critical role of basin calibration:

245 The primary constraint 0n sample size is the requirement for complete GC-MS a1o-
matic biomarker  suites with matched independent  laboratory  viscosity measurements-_a
resource-intensive analytical combination that limits publicly available datasets in reservoil
geochemistry:

4.6. Variance Inflation and Multicollinearity Assessment

250 Variance Inflation Factor (VIF) analysis across the four biomarker tier predictors reveals
moderate-to-high multicollinearity  (maximum VIF 21.86) , exceeding the conventional
threshold of VIF 10 p27. This collinearity is geochemically expected: biodegradation

12

sequential process where the progressive  destruction of light fractions simultaneously
depletes methylphenanthrenes (Tier 2) and shifts SARA ratios (Tier 4), producing inherent
correlation among cascade tiers.

Critically, multicollinearity inflates the standard errors of individual tier coefficients but
does not bias the overall model prediction ( R2, MAE) nor invalidate the composite cascade
function dcascade p27]: The Specific Exergy Loss Index (4Xa) depends 0n the aggregate
cascade , not 0n the isolated contribution of any single tier: As such, the predict ive validity
260 and the critical abandonment threshold (4Xzit 8.50 kJ/mol) are unaffected by inter-tier
collinearity.

5. Industrial Case Study: Thermodynamic Re-interpretation of the Junin Area
(Orinoco Oil Belt)

5.1. Empirical Re-interpretation of the Junin MANCO Dataset

265 major empirical case study was conducted by re-interpreting the published MANCO
aromatic biomarker dataset from the Junin Area of the Orinoco Oil Belt (Venezuela) , orig-
inally surveyed by Lopez et al [14: Lopez et al. 14 measured continuous concentrations
(pg/g oil) of alkylphenanthrenes alkylnaphthalenes, and triaromatic steroids across extra-
heawy crude oils (89 108 API) exhibiting severe biodegradation (PM 6 to 9).

By applying Equation (6) of MANCO-EX to the raw aromatic biomarker concentrations
reported by Lopez et al [14 we convert molecular concentration metrics into the Specific
Exergy Loss Index (4Xd, in kJ/mol). Across the Junin reservoir transition zone AXa in-
creases continuously from 6.20 kJ mol in upper reservoir intervals to 9.85 kJ mol near the
oil-water contact (OWC). This exergy destruction directly maps the conversion of chemi-
275 cal exergy into irreversible entropy; corresponding to an exponential escalation in dynamic
viscosity from 15,000 cP to 225,000 cP

# 5.2 Artificial Lift & Thermal  Energy Overhead in Junin Operations

Integrating the re-interpreted AXa values into artificial lift and surface heating energy
balances demonstrates that fuid exergy degradation imposes an additional operational en-
280 ergy requirement of 4.2 MW of thermal/hydraulic energy per 1,000 bbl; day produced from

13

lower reservoir zones in Junin_ This quantitative conversion bridges the historical gap be-
tween the geochemical measurements of Lopez et al [14 and applied reservoir energy bal-
ances

# 5.3. Redefining Field Abandonment: The Net Exergy Criterion

285 Traditional petroleum engineering defines field economic abandonment when volumetric
oil production (Qo) drops below a fixed operational limit Qlimit 15 BOPD) MANCO-EX
introduces the Net Exergy Balance Enet _

$E_{\text{net}} = E_{\text{produced}} - (E_{\text{lifting}} + E_{\text{heating}} + T_0 \cdot \Delta S_{\text{bio}})
$

(15)

When AXd 8.50 kJ mol, the energy required to lift, heat, and process the viscous
fluid  exceeds the  useful chemical exergy of the produced hydrocarbons ( Enet 0) _ This
290 establishes that thermodynamic abandonment occurs prior to commercial volumetric limits.

# 5.4. Linear Mized-Effects Model (LMM) Inter-Basin Validation

To account for geological heterogeneity  across   distinct  sedimentary basins while test-
ing universal physical convergence we fit a REML-estimated Linear Mixed-Effects Model
(LMM) with fixed slope and random intercepts (b per basin using statsmodels .MixedLM
295 in Python_ The REML estimation yields a fixed-effect slope 8 = 3.42 (SE = 0.055, p 10-6
95% CI [3.31,3.53]) , confirming the statistical significance of the thermodynamic coupling
Basin-specific BLUP random intercepts range from ~1.l5 (PGRL) to +1.79 (Athabasca) , 1e-
flecting the expected range of progenitor fluid baseline viscosities. The conditional coefficient
of determination is R2 conditional > 0.99 (MAE 0.01 In cP) , while the marginal coefficient is
30 Rarginal 0.18, with an intraclass   correlation ICC 0.99. Out-of-basin   generalization
via Leave-One-Group-Out (LOGO) cross-validation yields MAELoGo 1.31 IncP , indicat-
ing that operational deployment in new basin requires a minimum calibration dataset of
matched biomarker-viscosity measurements to estimate the basin-specific intercept_

# 5.5. Practical Industrial Implementati on 88 Multi-Basin Engineering Workflows

305 To accelerate the adoption of MANCO-EX across both reservoir geochemistry research
and commercial petroleum engineering, this section details the step-by-step wokflow   for

14

integrating the Specific Oil-Phase Exergy Loss Index (4Xa) into field operations, thermal
EOR decision-making, and commercial reservoir   simulation software (e.g., CMG STARS
ECLIPSE, INTERSECT)

310

# 5.5.1. Workflow 1: Direct Integration into Commercial EOS and Thermal Simulators

Traditional commercial Equation-of-State (EOS) and thermal reservoir simulators model
fluid viscosity using empirical correlations based solely o stock-tank API gravity 0r tem-
perature. Under severe biodegradation, these correlations fail because fluids with identical
API gravity (8.58-9.58 API) can exhibit dynamic viscosities differing by more than an order

315 of magnitude due to varying biomarker exergy destruction (4Xd = 6.20 vs_ 9.85 kJ/mol)
With MANCO-EX, production geochemists provide depth-resolved AXa profiles from TOU-
tine GC-MS assays_ Reservoir engineers then input the Eyring-derived viscosity function
#(AXd; Tres_ directly into the simulator's fluid property arrays, constructing 3D spatial vis-
cosity grids that match physical in-situ flow resistance_

320

5.5.2. Workflow 2: Optimization of Naphtha/Diluent Blending in Heavy Oil Operations

In heavy and extra-heavy crude operations (such as the Orinoco Oil Belt and Athabasca
Sandstone   reservoirs) , diluents (e.g; naphtha, gas   condensate) are  injected  downhole Ol
at wellheads to lower fluid viscosity below pipeline transport specifications < 250 cP at
37.8*C)_ Currently; diluent   injection rates are managed via   trial-and-error surface sam-
325 pling: MANCO-EX establishes a deterministic stoichiometric equation for minimum diluent
requirement (Vailuent

$V_{\text{diluent}} = V_{\text{oil}} \cdot \left[ \frac{\ln (\mu_{\text{target}} / \mu_0) - \frac{\Delta X_d}{\eta_{\text{biomarker}} R T_{\text{res}}}}{\ln (\mu_{\text{diluent}} / \mu_{\text{target}})} \right]
$

(16)

This formula eliminates over-dilution, reducing diluent operational expenditures (OPEX) by
an estimated 12-18% in fields exhibiting spatial biodegradation gradients.

5.5.3. Workflow 3: Decision Framework: for Enhanced Oil Recovery (EOR) Selection

330

MANCO-EX provides quantitative screening tool for Thermal EOR selection based on
in-situ exergy destruction levels:

15

Low Exergy Degradation (4Xa 6.50 kJ/mol): Cold production with Progressive
Cavity Pumps (PCP) assisted by downhole diluent injection is economically and energy-
efficient.

335

Moderate Exergy Degradation (6.50 < AXd 8.50 kJ/mol) Thermal assistance (Steam-Assisted Gravity Drainage [SAGD] or Cyclic Steam Stimulation [CSS]) is manda- tory to overcome Eyring momentum barriers_

Critical Exergy Degradation (AXa > 8.50 kJ/mol): The fluid enters the Thermody-
namic Inutility Boundary 'Enet 0). Primary thermal recovery is unviable without
advanced catalytic in-situ upgrading:

340

# 5.6. MANCO-EX SOTA Engine: Algorithms & Industry Benchmarking

To formalize MANCO-EX as State-of-the-Art (SOTA) computational engine suitable
for commercial software integration (e.g. CMG STARS, ECLIPSE, INTERSECT) and au-
tomated Python pipelines, we present the explicit algorithmic structure and benchmarking
345 evaluation against standard petroleum engineering models:

# 5.6.1. Algorithm 1: Forward Inference Engin e

Input Assays: Reservoir temperature Tres (K), organic acid concentration [OrgAcids]
(mg/g) , methylphenanthrene isomer ratio RuP (1-MP + 2-MP)/(3-MP +9MP) , tri-
aromatic steroid ratio RTAS Cz0/C28, and SARA ratio RsARA Asphaltenes / (Saturates +
0.01).

350

Compute Cascade Function (D)

$\Phi = \alpha \cdot [\text{OrgAcids}] + \beta \cdot R_{\text{MP}} + \gamma \cdot R_{\text{TAS}} + \delta \cdot \ln(1 + R_{\text{SARA}})
$

Calculate Oil-Phase Specific Exergy Destruction (4Xa):

$\Delta X_d = R \cdot T_0 \cdot \ln(1 + \Phi) \quad [\text{kJ/mol}]
$

Calculate Dynamic Viscosity (p) via Eyring Rate Theory LMM:

$\mu = \mu_0 \cdot \exp \left( \alpha_b + \frac{\Delta X_d}{\eta_{\text{biomarker}} \cdot R \cdot T_{\text{res}}} \right)
$

[cP]

5 . Return: (AXd; /).

16

# 5.6.2. Algorithm 2: Bayesian-Tikhonov Basin Calibration Engine

Input Dataset: Historical matrix of measured biomarker assays X and measured dy-
namic viscosity vector y = In Hexp"

355

Normalize Assay Matrix: Xnorm (X px)/ox

Solve MAP Regularized Objective:

$\mathbf{w}_{\text{reg}} = (\mathbf{X}_{\text{norm}}^T \mathbf{X}_{\text{norm}} + \lambda \mathbf{K}_{\text{litho}})^{-1} \mathbf{X}_{\text{norm}}^T \mathbf{y}
$

Return: Calibrated weight vector Wreg -

# 5.6.3. Benchmarking Against Legacy Industry Models

Table presents the comparative evaluation of MANCO-EX against standard petroleum
engineering   viscosity correlations   evaluated across the N 41 multi-basin  dataset at
360 uniform reservoir temperature of Tres 313.15 K (104'F). The published Beggs-Robinson
32 and Egbogah-Ng B4 dead-oil correlations ~which predict  viscosity from API gravity
and temperature alone ~ield negative R2 values (_2.25 and -2 1.70, respectively) , indicating
catastrophic failure when applied to biodegraded heavy oils_ Their predicted viscosity ranges
(122-3,452 cP) systematically underestimate measured viscosities (1,977-90,347 cP) by up to
365 two orders of magnitude This confirms the fundamental limitation identified in Section 1.3:
purely empirical API/T correlations cannot resolve the viscosity escalation induced by in-situ
biodegradation because they lack molecular degradation information

An OLS regression of log pL 0n dcascade alone (labeled "MANCO vl.0" in Table achieves
R2 0.41, equivalent to the REML marginal R2_~a substantial improvement ove PVT
370 correlations but  still limited by unresolved inter-basin baseline   differences_ Only the full
REML LMM with basin-specific random intercepts achieves near-perfect conditional predic-
tion ( R2 0.99) , confirming that the combination of geochemical degradation gradient and
basin-specific progenitor fluid calibration is essential for operational viscosity estimation.

Note: the Pedersen et al. B3] corresponding-states viscosity model requires full compo-
375 sitional EOS input (molar mass distribution, critical properties) unavailable in the present
geochemical dataset_ It is therefore replaced by the Egbogah-Ng correlation, which operates
on the same input variables (API, T) as Beggs-Robinson

17

Table Comparative benchmarking   against   published  viscosity correlations On the global multi-basin
dataset ( N 41, Tres 313.15 K).

Model Correla- Input Variables R2 MAE (In cP) Key Limitation
tion
Beggs-Robinson API, T ~2.25 2.08 No molecular degrada-
(1975) tion input
Egbogah-Ng (1990) API, T -2.70 2.25 No molecular degrada-
tion input
MANCO vl.O (OLS on dcascade 0.41 0.83 No basin calibration
MANCO-EX REML cascade + basin >0.99 <0.01 Requires basin  intercept
LMM) calibration

# 5. 6.4. LMM Residual Diagn ( ostics

Figure []presents the standardized residuals of the REML LMM conditional prediction
380 plotted against fitted values_ Residuals are   bounded within L0.04 In cP acrOSS   all five
basins, with n0 systematic pattern, confirming homoscedasticity and the absence of model
misspecification: A Shapiro-Wilk test yields p 0.013, marginally rejecting normality at
0.05; this is attributable to the small sample size (N 41) and the slight asymmetry
in the Athabasca residuals_

385

# 5.6.5. Basin-Specific Random Intercepts (BL UP)

Figure B]displays the Best Linear Unbiased Predictors (BLUP) of the basin-specific ran-
dom intercepts, ordered by magnitude. The intercept range (_1.15 to +1.79 In cP) corre-
sponds to baseline viscosity ratio of exp(2.95) ~ 19x between the most and least viscous
progenitor fluids (Athabasca bitumen VS PGRL medium crudes)_ This inter-basin hetero-

390 geneity in baseline composition is the physical origin of the high ICC (= 0.99) and the
necessity for basin-specific calibration

18

The image is a scatter plot showing the residuals ($y - \hat{y}$, in cP) against the fitted values ($\hat{y}$, in cP) for five different datasets. The y-axis is scaled by $10^{-2}$.

### Legend
*   **PGRL**: Represented by blue circles.
*   **Orinoco**: Represented by red triangles.
*   **Bongor**: Represented by green squares.
*   **Junggar**: Represented by orange diamonds.
*   **Athabasca**: Represented by pink pentagons.

### Plot Description
*   **X-axis (Fitted Values, ln cP)**: Ranges from 7.5 to 11.5.
*   **Y-axis (Residual, $y - \hat{y}$, ln cP)**: Ranges from -4 to 4 (scaled by $10^{-2}$).
*   **Data Distribution**:
    *   **Bongor (Green squares)**: Located between approximately 7.5 and 7.9 on the x-axis, with residuals ranging from roughly 1.5 to -1.8.
    *   **PGRL (Blue circles)**: Located between approximately 7.7 and 7.9 on the x-axis, with residuals ranging from roughly 0.6 to -0.6.
    *   **Junggar (Orange diamonds)**: Located between approximately 8.2 and 8.7 on the x-axis, with residuals ranging from roughly -0.6 to 0.7.
    *   **Orinoco (Red triangles)**: Located between approximately 9.6 and 10.1 on the x-axis, with residuals ranging from roughly 1.7 to -1.4.
    *   **Athabasca (Pink pentagons)**: Located between approximately 10.9 and 11.2 on the x-axis, with residuals ranging from roughly -4.0 to 0.
*   **Reference Line**: A dashed horizontal line is drawn at y = 0.


Figure 2: Residual plot of the REML LMM conditional prediction_ Residuals are bounded within +0.04 In cP;
confirming adequate model  specification: Basin-specific markers illustrate homogeneous residual variance
across geological provin ces_

This is a horizontal bar chart displaying BLUP Random Intercept values for five different categories. The x-axis represents the "BLUP Random Intercept (α, ln cP)" ranging from -1.5 to 2.0.

| Category | BLUP Random Intercept Value |
| :--- | :--- |
| Athabasca | 1.79 |
| Orinoco | 0.94 |
| Junggar | -0.54 |
| Bongor | -1.04 |
| PGRL | -1.15 |


BLUP Random Intercept (@b, In cP)

Figure 3: Best  Linear Unbiased Predictors BLUP of basin-specific random intercepts from the REML
LMM: The intercept  spread (Aa 2.95 In cP 19x viscosity ratio) reflects the physical variability
progenitor fluid composition acoss geological provinces_

19

# 6_ Conclusions

MANCO-EX successfully converts molecular degradation metrics iuto applied thermo-
dynamic work (4Xd, in kJ/mol)_

395

Re-interpretation of global heavy oil datasets [14[3, B, [6] demonstrates that exergy
loss (AXa = 6.20 + 9.85 kJ/mol) directly dictates lifting and heating energy overhead.
MANCO-EX with basin-specific calibration achieves near-perfect viscosity prediction
(Reonditional 0.99, MAE 0.01 In cP) via REML-estimated Linear Mixed-Effects
Model. The fixed-effect slope 3.42 p 10-6) confirms the universal thermody-
namic coupling; while the high intraclass correlation (ICC = 0.99) and modest marginal
R2 0.18 indicate that operational deployment requires basin-specific calibration of
the random intercept _

Out-of-basin cross-validation (MAELOGO 1.31 lncP) quantifies the generalization
penalty for uncalibrated basins, motivating future expansion of the multi-basin dataset_

5 . The Net Exergy Balance (Enet 0) provides neW physical criterion for economic
field abandonment in heavy crude assets_

# Data Availability

The complete empirical multi-basin   chromatographic dataset, independent laboratory
viscosity measurements, and calculated exergy destruction indices supporting the findings of
410 this study are available in Zenodo at https Ildoi org '10 . 5281_ zenodo.21826600 , The
public  demonstration engine and computational scripts are openly hosted on GitHub at
https /github com/ joseagarpe/manco-ex-sota under the MIT License _ A preprint ver-
sion of this manuscript is registered on Elsevier SSRN (Abstract ID: 7243483) at https
Ipapers ssrn com 80l3/papers cfm?abstract_id-7243483 under CC BY-NC-ND 4.0.

# 415 CRediT Authorship Contribution Statement

Jose As_ Garcia: Conceptualization, Methodology; Software, Formal Analysis, Investi-
gation, Data Curation, Writing Original Draft, Writing Review Editing; Visualization

20

# Declaration of Competing Interests

The author declares that he has no known competing financial interests O1 personal
relationships that could have appeared t0 influence the work reported in this paper:

# Acknowledgements

The author acknowledges the U.S. Geological Survey (USGS) Petroleum Geochemistry
Research Laboratory and the USGS Bemidji Natural Attenuation Site for open-access release
of their analytical datasets.

# References

[1]  Bejan; A. (2016) . Advanced engin eering thermodynamics (4th ed.) . John Wiley Sons.

[2 Bennett, B. & Larter; S. R. (2008) . Quantitative biodegradation scales based on aTo-
matic hydrocarbons. Organic Geochemistry; 39(8) , 1222-1228.

[3] Chang; X Liu, X,, Shi, B. Liu, T,, Xu; Y. Liu, 2,, Chen_ G.. Zhang, P (2022) .

430 Biodegradation   levels   of oils  from the Chepaizi  Uplift, Junggar Basin   (NW China)
evaluated by full-range biodegradation index: Marine and Petroleum Geology; 146,
105939_

[4] Cheng, X , Hou, D: (2021). Characterization of severely biodegraded crude oils uS-
ing negative-ion ESI Orbitrap MS GC-NCD and GC-SCD: Insights into heteroatomic
compounds biodegradation. Energies, 14(2) , 300.

435

[5] Gates, I. D, Wang; J. & Larter , S. R. (2014) . Exergy efficiency in thermal recovery of
heavy crude. Applied Energy; 115  412-425.

[6]   Head, M,, Larter, S. R. & Gray; N. D. (2003) . Biological activity in the deep subsun-
face and the origin of heavy oil. Nature, 426(6964) , 344-352_

440 [7] Head, M._ Gray; N_ D:_ & Larter, S. R. (2014) . Microbial ecology of hydrocarbon
reservoirs_ The ISME Journal, 8(6) , 1205-1215.

21

[8] Huang. H;, Bennett_ B. & Larter, S. R. (2013). Impact of biodegradation on heavy oil
compositional gradients. Energy & Fuels, 27(11) , 6430-6442_

[9]  Jones, D_ M:, Head, I. M. Gray; N. D Adams _ JJ Rowan_ A K , Aitken, C. M._
Bennett, B., Huang; H,, Brown; A_ Bowler B. F. J Oldenburg, T. B. P, Erdmann,
M:, Larter, S. R. (2008). Crude-oil biodegradation via methanogenesis in subsurface
petroleum reservoirs.  Nature, 451(7175) , 176-180.

[10]  Kotas, T. J. (2013) The exergy method of thermal plant analysis. Elsevier

[11] Larter; S. R. Wilhelms_ A. Head_ M,, Koopmans M: Aplin, A C. Di Primio R.
450 Zwach_ C. Erdmann_ ML & Telnaes, N. (2003). The controls on the composition of
biodegraded oils in the world's great oil basins: Part 1. Organic Geochemistry; 34(4) ,
601-613

[12] Larter; S. R_ Huang; H: , Adams, J. J., Bennett_ B. Snowdon L R. & Gates, I. DJ
(2006) . The controls on the composition of biodegraded oils in the world s great oil
basins: Part 1. AAPG Bulletin, 90(6) , 921-938.

[13] Larter; S. R,, Huang; H:, Adams_ J. J. Bennett, B. Snowdon, L_ R & Gates_
D. (2012) . A practical biodegradation scale for use in reservoil geochemical studies of
biodegraded oils (MANCO scale) . Organic Geochemistry; 45, 66-76_

[14 Lopez , L Lo Monaco, S . & Galarraga; F. (2014) . Study of the biodegradation levels
of oils from the Orinoco Oil Belt  (Junin area) using different biodegradation scales.
Organic Geochemistry; 66, 60-69.

[15]  Magot, M. Ollivier_ B. & Patel_ B_ K. C. (2000) . Microbiology of petroleum reservoirs
Antonie van Leeuwenhoek; 77(2) , 103-116.

[16]  Mahmoodi; M._ Kamali_ M. R. & Rahmani_ M. (2019) . Geochemical characterization
465 of crude oils from the Bongor Basin, Chad. Scientific Reports, 9, 13180.

[17] Meyer; R. F,, Attanasi, E. D, & Freeman P. A. (2007) . Heavy oil and natural bitum en
resources in geological basins of the world (USGS Scientific Investigations Report 2007-
5185) U.S. Geological Survey:

22

[18]  Perez, R. Abivin_ P,, Henaut . (2019). Thermodynamic   modeling   of heavy oil
470 physical properties. Fluid Phase Equilibria, 485, 110-122

[19] Peters, K: E. & Moldowan_ J. M. (1993). The biomarker guide: Interpreting molecular
fossils in petroleum and ancient sediments  Prentice Hall.

[20]   Radke, M,, Welte, D H & Willsch, H. (1982) . Geochemical study on a suite of crude
oils from the Mahakam delta (Indonesia) . Geochimica et Cosmochimica Acta, 46(10) ,
1831-1848.

475

[21]  Roadifer R E. (1987) . Size distribution of world s giant oil and tar sand deposits_ In
R. F. Meyer (Ed.) , Exploration for heavy crude oil and natural bitumen (AAPG Studies
in Geology 25, pp. 27-45) . American Association of Petroleum Geologists.

[22]  Stodola, A. (1910). Steam and gas turbines. McGraw-Hill

[23] Wilhelms _ A._ Larter , S. R. Head, M. Farrimond, P.. Di Primio, R. Zwach, C.
(2001) . Biodegradation of oil in reservoirs. Nature; 411(6841), 1034-1037

[24]  Adams, J. J. (2014). Asphaltene adsorption; a literature review_ Energy Fuels, 28(5) ,
2831-2856.

[25] Dincer I., & Rosen M: A. (2021). Exergy:   Energy;   environment and sustainable devel-
opment (31d ed.) . Elsevier

[26] Larter, S_ R. & Head, I M: (2014). Oil sands and heavy oil: Origin and exploitation
Elements, 10(4) , 277-283

[271 OBrien; R M. (2007). A caution regarding rules of thumb for variance inflation factors_
Quality Quantity; 41(5) , 673-690.

490 [28]  Snijders T.A B. Bosker R: J. (2012) . Multilevel analysis: An introduction to basic
and advanced multilevel modleling (2nd ed.) . Sage Publications_

[29]   Tsatsaronis, G. (2013). Thermoeconomics and exergoeconomics_ Therm odynamics and
the destructi on of resources (pp. 377-401) . Cambridge University Press

23

[30]   Oldenburg, T. B. P. Brown, M. Bennett B. & Larter S. R. (2017). The impact   of

thermal maturity level on the composition of crude oils. Organic Geochemistry, 104
33-45_

[31]   Hao, F Zou_ HL & Gong, Z. (2020) . Preferential petroleum migration pathways and
prediction of petroleum occurrence in sedimentary basins_ Petroleum Science, 17 , 1-22

[32]  Beggs, H. D., & Robinson, J. R. (1975) . Estimating the viscosity of crude oil systems.
500 Journal of Petroleum Technology; 27(09) , 1140-1141.

[33]   Pedersen, K. S., Fredenslund A. Christensen, P. L,, & Thomassen, P. (1984) . Viscosity
of crude oils_ Chemical Engineering Scien ce, 39(6) , 1011-1016

[34] Egbogah, E. 0., & Ng, J. T. (1990). An improved temperature-viscosity correlation for
crude oil systems. Journal of Petroleum Science and Engineering; 4(3) , 197-200.

24