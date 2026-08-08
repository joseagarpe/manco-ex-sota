## Detailed Analysis of the MANCO-EX Experimental and Dataset Specifications

### 1. USGS Bemidji Dataset Description and Usage
* **Description:** The USGS Bemidji Natural Attenuation Site Dataset is described as a 'multi-decadal monitoring corpus comprising 1,585 analytical samples tracking low-molecular-weight organic acid generation, SARA fraction shifts, and physical property variations resulting from crude oil biodegradation' [1]. The provenance of this dataset is clarified as representing 'a shallow pipeline spill into a glacial aquifer in Minnesota, USA' [1].
* **Explicit Use:** Because near-surface groundwater environments differ from deep petroleum reservoirs in pressure, temperature, and microbial consortia, the Bemidji dataset was 'utilized exclusively for calibrating the stoichiometric organic acid generation kinetics (α weighting coefficient in Tier 1)' [2]. It was explicitly 'not used for deep reservoir viscosity calibration' [2].

---

### 2. Description of the $N=41$ Reservoir Samples
* **Deep Reservoir Samples and Depth:** The $N=41$ samples are described as independent high-resolution GC-MS aromatic biomarker suites matched with laboratory-measured experimental viscosities from 'deep petroleum reservoirs' with a specified depth of '$z_f = 800\text{–}2,500$ m' [3].
* **Temperature and Pressure:** The dynamic viscosity measurements for these samples were conducted under 'atmospheric dead-oil conditions' (which defines the measurement pressure) at a standardized test temperature of '$T_{\text{res}} = 313.15$ K ($40.0^\circ$C, $104.0^\circ$F)' [4]. The manuscript separately notes that the actual deep reservoir fluids exist under elevated static pressures of '$P_{\text{res}} = 80\text{–}250$ bar' [5].

---

### 3. GC-MS Analytical Conditions
* **Instrument and Ionization:** Analyses were executed using an 'Agilent 6890N Gas Chromatograph coupled with a 5975C Mass Selective Detector (MSD)' operating in 'Electron Ionization (EI, 70 eV)' and 'Selected Ion Monitoring (SIM) mode' [6].
* **Column and Carrier Gas:** Separation was achieved using an 'HP-5MS fused-silica capillary column (30 m × 0.25 mm ID × 0.25 μm film thickness)' with 'Helium carrier gas at a constant flow rate of 1.0 mL/min' [6].
* **Temperature Program:** The oven temperature program was 'held at $50^\circ$C for 2 min, ramped at $4^\circ$C/min to $310^\circ$C, and held isothermally for 15 min' [6].
* **Internal Standard:** Aromatic biomarker ratios were quantified via peak area integration relative to 'deuterated internal standards ($d_{10}$-phenanthrene)' [6].

---

### 4. Viscometry Measurement Protocol
* **Protocol Details:** Independent dynamic viscosity measurements ($\mu$) for the $N=41$ multi-basin validation samples were conducted under 'atmospheric dead-oil conditions' at a standardized test temperature of '$T_{\text{res}} = 313.15$ K ($40.0^\circ$C, $104.0^\circ$F)' [4].
* **Instrument Type:** The measurements utilized a 'Haake RheoStress 600 rotational cone-and-plate viscometer' with a 'gap [of] 0.105 mm' and a 'shear rate range [of] $0.1\text{–}100\text{ s}^{-1}$' [4].

---

### 5. Data and Code Availability Statement
* **Statement:** Yes, the manuscript contains a dedicated section titled **'6.2. Data and Code Availability Statement'** which states: 'All data and calculation codes supporting the findings of this study are available in open-access repositories:' [7].
* **Repositories:** It lists the 'MANCO-EX SOTA Engine Python Code & Benchmark Scripts' on GitHub (`https://github.com/joseagarpe/manco-ex-sota`) [8], the 'Consolidated Geochemical Datasets (PGRL, Bemidji, Multi-Basin)' on Zenodo (`https://doi.org/10.5281/zenodo.21826600`) [9], and the 'USGS Open-Access Repositories' for the USGS PGRL and USGS Bemidji sites [9].

---

### 6. Broader Impact Section
* **Section Details:** Yes, there is a section titled **'6.1. Broader Impact, Environmental Sustainability & Field Economics'** [10]. It discusses the following key areas:
  * **GHG and SOR:** 'Heavy oil recovery in the Athabasca Oil Sands (Steam-Assisted Gravity Drainage, SAGD) and the Orinoco Oil Belt (diluent blending) is highly energy-intensive. Identifying the Thermodynamic Inutility Boundary ($\Delta X_d^{\text{crit}} > 8.50$ kJ/mol) prevents futile thermal injection in zones where fluid exergy is depleted, directly reducing field Steam-to-Oil Ratios (SOR) and associated Scope 1 $\text{CO}_2$ emissions.' [11]
  * **Economics ($/bbl):** 'Coupling $\Delta X_d$ with production economics demonstrates that thermodynamic abandonment ($E_{\text{net}} \le 0$) occurs prior to commercial volumetric production limits ($Q_{\text{limit}} \approx 15$ BOPD). Integrating exergy loss into asset net present value (NPV) models provides a physical break-even cost ($/bbl) for thermal EOR and diluent injection.' [12]
  * **National Resource Strategies:** 'As major heavy oil holding nations (Venezuela, Canada) navigate global energy transition pressures, MANCO-EX provides a quantitative thermodynamic audit tool for prioritizing high-exergy, low-viscosity reservoir intervals over hyper-biodegraded bitumen zones.' [13]