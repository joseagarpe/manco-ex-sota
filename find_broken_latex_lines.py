import os

tex_path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\fuel_manco_v2_manuscript.tex"

with open(tex_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if r"\cr" in l or r"\end{enumerate}{enumerate}" in l or r"\begin{tabular}" in l:
        print(f"Line {i+1}: {l.strip()}")
