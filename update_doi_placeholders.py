import re

tex_path = r"C:\Users\josea\CEREBRO\004 PROYECTOS\ARTICULO_GEOQUIMICA_EXERGIA_V1_2\fuel_manco_v2_manuscript.tex"

with open(tex_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace dummy DOI and GitHub URL with standard pre-submission editorial placeholders
text = text.replace(r"\texttt{10.5281/zenodo.10892341}", r"\texttt{[Zenodo DOI to be assigned upon publication]}")
text = text.replace(r"\texttt{github.com/manco-ex/manco-exergetic-framework}", r"\texttt{[GitHub repository link available upon publication]}")

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated DOI and GitHub placeholders to standard editorial pre-submission format.")
