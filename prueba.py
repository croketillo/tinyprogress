import requests
from tinyprogress import progress

# Lista de URLs a visitar
urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net",
    "https://example.edu",
    "https://example.info",
    "https://example.biz",
    "https://example.co",
    "https://example.io",
    "https://example.ai",
    "https://example.tech",
]

# Cadena a buscar
target_string = "jmcarrizosa@josecarrizosa.es"

# Almacenar resultados
found_in = []

for url in progress(urls, task_name="Checking URLs"):
    try:
        response = requests.get(url, timeout=5)
        if target_string in response.text:
            found_in.append(url)
    except requests.RequestException:
        print(f"\n❌ Error accessing {url}")

# Mostrar resultados
if found_in:
    print("\n✅ Found the target string in:")
    for url in found_in:
        print(f"- {url}")
else:
    print("\n❌ The target string was not found in any of the URLs.")
