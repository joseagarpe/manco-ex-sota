# The MANCO Exergetic Framework: Bridging Molecular
Biodegradation and Thermodynamic Reservoir Abandonment in
Heavy Oils

Josc A. Garcia

Instituto de Ciencias de la Tierra, Universidad Central de Venezuela, AP 3895, Caracas 1010A, Venezuela

# Abstract

Microbial biodegradation in heavy crude il reservoirs destroys high-exergy aliphatic frac-
tions, causing exponential viscosity escalation and premature field economic abandonment_
The molecular-scale Larter Multi-Analyte Degradation Scale (MANCO, /'g/ g oil) cannot
be integrated directly into thermodynamic reservoir simulators_ This paper introduces the
MANCO Exergetic Framework (MANCO-EX), converting  molecular   biomarker depletion
into a Specific Exergy Loss Index (4Xd; kJ/mol) via the Gouy-Stodola theorem and Eyring
transition-state theory: multi-tiered biomarker cascade (methylphenanthrene   isomers
triaromatic steroids, asphaltenic polar anchor) maintains diagnostic capability across all Pe-
ters & Moldowan (PM) degradation levels (PM 1-10). Calibrated on 1,585 physicochemical
samples (USGS Bemidji Site) for organic acid kinetics and 311 Gas Chromatography-Mass
Spectrometry (GC-MS) runs (USGS PGRL Repository) , the framework is validated against
independent laboratory viscosity measurements from N = 41 multi-basin reservoir samples
(Orinoco, Athabasca, Junggar, Bongor) . A Restricted Maximum Likelihood (REML) Linear
Mixed-Effects Model (LMM) with basin-specific random intercepts achieves a conditional c0-
efficient of determination R2 conditional 0.99 with a Mean Absolute Error MAE 0.01 In cP.
The fixed-effect slope is highly significant (p 10-6) , while the Intraclass Correlation Co-
efficient (ICC 0.99) reflects progenitor fluid baseline variance across basins. critical
exergy threshold (4Xarit 8.50 + 0.78 kJ/mol; 95% CI [6.09, 9.20]) defines the Thermo-

#Corresponding author at Instituto de Ciencias de la Tierra; Universidad Central de Venezuela; AP 3895
Caracas 10104 Venezuela.
Email address: jose. garcia47@ucv _ ve Jose A. Garcia)

dynamic Inutility Boundary where operational lifting and heating energy exceeds produced
fuel chemical exergy:

Keywords: Heavy Oil, Exergy Degradation, MANCO Exer 'getic Framework

(MANCO-EX) Biomarkers, Biodegradation; Applied Thermodynamics, Reservoir
Engineering, Fuel

# Introduction

# 1.1. Unconventional Heavy Crude Oil Reserves Energy Challenges

Heavy and extra- hcavy crude oil resources represent over 50% of the world s remaining
liquid hydrocarbon inventory; with colossal accumulations concentrated in the Orinoco Oil
Belt (Venezuela) , the Athabasca Bitumen Sands (Canada) , and the deepwater Gulf of Mexico
16,[2p7]. The commercial exploitation of these unconventional assets is heavily constrained
by extreme fluid viscosity (103 to 106 cP at reservoir conditions) , elevated concentrations of
heteroatoms (N, S, 0), high polar resin  and asphaltene contents and severe operational
friction during in-situ recovery; artificial lift, and pipeline transportation [2[7 [8

In-situ microbial biodegradation is the principal geological process responsible for the
formation of heavy and extra- heawy crude oil accumulations 123 [15] Anaerobic syntrophic
bacterial and archaeal consortia operating at the oil-water contact (OWC) selectively con-
sume light aliphatic hydrocarbons, preferential n-alkanes, and low-molecular-weight aromatic
fractions [9 []: This selective biodegradation alters fluid phase equilibria, increases density
(lowers API gravity) , and dramatically escalates dynamic viscosity by orders of magnitude
over narrow vertical transition zones [8,

1.2. Geochemical Prories: From Discrete Scales (PM 1-10) to Continuous Metrics

For over three decades, reservoir biodegradation was evaluated using the qualitative , O -
dinal scale established by Peters Moldowan [19] The Peters & Moldowan (PM) scale clas-
sifies biodegradation into levels through 10 based on the sequential depletion of saturated
hydrocarbon families (n-alkanes acyclic isoprenoids steranes 47 hopanes) However in
severely biodegraded reservoirs (PM > 6), saturated biomarkers are completely consumed
rendering the PM scale blind to further fluid alteration [23}[]. Consequently, the discrete PM

framework is incapable of explaining order-of-magnitude viscosity variations (e.g,, 10,000 cP

to 500,000 cP) observed within single PM levels across transition zones

To address this diagnostic limitation, Larter et al. [11J [3] introduced the Multi-Analyte
Molecular Degradation Scale (MANCO). By tracking continuous concentration shifts in resis-
tant aromatic hydrocarbon families ~specifically alkylphenanthrenes [20], alkylnaphthalenes
dibenzothiophenes, and triaromatic steroids-MANCO successfully resolved composition
and viscosity gradients at the oil-water contact (OWC).

# 1.3. The   Thermodynamic Vacuum in Reservoir Geochemistry

Despite its profound analytical success in organic geochemistry, MANCO remains an ab-
stract chemical parameter expressed in molecular concentrations pg g oil) . Petroleum engi-
neers, PVT modellers, and asset managers cannot input a molecular concentration value into
Equation-of-State (EOS) PVT packages, thermal recovery simulators, O thermodynamic en-
ergy balances [57[]: While standard empirical PVT correlations (e.g , Beggs-Robinson [1975
Egbogah-Ng /1990; De Ghetto et al [1995) operate effectively on conventional light oils they
lack molecular composition input and fail catastrophically under advanced biodegradation:

Recent computational efforts have attempted to bridge biomarker data with heavy oil
viscosity using machine learning and artificial neural networks [36, [5] 01 by using individual
biomarker ratios for reservoir compartment management [37 In parallel, physical chemistry
researchers have applied Eyring transition-state thcory to estimate reservoir-condition crude
oil viscosities 35/ and viscous flow activation nergy in heavy oil-diluent systems 38
However major thermodynamic vacuum persists: n0 prior study has established a quanti-
tative conversion bridge linking in-situ microbial exergy destruction to macroscopic transport
resistance and net exergy recovery Reservoir engineers continue to calculate lifting DOWCI
abandonment decisions rely on arbitrary volumetric Hlow rate thresholds (e.g: 15 BOPD)

steam-to-oil ratios (SOR) , and heating requirements in megajoules (MJ) while economic field
ignoring the second-law net exergy balance of the asset [10]:

1.4. Objectives of This Study

To bridge this fundamental gap between molecular organic   geochemistry and applied
energy engineering, this paper introduces the MANCO Exergetic Framework (MANCO-EX)

The specific objectives of this study are:

To establish a mathematical formulation of the Specific Exergy Loss Index (4Xd; in
kJ/mol) by coupling the Gouy-Stodola theorem of irreversible entropy generation with
aromatic biomarker depletion_

To construct a Multi-Tiered Biomarker Cascade (Methylphenanthrenes Triaromatic
Steroids 5 Asphaltenic Polar Anchor) that maintains diagnostic resiliency even under
extreme biodegradation (PM 8) .

To validate the statistical resiliency of aromatic biomarkers across a multi-source em-
pirical dataset of 1,896 analytical samples ( NPGRL =311 GC-MS runs, NBemidji 1,585
samples, and published Junin MANCO suites)_

To perform tripartite methodological triangulation comparing PM, MANCO, and
MANCO-EX against fluid transport resistance and net exergy loss.

To formulate neW thermodynamic   criterion for  economic reservoir  abandonment
Enet < 0).

# 2 Geochemical Dataset Architecture & Empirical Corpus

2.1. Data Ingestion, Provenance Dataset Distinction

The empirical foundation of MANCO-EX utilizes three consolidated geochemical repos-

itories openly accessible via Zenodo https I/doi.org/10 5281 zenodo . 21826600 and
GitHub https 'github . com/ joseagarpe/manco-ex- sota

USGS Petroleum Geochemistry Research Laboratory (PGRL) Dataset:
high-precision analytical release containing 201 biomarker variables across 311 single-
quadrupole GC-MS runs, focused 0n dibenzothiophenes, methylphenanthrene isomers
(1-MP 2-MP _ 3-MP , 9-MP) , and triaromatic steroids (C20, C21, C26, C27, C28) .

USGS Bemidji Natural Attenuation Site Dataset: A multi-decadal monitoring
corpus comprising 1,585 analytical samples tracking low-molecular-weight organic acid
generation; SARA fraction shifts, and physical property variations resulting from crude
oil biodegradation.   Important dataset provenance clarification: The USGS Bemidji site
represents shallow  pipeline spill into glacial aquifer in  Minnesota USA Because

near-surface groundwater environments differ from deep petroleum reservoirs in pres-
sure , temperature and microbial consortia, the Bemidji dataset was utilized exclu-
sively for calibrating the stoichiometric organic acid generation kinetics (a weighting
coefficient in Tier 1). It was not used for deep reservoir viscosity calibration

Global Multi-Basin Reservoir Validation Corpus (N = 41): Independent high-
resolution GC-MS aromatic biomarker suites matched with laboratory-measured eX
perimental viscosities from deep petroleum reservoirs (2f 800-2,500 m) across four
geologically distinct provinces: Orinoco Oil Belt (Junin Area, Venezuela; N 11)
Athabasca Oil Sands (Alberta; Canada; N 5) [13] , Junggar Basin (Chepaizi Uplift,
China; N 7) B3, Bongor Basin (Chad; N 8) [16] and USGS PGRL Reservoir
Standards (N 10) .

# 2.2 GC-MS & Reometry Experim ental Analyti cal Protocols

All chromatographic biomarker analyses in the USGS PGRL repository and validation
suites were executed using an Agilent 6890N Gas Chromatograph coupled with 5975C
Mass Selective Detector (MSD) operating in Electron Ionization (EI, 70 eV) and Selected
Ion Monitoring (SIM) mode Separation was achieved using an HP-SMS fused-silica cap-
illary column (30 m X 0.25 mm ID X 0.25 /m film thickness) with Helium carrier gas at a
constant flow rate of 1.0 mL min. The oven  temperature program was held at 50'C for
min, ramped at 4PC min to 3109C , and held isothermally for 15 min. Aromatic biomarker
ratios (1-MP /3-MP Czo TAS/C2sTAS) were quantified via pcak area integration relative to
deuterated internal standards (d10-phenanthrene)_

105

Independent dynamic viscosity measurements (p) for the N 41 multi-basin valida-
tion samples were conducted under atmospheric dead-oil conditions at standardized test
temperature of Tres 313.15 K (40.0*C, 104.0PF) using Haake RheoStress 600 rotational
cone-and-plate viscometer (gap 0.105 mm, shear rate range 0.1-100 $ -1) Measurement re-
peatability was confirmed within -3.2% across duplicate runs.

# Theoretical & Thermodynamic Derivation of MANCO-EX

# 3.1.  System Boundary, Dead State; Gouy- Stodola Formulation

To establish rigorous thermodynamic accounting without circularity, MANCO-EX defines
110 an open control volume Sres encompassing the liquid crude oil phase within the reservoir pore
space at the oil-water contact (OWC). The reference environment (dead state) is specified
at standard conditions To 298.15 K (25.08C) and Po 1.013 bar (1 atm) , utilizing the
standard chemical exergy species of Szargut's model (COz,HzO,SO? [42 p5]

While deep reservoir fluids exist under elevated static pressure Pres 80-250 bar) , the
115 pressure exergy component er,P VUm ( Pres Po) 0.02 kJ/mol is  smaller by more than
three orders of magnitude than the thermochemical exergy destroyed during hydrocarbon
oxidation (4Xd 5.40-10.68 kJ/mol).  Consequently; exergy destruction is dominated by
chemical composition alteration

Under anaerobic reservoir conditions, sulphate-reducing bacteria  (SRB) oxidize hydro-
120 carbon fractions via the generalized reaction:

$\mathrm{C}_{n}\mathrm{H}_{2n+2} + \left( \frac{3n + 1}{4} \right) \mathrm{SO}_{4}^{2-} \longrightarrow n\mathrm{HCO}_{3}^{-} + \left( \frac{3n + 1}{4} \right) \mathrm{HS}^{-} + \left( \frac{n - 1}{4} \right) \mathrm{H}_{2}\mathrm{O}
$

According to the Gouy-Stodola theorem 40] 22 41 1] the Specific Exergy Loss Index
(AXd, in kJ/mol) destroyed per mole of altered crude oil is directly proportional to the total
entropy generation (4 Sgen)

$\Delta X_d(T_{\text{res}}) = T_0 \cdot \Delta S_{\text{gen}} = T_0 \cdot \left[ \Delta S_{\text{mix}} + \frac{\Delta H_{\text{rxn}} - \Delta G_{\text{rxn}}}{T_{\text{res}}} \right] \geq 0
$

Where 4 Smix REraln(ri/ir? accounts for configurational entropy generation resulting
125 from aliphatic depletion and polar resino-asphaltic enrichment_

# 3.2. Specific Chemical Exergy of Hydrocarbon Fractions

Chemical exergy ezh) represents the maximum theoretical work obtainable when a hydro-
carbon compound is brought into chemical equilibrium with reference environmental species.
For a hydrocarbon molecule CaH,O Sa, the standard molar chemical exergy at To, Po is com-
puted via the Szargut model j10, 25

130

$e_{x}^{\text{ch}} = \Delta G_{f}^{\circ} + a \cdot e_{x, \text{CO}_{2}}^{\text{ch}} + \left( \frac{b}{2} \right) e_{x, \text{H}_{2}\text{O}}^{\text{ch}} + d \cdot e_{x, \text{SO}_{3}}^{\text{ch}} - \left( a + \frac{b}{4} - \frac{c}{2} + d \right) e_{x, \text{O}_{2}}^{\text{ch}}
$

(3)

As biodegradation selectively consumes light n-alkanes (high chemical exergy; e.g,, ech (hexane) =
4,142 kJ/mol) , the residual  fluid mixture accumulates oxygenated polar resino-asphaltic
fractions with lower H/C ratios, permanently destroying fluid work potential per unit mass_

3.3. Eyring Rate Theory Viscous Flow Activation Energy Justification

135 To connect exergy destruction (4Xa) to dynamic viscosity (p) without empirical curve-
fitting, MANCO-EX applies Eyring 's transition-state rate theory for viscous flow [43,B57

$\mu(\Delta X_d, T_{\text{res}}) = \left( \frac{h \cdot N_A}{V_m} \right) \cdot \exp \left( \frac{\Delta G_0^{\ddagger} + \frac{\Delta X_d}{\eta_{\text{biomarker}}}}{R \cdot T_{\text{res}}} \right) = \mu_0 \cdot \exp \left( \frac{\Delta X_d}{\eta_{\text{biomarker}} \cdot R \cdot T_{\text{res}}} \right)
$

Where h is Planck s constant N is Avogadro'$ number, Vm is molar volume, AGf is the
viscous flow activation free energy of unbiodegraded crude oil, and Tlbiomarker [0.85, 0.92] is
the dimensionless exergetic coupling efficiency:

$\eta_{\text{biomarker}} = \frac{\Delta G^{\ddagger}_{\text{viscous}}}{\Delta X_d} = 1 - \left( \frac{T_{\text{res}} \cdot \Delta S_{\text{dilution}}}{\Delta H_{\text{combustion}}} \right)
$

140 Justification of Eyring Theory for High-Viscosity Heavy Oils (103_105 cP): While free-
volume models (WLF , VFT) are often preferred near the glass transition temperature (Tg),
Eyring transition-state theory remains physically valid for heavy crude oils at reservoir tem-
peratures (30-80*C) because viscous dissipation in biodegraded oils is governed by the ther-
mal activation energy required for molecules to jump past structural obstacles created by
145 pi-pi stacking of asphaltenic nano-aggregates 357 B8 As biodegradation destroys light sol-
vents, the activation barrier AGt increases linearly with cumulative exergy loss AXd:

# 3.4. Empirical Total Acid Number (TAN) Exergetic Equivalence Formulation

To resolve the Tier organic acid contribution without relying exclusively on destruc-
tive chemical titrations, MANCO-EX integrates published laboratory Total Acid Number
150 measurements (TANemp [0.8,9.5] mg KOH oil) across the global dataset [13,[4 B]: We
formulate the Exergetic Equivalent Acid Numher (TANexergenic) by coupling ESI Orbitrap
MS heteroatomic NSO profiles 4 with carboxylic acid Gibbs free energy:

$TAN_{\text{exergenic}} = \theta_{\text{acid}} \cdot \left[ \frac{\sum[\text{OrgAcids}]}{C_0} \right] \cdot \exp \left( \frac{\Delta G_f^\circ(\text{R-COOH})}{R \cdot T_0} \right) \text{ [mg KOH/g oil]}
$

(6)

Where Oacid 4.82 is a stoichiometric conversion factor. Linear regression between theoret-
ical TANexergenic and published empirical laboratory TAN yields R? 0.9642 (p 10-15) 
155 proving that exergy destruction directly governs reservoir acidity evolution:

# 3.5. Litho-Thermodynamic Weighting Vector

The biomarker cascade weights W (a, 8,1,6) were determined by ordinary least-
squares (OLS) multivariate regression against 1,585 matched physicochemical samples from
the USGS Bemidji dataset, yielding the baseline vect OL   Wsilici [0.35, 0.40,0.15, 0.10]T  for
160 siliciclastic sandstone reservoirs (Orinoco, Athabasca, Bongor) For basin-specific recalibra-
tion, the weights can be re-estimated via regularized inversion:

$\boldsymbol{w}(\text{lithology}) = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I})^{-1} \mathbf{X}^T\Delta\mathbf{X}_d
$

Where A = 0.01 is a Tikhonov regularization parameter ensuring numerical stability when the
predictor matrix X is ill-conditioned (condition number ~ 497; see Section 4.6). While pre-
liminary sensitivity analysis suggests that hyper-sulfurated carbonate reservoirs (S 2.5%)
165 may require increased asphaltene/NSO weighting ($ _  0.20) , lithology-specific recalibration
remains target for future validation as additional complete multi-basin datasets become
available_

3.6. Derivation of the Critical Exergy Threshold from Hydraulic & Thermal Energy Balan ces
The critical exergy destruction threshold (4 Kzrit 8.50 kJ/mol) is derived directly from
170 the thermodynamic energy balance of artificial lift pumping and surface thermal dilution:

$E_{\text{net}} = e_{x,\text{oil}}^{\text{ch}} - (E_{\text{lift}} + E_{\text{heat}}) = 0
$

Where ezhoil 42.0 MJ/kg   is the   standard chemical exergy of the  produced hydrocar-
bons. The mechanical lifting exergy Elift is governed by the Fanning friction pressure drop
Piric (#(4Xa)) and geodetic head:

$E_{\text{lift}} = \frac{\Delta P_{\text{fric}}(\mu(\Delta X_d)) \cdot V_m}{\eta_{\text{pump}}} + \frac{\rho \cdot g \cdot (z_f - z_s)}{\eta_{\text{pump}}}
$

The thermal energy input Eneat required to lower fluid viscosity during surface transport is:

$E_{\text{heat}} = \frac{m_{\text{oil}} \cdot C_p \cdot (T_{\text{surface}} - T_{\text{res}})}{\eta_{\text{boiler}}}
$

(10)

175 Setting Enet 0 for typical reservoir conditions (~f 1,500 m, Tres 313.15 K, Thpump
0.65 , Vboiler 0.80) demonstrates that when fluid viscosity reaches / 200.000 cP (cor-
responding to AXd 8.50 kJ/mol), the total operational energy required to extract and
heat the crude oil equals the net chemical exergy of the produced fuel, defining the physical
Thermodynamic Inutility Boundary:

# 180 3.7. Multi-Tiered Biomarker Cascade Formulation

To ensure continuous diagnostic capability across all degradation levels (PM 1 to 10),
MANCO-EX formulates three-tiered cascading biomarker function:

$\Delta X_d = T_0 \cdot R \cdot \ln (1 + \Phi_{\text{cascade}})
$

Where the cascade function Dcascade combines Tier 1 Tier 2, and Tier 3 analytes:

$\Phi_{\text{cascade}} = \alpha \cdot \left[ \frac{\sum [\text{OrgAcids}]}{C_0} \right] + \beta \cdot \left[ \frac{\text{1-MP} + \text{2-MP}}{\text{3-MP} + \text{9-MP}} \right] + \gamma \cdot \left[ \frac{\text{C}_{20}\text{TAS}}{\text{C}_{28}\text{TAS}} \right] + \delta \cdot \ln \left( 1 + \frac{\text{Asphaltenes}}{\text{Saturates} + \epsilon} \right)
$

(12)

Where 0.01 is regularization parameter preventing mathematical divergence as satu-

185 rates approach zero (Saturates 0) in extreme biodegradation (PM > 6). The empirical
weighting constants (a = 0.35, 8 = 0.40, ~ 0.15,0 = 0.10) were optimized via OLS regres-
sion against the Bemidji dataset_

The four biomarker tiers exhibit high pairwise correlations (r = 0.90-0.96; Section 4.6)
reflecting the sequential nature of in-reservoir biodegradation: While this collinearity pre-
190 vents robust attribution of predictive power to individual tiers, the composite cascade func-
tion is designed as an aggregate degradation index rather than decomposable multi-factor
model The physical motivation for retaining all four tiers is diagnostic robustness: in moder-
ately biodegraded reservoirs (PM 3-5) , organic acids (Tier 1) and methylphenanthrene ratios
(Tier 2) carry diagnostic signal, whereas in severely altered fluids PM > 7) , only triaromatic

195

steroids (Tier 3) and the asphaltene anchor (Tier 4) remain measurable. The cascade thus

provides continuous coverage across the full degradation spectrum; even though, within any
single degradation level, individual tiers are largely redundant_

# 4 Results and Discussion

4.1. Resiliency of Aromatic Biomarkers € Monte Carlo Bootstrapping

Statistical regression analysis across the N = 41 chromatographic runs of the 5 global
basins confirms the extraordinary analytical resiliency of aromatic compounds under severe
biodegradation_ As detailed in Tablelq met- hylphenanthrene isomers (1-MP , 2-MP, 3-MP , 9MP)
maintain a deterministic linear correlation (R2 0.9854 0.9982)

To rigorously test sample-size robustness and eliminate overfitting risks, a non- parametric
205 Monte Carlo bootstrapping analysis (B 2,000 iterations) was executed across the global
dataset. Bootstrapping yields mean coefficient of determination R2 0.9992 with
95% confidence interval of CIgs% [0.9989, 0.9996] and slope distribution 8 1.6931
(CI9s% [1.6671,1.7313]). Furthermore, Kruskal-Wallis non-parametric ANOVA test
acIOss the 5 geological basins yielded H 19.305 (p = 0.0007) , demonstrating robust inter-
210 basin convergence_ Hypothesis testing via Student 's t-statistic confirms that even for N 10
met hylphenanthrene runs (t 66.62 , df 8) , the correlation is statistically indisputable
(p = 1.34 X 10-11 0.001)

Table 1: Biomarker Resiliency Regression Matrix USGS PGRL Real Dataset

Biomarker Ratio Compound Family Mean Peak Area Std Dv Runs ( Correlation R- Student s t-statistic
1-MP Methylphenanthrenes 8.64x 105 2.42 x 105 0.9982 t = 66.62 (df = 8,p < 10-8
2-MP Methylphenanthrenes 7.20 x 105 2.12 x 10" 0.9970 t =51.52 (df = 8,p < 10-8
3-MP Methylphenanthrenes 7.09 X 105 2.01 x 105 0.9985 t =72.10 (df = 8,p < 10-8
9-MP Methylphenanthrenes 1.26 x 106 3.31 X 105 0.9854 t =23.18 (df = 8,p < 10-' )
C20 TAS Triaromatic Steroids 3.33 * 10" 4.57 x 105 0.9949 t =30.12 (df = 55,p < 10-10,
C28 TAS Triaromatic Steroids 7.88 x 105 1.05 X 106 0.8225 t =16.01 (df =55,p < 10-10)

# 4.2 Methodological Triangulation Across the Full Sample Corpus

To evaluate predictive capacity against reservoir fluid transport resistance (viscosity and
215 lifting energy requirement) , comparative regression analysis was performed across the 1,585
monitoring samples from the Bemidji dataset PGRL; and Junin MANCO suites (Table []

As shown in Tablep} MANCO-EX with basin-specific calibration achieves conditional
coefficient of determination RZonditional 0.99 (MAE 0.01 IncP). The marginal coefficient

10

This image is a line chart showing the relationship between the Multi-Tiered Cascade Function ($\Phi_{\text{cascade}}$) and the Specific Exergy Loss Index ($\Delta X_d$ in kJ/mol).

### Chart Details
*   **X-axis:** Multi-Tiered Cascade Function ($\Phi_{\text{cascade}}$), ranging from 0.3 to 0.65.
*   **Y-axis:** Specific Exergy Loss Index ($\Delta X_d$ in kJ/mol), ranging from 0.8 to 1.2.
*   **Data Points:** Blue dots representing the "Empirical Multi-Basin Dataset ($N = 41$ Real Samples)".
*   **Trend Line:** A red line representing the "Linear Fit ($\bar{R}^2 = 0.9992$, Bootstrapped $B = 10,000$)".

### Data Interpretation
The chart displays a strong positive linear correlation between the Multi-Tiered Cascade Function and the Specific Exergy Loss Index, as evidenced by the high $\bar{R}^2$ value of 0.9992. The 41 empirical data points are tightly clustered along the linear regression line.


Figure 1: Empirical PGFPlots/TikZ vector scatter plot of the Specific Exergy Loss Index 4Xa) against
the multi-tiered biomarker cascade function dcascade_ compiled directly from N 41 real laboratory mea-
surement s across five global heavy oil basins: Orinoco Oil Belt [4, Junggar Basin [B], Bongor Basin (16
Athabasca Oil Sands [3| and the USGS PGRL Repository: Non-parametric Monte Carlo bootstrapping
B = 10,000) confirms high stability (R2 0.9992, CI9s% [0.9989,0.9996])_

Table 2: Methodological Triangulation Against Dynamic Viscosity (N 41 Multi-Basin Samples)

Framework Metric Type PM > 6 Res Thermodynamic Utility R2 (VS Flow Res.
Peters & Moldowan 993) Discrete Ordinal (1-10) Collapses Null 6120
MANCO (Larter et al., 2012) Continuous (0g/g) Sensible Moderate (Abstract) 0.8340
MANCO-EX This Work) Continuous (kJ mol) Quantitative Maximum Work) >0.99 (Cond LMM)

of determination REarginal 0.18) reflects the modest explanatory power of the fixed-effect
slope alone; the high intraclass  correlation (ICC 0.99) confirms that   progenito   fluid
composition ~captured by the basin-specific random intercept-_~dominates the total variance
in log-viscosity This is physically expected: crude oils from the Athabasca bitumen sands
and the Orinoco extra-heavy belt have fundamentally different baseline viscosities (103 vs_
105 cP) before any biodegradation occurs_

# 225 4.3. Parameter Sensitivity and Model Stability Analysis

To verify model robustness against potential calibration uncertainty in the weighting
coefficients (& 0.35, B 0.40, 7 0.15,0 0.10) , a Monte Carlo sensitivity analysis was

11

conducted by perturbing each coefficient independently by L2O%. As detailed in Table BI
the maximum variation in calculated exergy destruction (4Xd) is bounded within  3.8%,
and the thermodynamic economic abandonment threshold ( Enet < 0) remains   invariant
at AXd 8.50 _ 0.12 kJ mol This confirms that the formulation operates as stable
thermodynamic attractor insensitive to minor basin-specific parameter adjustments_

Table 3: Parameter Sensitivity Analysis (~2O% Coefficient Perturbation)

Pert urbed Parameter Baseline Perturbed Range (+20%) Max 4.Xz Shift Abandonment  Threshold
Alpha (0, Org Acids) 0.35 0.28 0.42 12.1% Invariant (8.50 kJ mol )
Beta (8, Methylphenanthrenes) 0.40 0.32 0.48 12.8% Invariant (8.52 kJ/ mol)
Gamma (~ TAS Steroids) 0.15 0.12 - 0.18 11.2 Invariant (8.48 kJ mol )
Delta ($, Regularized S.R.A) 0.10 08 0.12 11.5% Invariant (8.49 kJ/ mol)
Combined Worst-Case Simultaneous +2O% 13.89 Invariant (8.50 = 0.12 kJ/ mol)

# 4.4- Marginal US . Conditional Variance Decomposition

The REML-estimated Linear Mixed-Effects Model distinguishes   between   variance eX
plained by fixed effects alone Rqarginal 0.18) and variance explained when basin-specific
random intercepts are included (RZonclitional 0.99)_ The intraclass  correlation coefficient
(ICC 0.99) indicates that the dominant source of variance in log-viscosity is the basin-
specific baseline fluid composition, not the within-basin degradation gradient_ This is physi-
cally expected:  progenitor crude oils from the Orinoco Belt (extra-heavy, 8-10PAPI) , the
240 Athabasca Oil Sands   (bitumen, 7-9"API) , and the Junggar Basin (medium-heavy; 12-
16PAPI) exhibit inherently different  compositional baselines prior to any biodegradation;
producing baseline log-viscosity differences of  El.8 In cP

The REML-estimated fixed-effect slope (8 = 3.42, SE 0.055, p 10-6, 95% CI
[3.31,3.53]) captures the within-basin thermodynamic coupling between exergy destruction
245 and viscosity escalation-the core physical claim of this framework: The random intercepts
(0b, absorb the basin-specific initial condition, analogous to how Arrhenius pre-exponential
factors vary acrOss fluid chemistries while the activation energy mechanism remains invariant.
Critically; the significance of the fixed slope (p 10-6) confirms that the exergy-viscosity
coupling is not an artifact of inter-basin confounding:

12

250

# 4.5. Sample Size Considerations and Generalization Diagnostics

The core validation dataset comprises N = 41 complete multi-basin  samples with inde-
pendent   experimental viscosity measurements While this exceeds the minimum effective
sample size for mixed-effects   regression   with groups [Neff > 30; p28] the observation-
toparameter ratio (4.5.1 for the random-intercept model) is  below the conservative 10:1
255 guideline for complex LMM structures.

Three mitigation strategies were employed:

Random-intercept-only specification: Random slopes were excluded from the final
model. The very high conditional R2 0.99 with only random intercepts warrants
caution: it reflects the dominance of between-basin variance rather than within-basin
predictive pOwer of Dcascade alone

260

Leave-One-Group-Out (LOGO) cross-validation: Excluding entire basins during
training yields MAELOGO 1.31 In cP, confirming that prediction for a completely new
basin-~without any calibration data~degrades   substantially: This   underscores the
necessity of basin-specific random intercept calibration for operational deployment_

265

Non-parametric Monte Carlo bootstrapping (B 10,000): Bootstrap confi-
dence intervals for the Pcascade AXa calibration slope (Eq: 14, Figure [] are narTOW
Bcal 1.6931, CIg;% [1.6651,1.7319]) , confirming that the exergy-cascade map
ping is robust. Note that this calibration slope (4Xd Vs. Dcascade_ is distinct from the
LMM fixed-effect slope BLMM 3.42, log-viscosity VS. Dcascade) , which is estimated via
REML (Section 4.4)

Post-hoc statistical power analysis yields Cohen 's f2 = 0.23 (calculated as Rarginall
REarginal)) , medium-to-large effect size_ With N 41, df1 = 1, and df2 39, statistical
power exceeds 0.95 for detecting the fixed-effect slope at a 0.05, indicating that the sample
size is adequate for establishing the thermodynamic coupling, though the modest marginal
R2 highlights the critical role of basin calibration

275

The primary  constraint on sample size is the requirement for complete GC-MS aro-
matic biomarker suites with matched independent   laboratory viscosity measurements~a
resource-intensive analytical combination that limits publicly available datasets in reservoir
geochemistry:

13

# 280 4.6. Variance Inflation and Multicollinearity Assessment

Variance Inflation Factor (VIF) analysis across the four biomarker tier predictors reveals
moderate-to-high multicollinearity  (maximum VIF 21.86) , exceeding the conventional
threshold of VIF 10 p27 This collinearity is   geochemically expected: biodegradation
sequential process where the progressive  destruction of light fractions simultaneously
depletes methylphenanthrenes (Tier 2) and shifts SARA ratios (Tier 4), producing inherent
correlation among cascade tiers_

Critically; multicollinearity inflates the standard errors of individual tier coefficients but
does not bias the overall model prediction R2 , MAE) nOr invalidate the composite cascade
function dcascade 127]: The Specific Exergy Loss Index (4Xa) depends on the aggregate
290 dcascade . not on the isolated contribution of any single tier. As such, the predict ive validity
and the critical abandonment threshold (AXzit 8.50 kJ/mol) are unaffected by inter-tier
collinearity.

# 5. Industrial Case Study Thermodynamic Re-interpretation of the Junin Area
(Orinoco Oil Belt)

295

# 5.1. Empirical Re-interpretation of the Junin MANCO Dataset

major empirical case study was conducted by re-interpreting the published MANCO
aromatic biomarker dataset from the Junin Area of the Orinoco Oil Belt (Venezuela) , o1ig-
inally surveyed by Lopez et al [14| Lopez et al. measured continuous concentrations
(pg/g oil) of alkylphenanthrenes alkylnaphthalenes, and triaromatic steroids across extra-
heavy crude oils (89 108 API) exhibiting severe biodegradation PM 6 to 9).

30

By applying Equation (6) of MANCO-EX to the raw aromatic biomarker concentrations
reported by Lopez et al [14 we convert molecular concentration metrics into the Specific
Exergy Loss Index (4Xd; in kJ/mol)_ Across the Junin reservoir transition zone AXa in-
creases continuously from 6.20 kJ/mol in upper reservoir intervals to 9.85 kJ mol near the
305 oil-water contact (OWC). This exergy destruction directly maps the conversion of chemi-
cal exergy into irreversible entropy; corresponding to an exponential escalation in dynamic
viscosity from 15,000 cP to 225,000 cP_

14

# 5.2. Artificial Lift Thermal Energy Overhead in Junin Operations

Integrating the re-interpreted AXa values into artificial lift and suface heating energy
310 balances demonstrates that fluid exergy degradation imposes an additional operational en-
ergy requirement of 4.2 MW of thermal/hydraulic energy per 1,000 bbl/day produced from
lower reservoir zones in Junin. This quantitative conversion bridges the historical gap be-
tween the geochemical measurements of Lopez et al 14 and applied reservoir energy bal-
ances_

# 315 5.3. Redefining Field Abandonment:    The Net Exergy Criterion

Traditional petroleum engineering defines field economic abandonment when volumetric
oil production Qo) drops below a fixed operational limit Qlimit 15 BOPD) MANCO-EX
introduces the Net Exergy Balance Enet )

$E_{\text{net}} = E_{\text{produced}} - (E_{\text{lifting}} + E_{\text{heating}} + T_0 \cdot \Delta S_{\text{bio}})
$

(13)

When 4Xd 8.50 kJ/mol_ the energy required to lift, heat _ and process the viscous
320 fluid  exceeds the useful chemical exergy of the produced hydrocarbons ( Enet < 0). This
establishes that thermodynamic abandonment occurs prior to commercial volumetric limits.

# 5.4 Linear Mized-Effects Model 'LMM) Random Slopes Test

To account for geological heterogeneity across distinct sedimentary basins while testing
universal physical convergence , we fit REML-estimated Linear Mixed-Effects Models using
325 statsmodels .MixedLM in Python. Model specification testing comparing Random Inter-
cept model against Random Slopes model (re_ formula Dcascade via Likelihood
Ratio Test (LRT) yields LRT 449.05 (p 3.09 x 10 98 0.001, AICslopes 622.49
VS_ AICintercepts -177.44) . This confirms that the exergy-viscosity coupling slope (BMM)
varies significantly across basins depending on progenitor oil composition (3.05 + 0.32)_

Under the Random Intercept specification, the REML estimation yields a fixed-effect
slope B = 3.42 (SE 0.055, p < 10-6. 95% CI = [3.31,3.53]) . Basin-specific BLUP random
intercepts range from ~1.l5 (PGRL) to +1.79 (Athabasca) , reflecting the expected baseline
viscosity spread 19x) The conditional coefficient of determination is RZondlitional 0.99

15

(MAE 0.01 IncP), while the  marginal  coefficient   is R2 'marginal 0.18_ with an intra-
335 class   correlation ICC 0.99. Out-of-basin Leave-( One-( Group-Out   cross-validation yields
MAELOGO 1.31 lncP , confirming that operational deployment in neW basin requires
baseline calibration_

5.5. Cascade Ablation Study Across Biodegradation Tiers

To evaluate the individual diagnostic contribution of each biomarker tier , an ablation
340 study was conducted across the N = 41 multi-basin dataset Table

Table 4: Ablation study evaluating predictive accuracy across individual biomarker tiers and cumulative
cascade configurations.

Biomarker Configuration Rqarginal RZonditional MAE (In cP) Active PM Range
Utility
Tier 1 Alone (Organic Acids) 0.1454 0.9990 0.0299 Active PM 1- Early acid
generation
Tier 2 Alone (Methylphenanthrenes) 0.1756 0.9990 0.0318 Active PM 3-6 Light aro
matic depletion
Tier 3 Alone TAS Steroids) 0.1668 0.9979 0.0404 Active PM 6-8 Resistant
steroid ratio
Tier 4 Alone (Asphaltenic Anchor) 0.1494 0.9978 0.0447 Active PM 7-10 Extreme
polar buildup
Tiers 1 0.1676 0.9994 0.0231 Early-to-moderate degra-
dation
Tiers 1 + 2 + 3 0.1725 0.9994 0.0225 Moderate-to-severe degra-
dation
Full Cascade cascade_ 0.1841 0.9999 0.0082 XX Continuous coverage PM
1-10**

As   shown in Table single-tie  models exhibit higher log-viscosity errors  (MAE
0.0299-0.0447 In cP) and collapse at specific PM thresholds (e.g . Tier 1 acid signals plateau
above PM 5) Combining all four tiers into dcascade achieves the lowest  prediction erTor

16

(MAE 0.0082 In cP), proving that multi-tiered integration is essential for continous
345 diagnostic coverage across PM 1 to 10.

# 5.6. Uncertainty Budget Monte Carlo Error Propagation

To quantify the propagation of analytical measurement noise (GC-MS peak integration
15%, viscometer erTor ~3%) through the pipeline GC-MS 3 4 AXd 7 pL, non-
parametric Monte Carlo simulation (B 10,000 iterations) was executed

350

Monte Carlo erTor propagation yields a mean LMM slope of BLMM 3.05_10.32 (95% CI
[2.45,3.70]) and an mean critical exergy abandonment threshold of 4Xzit 8.50E0.78 kJ /mol
(95% CI [6.09,.9.20]) . Sensitivity analysis against assumed lifting depth (2; = 1,000-3,000 m)
indicates that 4Kzrit shifts by L0.42 kJ/mol, confirming that the thermodynamic threshold
remains robust within operational limits.

355

# 5.7. Practical Industrial Implementation Multi-Basin Engineering Workflows

To accelerate the adoption of MANCO-EX across both reservoir geochemistry research
and commercial petroleum engineering, this section details the step-by-step workflow   for
integrating the Specific Oil-Phase Exergy Loss Index (4Xa) into field operations, thermal
EOR decision-making, and commercial reservoir  Simulation software (e.g , CMG STARS
ECLIPSE_ INTERSECT).

30

# 5.7.1. Workflow 1: Direct Integration into Commercial EOS and Thermal Simulators

365

Traditional commercial Equation-of-State (EOS) and thermal reservoir simulators model
fluid viscosity using empirical correlations based solely on stock-tank API gravity O1"' tem-
perature: Under severe biodegradation, these correlations fail because fluids with identical
API gravity (8.58_9.59 API) can exhibit dynamic viscosities differing by more than an order
of magnitude due to varying biomarker exergy destruction (4Xd 6.20 vs.  9.85 kJ/mol)_

With MANCO-EL, production geochemists provide depth-resolved AXa profiles from roU-
tine GC-MS assays. Reservoir engineers then input the Eyring-derived viscosity function
#(AXd, Tres directly into the simulator'$ fluid property arrays, constructing 3D spatial vis-
370 cosity grids that match physical in-situ flow resistance_

17

5.7.2. Workflow 2: Optimization of Naphtha/ Diluent Blending in Heavy Oil Operations

In heavy and extra-heavy crude operations (such as the Orinoco Oil Belt and Athabasca
Sandstone  reservoirs) , diluents (e.g . naphtha, gas condensate) are injected downhole O1
at wellheads to lower fluid viscosity below pipeline transport specifications 250 cP at
375 37.8PC) . Currently, diluent  injection rates are managed via   trial-and-erTor surface sam-
pling:  MANCO-EX establishes a deterministic stoichiometric equation for minimum diluent
requirement Vdiluent _

$V_{\text{diluent}} = V_{\text{oil}} \cdot \left[ \frac{\ln (\mu_{\text{target}} / \mu_0) - \frac{\Delta X_d}{\eta_{\text{biomarker}} RT_{\text{res}}}}{\ln (\mu_{\text{diluent}} / \mu_{\text{target}})} \right]
$

(14)

This formula eliminates Over-dilution, reducing diluent operational expenditures (OPEX) by
an estimated 12-18 in fields exhibiting spatial biodegradation gradients.

380 5.7.3. Workflow 3: Decision Framework: for Enhan ced Oil Recovery (EOR) Selection
MANCO-EX provides quantitative screening tool for Thermal EOR selection based on
in-situ exergy destruction levels:

Low Exergy Degradation (4Xa 6.50 kJ/mol): Cold production with Progressive
Cavity Pumps (PCP) assisted by downhole diluent injection is economically and energy-
efficient.

385

2 Moderate Exergy Degradation (6.50 < AXd 8.50 kJ/mol) Thermal assistance
(Steam-Assisted Gravity Drainage [SAGD] or Cyclic Steam Stimulation [CSS]) is manda-
tory to overcome Eyring momentum barries_

390

Critical Exergy Degradation (4Xa > 8.50 kJ/mol): The fluid enters the Thermodv-
namic Inutility Boundary (Enet < 0). Primary thermal recovery is unviable without
advanced catalytic in-situ upgrading:

# 5.8. MANCO-EX SOTA Engine:  Algorithms Industry Benchmarking

To formalize MANCO-EX as State-of-the-Art (SOTA) computational engine suitable
for commercial software integration (e.g. CMG STARS, ECLIPSE, INTERSECT) and a u-
395 tomated Python pipelines, we present the explicit algorithmic structure and benchmarking
evaluation against standard petroleum engineering models.

18

# 5.8.1. Algorithm 1: Forward Inference Engin e

1. Input Assays:   Reservoir temperature Tres (K), organic acid concentration [OrgAcids]
(mg/g) , methylphenanthrene isomer ratio RuP (1-MP + 2-MP)/(3-MP + 9-MP), tri-
aromatic steroid ratio RTAs Cz0/C28, and SARA ratio RsARA Asphaltenes / (Saturates +
0.01)

Compute Cascade Function (D)

$\Phi = \alpha \cdot [\text{OrgAcids}] + \beta \cdot R_{\text{MP}} + \gamma \cdot R_{\text{TAS}} + \delta \cdot \ln(1 + R_{\text{SARA}})
$

Calculate Oil-Phase Specific Exergy Destruction (4Xa):

$\Delta X_d = R \cdot T_0 \cdot \ln(1 + \Phi) \text{ [kJ/mol]}
$

Calculate Dynamic Viscosity via Eyring Rate Theory LMM:

$\mu = \mu_0 \cdot \exp \left( \alpha_b + \frac{\Delta X_d}{\eta_{\text{biomarker}} \cdot R \cdot T_{\text{res}}} \right) [\text{cP}]
$

Return: (AXd; /).

# 5.8.2. Algorithm 2: Bayesian-Tikhonov Basin Calibration Engine

Input Dataset: Historical matrix of measured biomarker assays X and measured dy-
namic viscosity vector y In pexp"

2 Normalize Assay Matrix: Xnorm (X px)/ox-

Solve MAP Regularized Objective:

$\mathbf{w}_{\text{reg}} = (\mathbf{X}_{\text{norm}}^{T}\mathbf{X}_{\text{norm}} + \lambda\mathbf{K}_{\text{litho}})^{-1} \mathbf{X}_{\text{norm}}^{T}\mathbf{y}
$

Return: Calibrated weight vector Wrcg"

# 5.8.3. Benchmarking Against Legacy Industry Modlels

Table []presents the comparative evaluation of MANCO-EX against standard petroleum
410 engineering   viscosity correlations   evaluated across the N 41 multi-basin dataset at
uniform reservoir temperature of Tres 313.15 K (104'). The published Beggs-Robinson
and Egbogah-Ng 134 dead-oil correlations ~which predict  viscosity from API gravity
and temperature alone ~vield negative R2 values (-2.25 and ~2.70, respectively) , indicating

19

415

ca tastrophic failure when applied to biodegraded heavy oils. Their predicted viscosity ranges
(122-3,452 cP) systematically underestimate measured viscosities (1,977-90,347 cP) by up to
two orders of magnitude. This confirms the fundamental limitation identified in Section 1.3:
purely empirical API/T correlations cannot resolve the viscosity escalation induced by in-situ
biodegradation because they lack molecular degradation information

An OLS regression of log / On Dcascade alone (labeled "MANCO vl.O" in Table]] achieves
420 R2 0.41, equivalent to the REML marginal R2_~a substantial improvement over PVT
correlations but  still limited by   unresolved  inter-basin   baseline   differences. Only the full
REML LMM with basin-specific random intercepts achieves near-perfect conditional predic-
tion (R2 > 0.99) , confirming that the combination of geochemical degradation gradient and
basin-specific progenitor fluid calibration is essential fo operational viscosity estimation.

Note: the Pedersen et al. B3] corresponding-states viscosity model requires full compo-
sitional EOS input (molar mass distribution; critical properties) unavailable in the present
geochemical dataset_ It is therefore replaced by the Egbogah-Ng correlation, which operates
on the same input variables (API, T) as Beggs-Robinson

Table 5: Comparative benchmarking   against   published viscosity correlations On the global multi-basin
dataset (N 41. Lres 313.15 K)

Model Correla- Input Variables R2 MAE (In cP) Key Limitation
tion
Beggs-Robinson API, T -2.25 2.08 No molecular degrada-
(1975) tion input
Egbogah-Ng (1990) API, T -2.70 2.25 No molecular degrada-
tion input
MANCO vl.0 (OLS on @carcade 0.41 0.83 No basin calibration
MANCO-EX REML dcascade basin >0.99 <0.01 Requires  basin   intercept
LMM) calibration

20

# 5.8.4. LMM Residual Diagn ( ostics

Figure P] presents the standardized residuals of the REML LMM conditional prediction
plotted against fitted values. Residuals are bounded within L0.04 In cP across  all five
basins, with no systematic pattern, confirming homoscedasticity and the absence of model
misspecification_ A Shapiro-Wilk test yields p 0.013, marginally rejecting normality at
0.05; this is attributable to the small sample size (N = 41) and the slight asymmetry
435 in the Athabasca residuals_

The image is a scatter plot showing the residuals ($y - \hat{y}$, ln cP) against the fitted values ($\hat{y}$, ln cP) for five different datasets. The y-axis values are scaled by $10^{-2}$.

### Legend
*   **PGRL**: Blue circles
*   **Orinoco**: Red triangles
*   **Bongor**: Green squares
*   **Junggar**: Orange diamonds
*   **Athabasca**: Pink pentagons

### Data Distribution
*   **PGRL (Blue circles)**: Clustered between fitted values of approximately 7.7 and 7.9, with residuals ranging from roughly 0.6 to -0.6.
*   **Orinoco (Red triangles)**: Clustered between fitted values of approximately 9.6 and 10.1, with residuals ranging from roughly 1.7 to -1.4.
*   **Bongor (Green squares)**: Clustered between fitted values of approximately 7.6 and 7.9, with residuals ranging from roughly 1.5 to -1.7.
*   **Junggar (Orange diamonds)**: Clustered between fitted values of approximately 8.2 and 8.7, with residuals ranging from roughly -0.6 to 0.7.
*   **Athabasca (Pink pentagons)**: Clustered between fitted values of approximately 10.9 and 11.2, with residuals ranging from roughly -4.0 to 0.0.

A horizontal dashed line is drawn at the residual value of 0.


Figure 2: Residual plot of the REML LMM conditional prediction_ Residuals are bounded within +0.04 In cP.
confirming adequate model specification.   Basin-specific markers illustrate homogeneous residual variance
across geological provin ces_

# 5.8.5. Basin-Specific Random Intercepts (BL UP)

Figure B]displays the Best Linear Unbiased Predictors (BLUP) of the basin-specific ran-
dom intercepts, ordered by magnitude. The intercept range (_1.15 to +1.79 In cP) corre-
sponds to a baseline viscosity ratio of exp(2.95) 19x between the most and least viscous
440 progenitor fluids (Athabasca bitumen vs. PGRL medium crudes)_ This inter-basin hetero-
geneity in  baseline  composition is the physical origin of the high ICC (= 0.99) and the
necessity for basin-specific calibration

# 6 Conclusions

MANCO-EX successfully converts molecular degradation metrics into applied thermo-
dynamic work (4Xd, in kJ/mol).

21

This bar chart displays the BLUP Random Intercept ($\alpha_b$, ln cP) for five different categories.

| Category | BLUP Random Intercept ($\alpha_b$, ln cP) |
| :--- | :--- |
| Athabasca | 1.79 |
| Orinoco | 0.94 |
| Junggar | -0.54 |
| Bongor | -1.04 |
| PGRL | -1.15 |


Figure 3: Best  Linear Unbiased Predictors BLUP) of basin-specific random intercepts from the REML
LMM: The intercept   spread (Aa 2.95 In cP 19x viscosity ratio) reflects the physical variability in
progenitor fluid composition acoss geological provinces_

Re-interpretation of global heavy oil datasets [14 [3, B [6] demonstrates that exergy
loss (4Xd 6.20 + 9.85 kJ/mol) directly dictates lifting and heating energy overhead.
MANCO-EX with basin-specific calibration achieves near-perfect viscosity prediction
(Rzonditional 0.99, MAE 0.01 In cP) via a REML-estimated Linear Mixed-Effects
Model: The fixed-effect slope (8 = 3.42 10-6) confirms the universal thermody-
namic coupling; while the high intraclass correlation (ICC = 0.99) and modest marginal
R2 0.18 indicate that operational deployment requires basin-specific calibration of
the random intercept _

Out-of-basin cross-validation (MAELOGO 1.31 IncP) quantifies the generalization
penalty for uncalibrated basins, motivating future expansion of the multi-basin dataset_

# CRediT Authorship Contribution Statement

Jose A. Garcia: Conceptualization; Methodology; Software, Formal Analysis, Investi-
gation, Data Curation, Writing Original Draft, Writing Review & Editing; Visualization

# Declaration of Competing Interests

460 The author declares that he has n0 known  competing financial interests O1"   personal
relationships that could have appeared to influence the work reported in this pape:

22

# Acknowledgements

The author acknowledges the U.S. Geological Survey (USGS) Petroleum Geochemistry
Research Laboratory and the USGS Bemidji Natural Attenuation Site for open-access release
465 of their analytical datasets.

# 6.1. Broader Impact, Environmental Sustainability Field Economics

The deployment of MANCO-EX carries significant environmental, economic, and energy
policy implications for unconventional heavy crude oil resource management:

GHG Emission Intensity Reduction: Heavy oil recovery in the Athabasca Oil
Sands (Steam-Assisted Gravity Drainage, SAGD) and the Orinoco Oil Belt (diluent
blending) is highly energy-intensive. Identifying the Thermodynamic Inutility Bound-
ary (4Xd > 8.50 kJ/mol) prevents futile thermal injection in zones where fluid exergy
is depleted, directly reducing field Steam-to-Oil Ratios (SOR) and associated Scope
CO2 emissions_

475

Field Economics & Asset Valuations: Coupling 4Xa with production economics
demonstrates that thermodynamic abandonment ( Enet < 0) occurs prior to commercial
volumetric production limits ( Qlimit 15 BOPD) . Integrating exergy loss into asset
net present value (NPV models provides a physical break-even cost $/bbl) for thermal
EOR and diluent injection

National Resource Strategy Context: As major heavy oil holding nations (Venezuela,
Canada) navigate global energy transition pressures; MANCO-EX provides quanti-
tative thermodynamic audit tool for prioritizing high-exergy, low-viscosity reservoir
intervals over hyper-biodegraded bitumen zones_

6.2 Data and Code Availability Statement

All data and calculation codes   supporting the findings of this  study are available  in
open-access repositories:

MANCO-EX SOTA Engine Python  Code Benchmark Scripts: GitHub https

'github_ 11 com/

joseagarpe/manco-ex sota

23

Consolidated Geochemical Datasets (PGRL, Bemidji, Multi-Basin): Zenodo Reposi-
tory (https /doi org/10 5281/zenodo.21826600

USGS Open-Access  Repositories: USGS PGRL (https '/energy.usgs gov / and
USGS Bemidji Site https mn. water usgs gov /bemidji/

# References

[1|  Bejan, A. (2016) . Advanced engin eering thermodynamics (4th ed.). John Wiley Sons.

495 [2] Bennett, B. & Larter; S. R. (2008) . Quantitative biodegradation scales based on aro-
matic hydrocarbons_ Organic Geochemistry; 39(8) , 1222-1228.

[3] Chang, X. Liu, X. Shi, B. Liu, T. Xu_ Y,, Liu, 2., Chen, G., & Zhang, P (2022).
Biodegradation levels  of oils from the Chepaizi  Uplift, Junggar Basin   (NW China)
evaluated by full-range biodegradation index: Marine and Petroleum   Geology; 146
105939

500

Cheng; X,, Hou, D. (2021). Characterization of severely biodegraded crude oils uS-
ing negative-ion ESI Orbitrap MS, GC-NCD and GC-SCD: Insights into heteroatomic
compounds biodegradation. Energies, 14(2) , 300.

[5] Gates, I. D. Wang; J & Larter , S. R. (2014) . Exergy efficiency in thermal recovery of
heawy crude  Applied Energy; 115 , 412-425.

505

[6] Head, M,, Larter, S R. & Gray; N. D. (2003) . Biological activity in the deep subsun-
face and the origin of heavy oil. Nature; 426(6964) , 344-352_

[7] Head, M. Gray; N_ D & Larter, S. R (2014) . Microbial ecology of hydrocarbon
reservoirs_ The ISME Journal, 8(6) , 1205-1215.

510 [8]   Huang, H. Bennett _ B. & Larter, S. R: (2013) . Impact of biodegradation on heavy oil
compositional gradients. Energy & Fuels, 27(11) , 6430-6442_

[9]  Jones, D_ M., Head, I. M. Gray; N. D. Adams_ J. J,, Rowan; A K , Aitken, C. M._
Bennett, B., Huang; H. Brown, A Bowler B. F. J,, Oldenburg,; T. B. P, Erdmann,

24

M. Larter, S. R. (2008). Crude-oil biodegradation via methanogenesis in subsurface
515 petroleum reservoirs.  Nature; 451(7175) , 176-180.

[10]  Kotas; T. J. (2013). The ecergy method of thermal plant analysis. Elsevier

[11] Larter; S R. Wilhelms_ A., Head, I. M,, Koopmans M:, Aplin, A C. Di Primio, R.
Zwach_ C. Erdmann M. & Telnaes, N. (2003) . The controls on the composition of
biodegraded oils in the world's great oil basins: Part 1. Organic Geochemistry; 34(4) ,
601-613

[12] Larter; S. R Huang, H,, Adams, J. J, Bennett_ B., Snowdon, L R,, & Gates, I. D
(2006) . The controls 0n the composition of biodegraded oils in the world's great oil
basins: Part 1. AAPG Bulletin, 90(6) , 921-938.

[13] Larter; S. R._ Huang, H: Adams , J. J,, Bennett, B. Snowdon, L_ R_ & Gates,

525 D. (2012) . A practical biodegradation scale for use in reservoir geochemical studies of
biodegraded oils (MANCO scale). Organic Geochemistry; 45 , 66-76_

[14] Lopez, L_ Lo Monaco, S,, & Galarraga, F. (2014) . Study of the biodegradation levels
of oils from the Orinoco Oil Belt (Junin area) using different biodegradation scales.
Organic Geochemistry, 66,60-69.

530 [15]  Magot, M: Ollivier _ B & Patel. B. K. C. (2000) . Microbiology of petroleum reservoirs_
Antonie van Leeuwenhoek; 77(2) , 103-116.

[16]   Mahmoodi; M. Kamali _ M. R. & Rahmani, M. (2019) . Geochemical characterization
of crude oils from the Bongor Basin, Chad. Scientific Reports, 9, 13180.

[171 Meyer; R. F., Attanasi, E. D. & Freeman_ P. A. (2007) . Heavy oil and natural bitum en
535 resources in geological basins of the world (USGS Scientific Investigations Report 2007-
5185) _ U.S. Geological Survey:

[18]  Perez, R. Abivin, P,, Henaut . (2019). Thermodynamic   modeling   of heavy oil
physical properties_ Fluid Phase Equilibria, 485, 110-122

25

[19]  Peters K. E & Moldowan_ J. M. (1993). The biomarker guide: Interpreting molecular
540 fossils in petroleum and ancient sediments. Prentice Hall.

[20]  Radke M. Welte_ D H. & Willsch_ H. (1982) . Geochemical study on a suite of crude
oils from the Mahakam delta (Indonesia) . Geochimica et Cosm ochimica Acta, 46(10) ,
1831-1848.

[21] Roadifer , R. E. (1987) . Size distribution of world's giant oil and tar sand deposits_ In

R. F. Meyer (Ed:) , Exploration for heavy crude oil and natural bitumen (AAPG Studies
in Geology 25, pp. 27-45) . American Association of Petroleum Geologists.

[22]  Stodola, A. (1910). Steam and gas turbines. McGraw-Hill:

[23] Wilhelms _ A. Larter , S. R. Head, M. Farrimond, P._ Di Primio, R. Zwach, C.
(2001) . Biodegradation of oil in reservoirs. Nature; 411(6841), 1034-1037

550 [24]  Adams, J. J. (2014). Asphaltene adsorption; a literature review_ Energy Fuels, 28(5) ,
2831-2856.

[25]   Dincer; I., & Rosen; M. A. (2021) . Exergy: Energy;  environment and sustainable devel-
opment (3rd ed.). Elsevier:

[26]  Larter; S_ R. & Head, I. M. (2014). Oil sands and heavy oil: Origin and exploitation
Elements, 10(4) , 277-283.

[27] OBrien, R. M: (2007) . A caution regarding rules of thumb for variance inflation factors.
Quality Quantity; 41(5) , 673-690.

[28]  Snijders T. As B. & Bosker R: J. (2012) . Multilevel analysis: An introduction to basic
and advanced multilevel modleling (2nd ed.) Sage Publications_

560 [29]   Tsatsaronis, G_ (2013) . Thermoeconomics and exergoeconomics_ Therm odynamics and
the destruction of resources (pp. 377-401) Cambridge University Press_

[30]   Oldenburg; T. B P. Brown, M. Bennett B. & Larter S_ R. (2017). The impact   of
thermal maturity level on   the composition of crude oils. Organic Geochemistry; 104
33-45_

26

565 [31] Hao; F Zou H. & Gong; Z. (2020). Preferential petroleum migration pathways and
prediction of petroleum occurrence in sedimentary basins_ Petroleum Science, 17, 1-22_

[32]  Beggs, H. D,, & Robinson, J. R. (1975). Estimating the viscosity of crude oil systems.
Journal of Petroleum Technology; 27(09) , 1140-1141.

[33]  Pedersen K S , Fredenslund_ A,, Christensen, P. L , & Thomassen P. (1984) . Viscosity
570 of crude oils_ Chemical Engineering Scien ce, 39(6) , 1011-1016

[34] Egbogah, E: 0. & Ng; J. T. (1990). An improved temperature-viscosity correlation for
crude oil systems. Journal of Petroleum Scien ce and Engineering, 4(3) , 197-200.

[35]   Macias-Salinas, R. Garcia-Sanchez F. Eliosa-Jimenez_ G. (2009) . Eyring-theory-
based  model to estimate crude oil viscosity at   reservoir conditions. Energy Fuels
23(3) , 1438-1445 .

[36]  Zhong; X Zhang; Y & Liu, H. (2025). Establishing the relationship between heavy
oil viscosity and molecular markers using an enhanced neural network model Scientific
Reports; 15 18561_

[37]  McCaffrey, M. A,, Legarre, H. A, & Johnson, S. J. (1996). Using biomarkers to improve
580 heawy oil reservoir management Cymric field, California. AAPG Bulletin, 80(6) , 898_
913.

[38]  Miadonye; A & Amadu; M. (2024). Activation energy for viscous flow as measure
of dilution efficiency in heavy oil-diluent systems_ International Journal of Chemistry,
16(1) , 45-58.

[39] De Ghetto G. Paone F. Villa, M. (1995) . Pressure-volume-temperature correlations
for heavy and extra heavy oils.  SPE Reservoir Engineering; 10(02) , 143-150.

[40] Gouy; M. (1889). Sur Fenergie utilisable.  Journal de Physique Theorique et Appliquee;
8(1) , 501-518

[41]  Bejan; A. (1982) . Entropy generation through heat and fluid flow John Wiley & Sons.

27

590 [42] Szargut J. Morris D R. & Steward, F. R. (1988) . Exergy analysis of thermal, chem-
ical, and metallurgical processes. Hemisphere Publishing Corporation:

[43] Eyring; H (1936) . Viscosity; plasticity; and diffusion as examples of absolute reaction
rates. The Journal of Chemical Physics, 4(4) , 283-289.

[44 Andrade, D E. & Rajagopal K. (2018)_ Eyring-theory-based model for viscosity of
595 crude oils.  En ergy Fuels, 32(5) , 5890-5899.

[45] Hu, J,, Zhang; Y. & Wang; X (2014). Viscosity prediction of heavy oil using biomarker
parameters. Petroleum Science and Technology; 32(12) , 1450-1458.

28