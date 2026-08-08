import os
import glob
import csv
import json

BASE_DIR = r"C:\Users\josea\CEREBRO\005 RECURSOS\BASES_DE_DATOS_GEOQUIMICA"

def inspect_csv(file_path):
    print(f"\n==========================================")
    print(f"ARCHIVO: {os.path.basename(file_path)}")
    print(f"==========================================")
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if not headers:
                print("Archivo vacio.")
                return
            print(f"Total Columnas: {len(headers)}")
            print("Columnas (primeras 20):")
            for h in headers[:20]:
                print(f"  - {h}")
            
            rows = list(reader)
            print(f"Total Filas/Muestras: {len(rows)}")
            if rows:
                print("Muestra 1 (primeros 10 valores):")
                print(f"  {rows[0][:10]}")
    except Exception as e:
        print(f"Error leyendo {file_path}: {e}")

def main():
    csv_files = glob.glob(os.path.join(BASE_DIR, "*.csv"))
    print(f"Encontrados {len(csv_files)} archivos CSV en {BASE_DIR}.\n")
    for f in csv_files:
        inspect_csv(f)

if __name__ == "__main__":
    main()
