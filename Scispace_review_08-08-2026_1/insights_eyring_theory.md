## TL;DR

Eyring transition state theory (TST) has been widely used to model viscosity of hydrocarbons and crude oils by treating flow as an activated molecular jump; activation energies are linked to intermolecular interactions, free volume, or residual thermodynamic quantities. The supplied literature shows many Eyring-based viscosity models and composition-sensitive applications, but no direct examples combining Eyring viscosity models with biodegradation-driven molecular changes in the provided corpus.

----

## Eyring applications to viscosity

This section summarizes how Eyring TST and related significant‑structure or residual formulations have been implemented to predict viscosity across pure hydrocarbons, mixtures, heavy oils, and reservoir fluids. Examples include both empirical-modified Eyring correlations and theory-driven models that couple Eyring kinetics with equations of state or free‑volume theories.

- A number of practical viscosity models for crude and reservoir oils use Eyring’s absolute‑rate framework coupled with cubic equations of state to provide pressure‑ and temperature‑dependent viscosity predictions for dead-to-live oils with a small set of tuning parameters [1].  
- Generalized or modified Eyring expressions have been proposed to predict kinematic viscosity of petroleum fractions using reference fluids and simple descriptors such as molecular weight and true boiling point [2].  
- An Eyring‑based model was proposed specifically for paraffinic–naphthenic live crude oils and produced low average errors against measured undersaturated oil viscosities [3].  
- Entity‑based and Eyring–NRTL variants have been developed to handle complex mixtures such as oils and bitumens by combining Eyring kinetics with mixture interaction models [4].  
- The Eyring Significant Structure (ESS) approach has been combined with equilibrium statistical thermodynamics (Simha–Somcynsky) or free‑volume models to treat high‑molecular‑weight hydrocarbons and mixtures, using hole/fractional free volume as a key linking quantity [5] [6] [7] [8].  
- Experimental studies of mixtures (e.g., oil + refrigerant, oil + CO2) have used Eyring activation energies and excess activation terms to correlate nonideal viscosity behavior across temperature and concentration ranges [9] [10].

Table comparing representative Eyring applications

| Model or approach | System targeted | Key feature | Reference |
|---|---:|---|---:|
| Eyring + cubic EOS | Crude/reservoir oils | Thermodynamic properties from EOS feed Eyring framework | [1] |
| Modified Eyring fraction model | Petroleum fractions | Uses MW and TBP with two reference fluids | [2] |
| Eyring model for live crudes | Paraffinic–naphthenic oils | Low AAD for undersaturated viscosities | [3] |
| Eyring–NRTL entity model | Oils and bitumens | Mixture interaction + Eyring kinetics | [4] |
| ESS + SS or free volume | High MW hydrocarbons, mixtures | Hole fraction / free volume links equilibrium and transport | [5] [6] [7] |

----

## Basis linking activation energy to viscosity

This section outlines the theoretical rationale used in the literature to connect a molecular activation barrier to macroscopic viscosity in heavy oils. The linkage combines Eyring’s activated‑rate picture with thermodynamic or structural measures that quantify intermolecular cohesion and available free volume.

- Eyring TST conceptualizes viscous flow as an activated event in which a molecule must overcome an energy barrier to move into a neighboring site; the rate of these events determines macroscopic viscosity through an Eyring relationship between viscosity and the activation Gibbs free energy [11].  
- Classical implementations relate the activation energy for flow to a fraction of the energy of vaporization or to residual (nonideal) Helmholtz/Gibbs free energy compared with an ideal‑gas reference, so that cohesive intermolecular energy appears directly in the activation term [11] [1] [12].  
- Free‑volume and significant‑structure approaches treat the activated state as formation of a local vacancy or “hole”; the hole fraction or free volume computed from an equilibrium equation of state therefore provides the structural link between molecular packing and the activation barrier for flow [5] [6] [7] [8].  
- The kinetic compensation effect reported for multicomponent hydrocarbon media links changes in the Arrhenius pre‑exponential factor to changes in activation energy, providing an empirical constraint that ties molecular composition or topology to both barrier height and frequency prefactors in the Eyring form [13] [14].  
- Quantum and topological descriptors (for example, ionization potentials and Wiener indices) have been correlated empirically with the apparent activation energy of viscous flow, supporting mechanistic interpretations that dispersion and electronic factors influence the inter‑molecular interaction energy that appears in the activation term [13] [15].  
- Practically, models combine Eyring kinetics with thermodynamic input (EOS, residual Helmholtz energy, or experimentally derived free volume) so that activation parameters become functions of density, composition, and temperature, enabling prediction across reservoir conditions [16] [1] [2].

----

## Precedents and biodegradation

This section addresses whether Eyring approaches have been used together with composition changes specifically arising from biodegradation and notes analogous precedent studies that modulate composition.

- Insufficient evidence exists in the supplied literature for any study that explicitly couples Eyring‑based viscosity prediction to molecular composition changes caused by biodegradation; no papers in the provided corpus directly study biodegraded oils within an Eyring framework.  
- There are, however, multiple precedents for composition‑sensitive Eyring applications that are relevant and suggest feasibility: Eyring models applied to mixtures and binary/ternary systems with excess activation energies or concentration‑dependent activation terms have been used to capture nonideal viscosity changes upon dilution or blending [17] [9] [10].  
- Studies assessing dilution efficiency and activation energies for heavy oil–diluent systems treat changes in activation energy as a descriptor of composition‑driven viscosity reduction, illustrating how measured or modeled activation energies can reflect compositional modification [18].  
- Therefore, while the literature supplied shows established methods to make activation parameters composition‑dependent and to relate molecular descriptors to activation energy, direct published examples combining Eyring viscosity models with biodegradation‑induced molecular transformation are not present in this corpus; applying Eyring models to biodegraded compositions would be conceptually consistent with existing mixture and composition‑sensitivity approaches but represents a gap in the provided references.