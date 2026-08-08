import os
import json
import urllib.request
import urllib.parse
import ssl

ssl_context = ssl._create_unverified_context()
BASE_DIR = r"C:\Users\josea\CEREBRO\005 RECURSOS\BASES_DE_DATOS_GEOQUIMICA"

def search_sciencebase(query):
    url = f"https://www.sciencebase.gov/catalog/items?q={urllib.parse.quote(query)}&format=json&max=20"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ssl_context) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('items', [])
    except Exception as e:
        print(f"Error {query}: {e}")
        return []

def main():
    queries = [
        "Crude Oil Database",
        "Petroleum Geochemistry Database",
        "Geochemical Database of Oil",
        "USGS Petroleum Characterization",
        "USGS Oil Biomarker"
    ]
    
    results = {}
    for q in queries:
        items = search_sciencebase(q)
        print(f"\nQuery: '{q}' -> {len(items)} resultados")
        for it in items:
            title = it.get('title', '')
            item_id = it.get('id', '')
            link = it.get('link', {}).get('url', '')
            print(f"  * [{item_id}] {title}")
            
            # Fetch files
            detail_url = f"https://www.sciencebase.gov/catalog/item/{item_id}?format=json"
            try:
                with urllib.request.urlopen(urllib.request.Request(detail_url, headers={'User-Agent': 'Mozilla/5.0'}), context=ssl_context) as d_resp:
                    d_data = json.loads(d_resp.read().decode('utf-8'))
                    files = [f.get('name', '') for f in d_data.get('files', [])]
                    print(f"    Archivos ({len(files)}): {files[:5]}")
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
