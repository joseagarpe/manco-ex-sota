import os

tex_path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\fuel_manco_v2_manuscript.tex"

with open(tex_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Table 4 with clean wrapping columns
clean_table4_wrapped = r"""\begin{table}[htbp]
\centering
\caption{Comparative Benchmarking of MANCO-EX SOTA Engine Against Legacy Models Evaluated on the Global Multi-Basin Dataset ($N=41$).}
\label{tab:sota_benchmarking}
\small
\begin{tabular}{p{3.8cm} p{3.0cm} c c p{4.2cm}}
\toprule
\textbf{Model / Correlation} & \textbf{Model Type} & $R^2_{\text{CV}}$ & \textbf{MAE ($\ln\text{ cP}$)} & \textbf{Key Advantage / Limitation} \\
\midrule
Beggs-Robinson (1975) & Empirical (API, $T$) & 0.4520 & 1.25 & Standard PVT / Fails under advanced degradation \\
Pedersen et al. (1984) & Extended EOS & 0.6210 & 0.95 & High compositional input / Weak polar coupling \\
MANCO v1.0 (Larter 2012) & Geochemical Ratio & 0.8340 & 0.52 & High molecular resolution / No energy balance \\
MANCO-EX SOTA Engine & Physical + Geochemical & 0.9203 & 0.27 & Couples exergy, Eyring viscosity \& EOS \\
\bottomrule
\end{tabular}
\end{table}"""

start_idx = text.find(r"\label{tab:sota_benchmarking}")
if start_idx != -1:
    tbl_start = text.rfind(r"\begin{table}", 0, start_idx)
    tbl_end = text.find(r"\end{table}", start_idx) + len(r"\end{table}")
    text = text[:tbl_start] + clean_table4_wrapped + text[tbl_end:]

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Table 4 to explicit wrapping columns p{...} successfully.")
