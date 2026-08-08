tex_path = r"C:\Users\josea\CEREBRO\003 AREAS\RIQUEZA FINANCIERA\FIRMA DE TRANSFERENCIA TECNICA\A-IP_ACERVO_TECNOLOGICO\PAPER_5_FUEL\fuel_manco_v2_manuscript.tex"

with open(tex_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace non-ASCII characters with safe LaTeX equivalents
replacements = {
    "José A. García": r"Jos\'e A. Garc\'ia",
    "José": r"Jos\'e",
    "García": r"Garc\'ia",
    "Mónaco": r"M\'onaco",
    "Junín": r"Jun\'in",
    "": "--",
    "“": '"',
    "”": '"',
    "’": "'",
    "‘": "'",
    "–": "--",
    "—": "---"
}

for old_s, new_s in replacements.items():
    text = text.replace(old_s, new_s)

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Sanitized non-ASCII characters in LaTeX manuscript successfully.")
