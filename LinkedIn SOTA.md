NUEVO MARCO SOTA EN TERMODINÁMICA Y GEOQUÍMICA DE CRUDOS EXTRAPESADOS (MANCO-EX v3.1)

Presento la versión v3.1 del marco metodológico MANCO Exergetic Framework (MANCO-EX), publicado como Preprint Oficial en la red de investigación de Elsevier (SSRN Abstract ID: 7243483).

Hasta hoy, la caracterización de la degradación en crudos pesados dependía de escalas cualitativas como la de Peters & Moldowan (1993), que falla en PM > 6 por agotamiento de saturados, o de la escala molecular continua MANCO de Larter et al. (2012). Sin embargo, aunque la escala MANCO revolucionó la geoquímica al medir concentraciones aromáticas (μg/g oil), persistía una brecha fundamental: los ingenieros de yacimientos no podían ingresar métricas de concentración molecular en simuladores numéricos (CMG STARS, ECLIPSE), paquetes PVT/EOS ni en balances de energía de superficie. Ninguna herramienta lograba unir la geoquímica de Larter con la segunda ley de la termodinámica.

En este trabajo introduzco el marco metodológico MANCO Exergetic Framework (MANCO-EX) y su motor SOTA Engine (v3.1), evolucionando la escala de Larter al integrar:
1. Índice de Destrucción Exergética (ΔXd, en kJ/mol): Basado en la teoría de tasas de transición de Eyring y la exergía química de Szargut, convirtiendo la depleción de metilfenantrenos y esteroides triaromáticos en resistencia irreversible al flujo.
2. Arquitectura de Datos Multi-Cuenca (N = 1,896 muestras totales; N = 41 suites completas de alta resolución con mediciones de laboratorio): Validado rigurosamente en la Faja del Orinoco (Venezuela), Athabasca (Canadá), Junggar (China) y Bongor (Chad).
3. Límite Físico de Inutilidad Termodinámica (ΔXd_crit = 8.50 ± 0.78 kJ/mol, 95% CI: [6.09, 9.20], Enet ≤ 0): Define el umbral exacto donde la energía necesaria para levantar y calentar el fluido supera la exergía neta de los hidrocarburos producidos.

Resultados del benchmark de evaluación vs. Modelos Legado (Evaluados en N=41 a T=40°C):
• Modelo LMM REML: R² marginal = 0.18 (efecto fijo ΔXd) y R² condicional > 0.99 (con interceptos aleatorios por cuenca; MAE = 0.0082 ln cP, RMSE = 0.012 ln cP).
• Test de Pendientes Aleatorias (LRT = 449.05, p < 10⁻¹⁵): Demuestra que la pendiente exergética varía entre cuencas (β = 3.05 ± 0.32) según el fluido precursore.
• Falla de Correlaciones Tradicionales: Beggs-Robinson (1975) (R² = -2.25, MAE = 2.08 ln cP) y Egbogah-Ng (1990) (R² = -2.70, MAE = 2.25 ln cP) colapsan sistemáticamente al carecer de datos de degradación molecular.
• Optimización Operacional (OPEX): Ahorro del 12% al 18% en consumo de diluyente mediante optimización exergética de mezclas en cabezal de pozo.

Enlaces a la evidencia pública:
• Preprint Oficial en la Red de Elsevier (SSRN ID 7243483): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7243483
• Dataset Público Registrado (Zenodo DOI: 10.5281/zenodo.21826600): https://doi.org/10.5281/zenodo.21826600
• Código de Demostración Pública (GitHub - Licencia MIT): https://github.com/joseagarpe/manco-ex-sota

Para consultorías técnicas, integración en simuladores de yacimientos (EOS/PVT), optimización de diluyente o auditorías de selección de EOR Térmico bajo este marco metodológico, puedes contactarme directamente a través de: contacto@josegarciaphd.com.

#HeavyOil #ReservoirEngineering #Thermodynamics #OrganicGeochemistry #ExergyAnalysis #PetroleumEngineering #EOR #SSRN #Elsevier #Venezuela #OrinocoBelt #Athabasca #EnergyTransition #Geochemistry