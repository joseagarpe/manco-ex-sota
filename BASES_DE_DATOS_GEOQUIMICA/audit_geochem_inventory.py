import os
import csv
import sys

# Force stdout encoding to utf-8 if possible
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\josea\CEREBRO\005 RECURSOS\BASES_DE_DATOS_GEOQUIMICA"

def analyze_pgrl():
    data_file = os.path.join(BASE_DIR, "PGRL_MSD_Data_Release_Data.csv")
    desc_file = os.path.join(BASE_DIR, "PGRL_MSD_Data_Release_ColumnDescriptions.csv")
    
    print("\n=======================================================")
    print("AUDITORIA: USGS Petroleum Geochemistry Research Lab (PGRL)")
    print("=======================================================")
    
    if os.path.exists(desc_file):
        print("\n--- Descripcion de Columnas (PGRL) ---")
        with open(desc_file, "r", encoding="utf-8-sig", errors="ignore") as f:
            reader = csv.reader(f)
            for row in list(reader)[:35]:
                if row:
                    clean_row = [c.encode('ascii', 'ignore').decode('ascii') for c in row[:3]]
                    print(" | ".join(clean_row))
                    
    if os.path.exists(data_file):
        print("\n--- Muestreo de Datos (PGRL Data) ---")
        with open(data_file, "r", encoding="utf-8-sig", errors="ignore") as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            rows = list(reader)
            print(f"Total Columnas de Biomarcadores/Ratios: {len(headers) if headers else 0}")
            print(f"Total Registros/Analisis: {len(rows)}")
            print("\nPrimeras 30 Columnas de Biomarcadores:")
            if headers:
                for h in headers[:30]:
                    clean_h = h.encode('ascii', 'ignore').decode('ascii')
                    print(f"  - {clean_h}")

def main():
    print("=== INVENTARIO DE ARCHIVOS DESCARGADOS (005 RECURSOS\\BASES_DE_DATOS_GEOQUIMICA) ===")
    all_files = os.listdir(BASE_DIR)
    total_size_mb = 0
    for f in sorted(all_files):
        fpath = os.path.join(BASE_DIR, f)
        if os.path.isfile(fpath):
            size_mb = os.path.getsize(fpath) / (1024 * 1024)
            total_size_mb += size_mb
            print(f" - {f:<55} [{size_mb:.2f} MB]")
    print(f"\nTAMO TOTAL EN DISCO: {total_size_mb:.2f} MB\n")
            
    analyze_pgrl()

if __name__ == "__main__":
    main()
