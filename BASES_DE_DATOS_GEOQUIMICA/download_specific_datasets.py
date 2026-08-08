import os
import json
import urllib.request
import ssl

ssl_context = ssl._create_unverified_context()
BASE_DIR = r"C:\Users\josea\CEREBRO\005 RECURSOS\BASES_DE_DATOS_GEOQUIMICA"

item_ids = [
    "61561495d34e0df5fb9ec0dd",  # Petroleum Geochemistry Research Laboratory Biomarkers
    "60194f05d34edf5c66f0d0a4",  # Organic and Inorganic Geochemical Reference Material
    "64fa1e71d34ed30c2054ea11"   # USGS National Produced Waters Geochemical Database
]

for i_id in item_ids:
    url = f"https://www.sciencebase.gov/catalog/item/{i_id}?format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ssl_context) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            title = data.get('title', 'Sin titulo')
            print(f"\nItem: {title}")
            for f_info in data.get('files', []):
                fname = f_info.get('name', '')
                furl = f_info.get('url', '')
                target_path = os.path.join(BASE_DIR, fname.replace(" ", "_"))
                print(f"  - Descargando {fname} ({f_info.get('size', 0)} bytes)...")
                try:
                    f_req = urllib.request.Request(furl, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(f_req, context=ssl_context) as f_resp, open(target_path, 'wb') as out_f:
                        out_f.write(f_resp.read())
                    print(f"    Guardado en {target_path}")
                except Exception as e_f:
                    print(f"    Error descargando {fname}: {e_f}")
    except Exception as e:
        print(f"Error consultando item {i_id}: {e}")
