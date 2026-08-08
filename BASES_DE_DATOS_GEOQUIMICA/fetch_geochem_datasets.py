import os
import sys
import json
import urllib.request
import urllib.parse
import zipfile
import csv
import ssl

ssl_context = ssl._create_unverified_context()

BASE_DIR = r"C:\Users\josea\CEREBRO\005 RECURSOS\BASES_DE_DATOS_GEOQUIMICA"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def query_sciencebase(query, max_results=15):
    print(f"=== Buscando en USGS ScienceBase: '{query}' ===")
    url = f"https://www.sciencebase.gov/catalog/items?q={urllib.parse.quote(query)}&format=json&max={max_results}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ssl_context) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('items', [])
            print(f"Encontrados {len(items)} resultados de USGS ScienceBase.")
            results = []
            for item in items:
                title = item.get('title', 'Sin titulo')
                item_id = item.get('id', '')
                files = []
                detail_url = f"https://www.sciencebase.gov/catalog/item/{item_id}?format=json"
                try:
                    with urllib.request.urlopen(urllib.request.Request(detail_url, headers={'User-Agent': 'Mozilla/5.0'}), context=ssl_context) as d_resp:
                        d_data = json.loads(d_resp.read().decode('utf-8'))
                        for f in d_data.get('files', []):
                            files.append({
                                'name': f.get('name', ''),
                                'url': f.get('url', ''),
                                'size': f.get('size', 0)
                            })
                except Exception as e:
                    pass
                results.append({
                    'id': item_id,
                    'title': title,
                    'files': files
                })
            return results
    except Exception as e:
        print(f"Error consultando ScienceBase: {e}")
        return []

def download_file(url, target_path):
    print(f"Descargando: {url} -> {target_path}")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ssl_context) as resp, open(target_path, 'wb') as out_file:
        out_file.write(resp.read())
    print(f"Descarga completada ({os.path.getsize(target_path)} bytes).")

def main():
    ensure_dir(BASE_DIR)
    
    queries = [
        "crude oil geochemistry",
        "organic geochemistry petroleum biomarker",
        "geochemical database crude oil",
        "USGS crude oil"
    ]
    
    all_found_items = []
    seen_ids = set()
    
    for q in queries:
        items = query_sciencebase(q, max_results=10)
        for it in items:
            if it['id'] not in seen_ids:
                seen_ids.add(it['id'])
                all_found_items.append(it)
                
    log_path = os.path.join(BASE_DIR, "sciencebase_search_results.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(all_found_items, f, indent=2, ensure_ascii=False)
    print(f"\nResultados guardados en: {log_path}")
    
    downloadable = []
    for it in all_found_items:
        for f in it['files']:
            name_lower = f['name'].lower()
            if any(name_lower.endswith(ext) for ext in ['.csv', '.zip', '.xlsx', '.txt', '.tab', '.json', '.sqlite']):
                downloadable.append((it['title'], f['name'], f['url']))
                
    print(f"\nArchivos descargables identificados: {len(downloadable)}")
    for title, fname, url in downloadable[:15]:
        print(f"- [{fname}] ({title})")
        
    for title, fname, url in downloadable:
        if any(kw in fname.lower() or kw in title.lower() for kw in ['oil', 'geochem', 'crude', 'petroleum', 'biomarker', 'data', 'table']):
            safe_fname = fname.replace(" ", "_").replace("/", "_")
            out_file = os.path.join(BASE_DIR, safe_fname)
            try:
                download_file(url, out_file)
                if safe_fname.endswith('.zip'):
                    zip_extract_dir = os.path.join(BASE_DIR, safe_fname[:-4])
                    ensure_dir(zip_extract_dir)
                    with zipfile.ZipFile(out_file, 'r') as zip_ref:
                        zip_ref.extractall(zip_extract_dir)
                    print(f"Descomprimido en: {zip_extract_dir}")
            except Exception as e:
                print(f"Error descargando {fname}: {e}")

if __name__ == "__main__":
    main()
