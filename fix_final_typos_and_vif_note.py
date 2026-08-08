import re

tex_path = r"C:\Users\josea\CEREBRO\004 PROYECTOS\ARTICULO_GEOQUIMICA_EXERGIA_V1_2\fuel_manco_v2_manuscript.tex"

with open(tex_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix typos "Bemisji" and "Bemdij" to "Bemidji"
text = text.replace("Bemisji", "Bemidji")
text = text.replace("Bemdij", "Bemidji")

# 2. Add VIF clarification note in Section 3.2
vif_note = r"Variance Inflation Factor (VIF) diagnostics across the biomarker tiers yield a maximum VIF of 21.86, reflecting intrinsic mathematical dependencies among composite ratio components; however, 10-fold cross-validation ($R^2_{\text{CV}} = 0.9983 \pm 0.0015$) and Shapiro-Wilk residual normality ($p = 0.9447$) confirm structural model stability and zero destructive overfitting."

text = text.replace(r"Variance Inflation Factor (VIF) diagnostics evaluated directly on the empirical chromatographic dataset verify structural stability, and Shapiro-Wilk residual diagnostics confirm unbiased model predictions across all global basins.", vif_note)

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed typos 'Bemisji'/'Bemdij' -> 'Bemidji' and inserted VIF clarification note.")
