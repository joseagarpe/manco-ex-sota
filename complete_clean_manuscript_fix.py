import re

tex_path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\fuel_manco_v2_manuscript.tex"

with open(tex_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix line 73: Replace CEREBRO knowledge vault references
text = text.replace(r"maintained in the \textit{CEREBRO} knowledge vault (\texttt{005 RECURSOS/BASES\_DE\_DATOS\_GEOQUIMICA}):",
                    r"openly accessible via Zenodo (\url{https://doi.org/10.5281/zenodo.21826600}) and GitHub (\url{https://github.com/joseagarpe/manco-ex-sota}):")

text = re.sub(r'maintained in the \\textit\{CEREBRO\} knowledge vault.*?:', r'openly accessible via Zenodo (DOI: 10.5281/zenodo.21826600) and GitHub (https://github.com/joseagarpe/manco-ex-sota):', text)
text = text.replace("CEREBRO knowledge vault", "open-access data repository")
text = text.replace("005 RECURSOS/BASES_DE_DATOS_GEOQUIMICA", "Zenodo repository (DOI: 10.5281/zenodo.21826600)")

# 2. Remove all \textbf{...} in regular body text (except in headers, table headers, and math labels)
def remove_body_bold(match):
    full_match = match.group(0)
    content = match.group(1)
    # Preserve table header bolding, section titles, and small labels
    if "Model" in content or "Key" in content or "MAE" in content or "Perturbed" in content or "Baseline" in content or "Parameter" in content:
        return full_match
    return content

text = re.sub(r'\\textbf\{([^\}]+)\}', remove_body_bold, text)

# 3. Ensure Zenodo DOI and GitHub links are in the Abstract, Section 2.1, and Data Availability
zenodo_str = r"\url{https://doi.org/10.5281/zenodo.21826600}"
github_str = r"\url{https://github.com/joseagarpe/manco-ex-sota}"

if "10.5281/zenodo.21826600" not in text:
    text = text.replace(r"\end{abstract}", f" The open-access dataset ({zenodo_str}) and open-source public demonstration engine ({github_str}) are available.\n\\end{{abstract}}")

# 4. Make Table 4 (Benchmarking) fit cleanly within single-column text margins
clean_table4_final = r"""\begin{table}[htbp]
\centering
\caption{Comparative Benchmarking of MANCO-EX SOTA Engine Against Legacy Models Evaluated on the Global Multi-Basin Dataset ($N=41$).}
\label{tab:sota_benchmarking}
\small
\begin{tabular}{llccl}
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
    text = text[:tbl_start] + clean_table4_final + text[tbl_end:]

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied complete clean manuscript fixes successfully.")
