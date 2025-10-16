import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse, parse_qs

def search_content(query, num_results=3):
    query_encoded = requests.utils.quote(query)
    url = f"https://duckduckgo.com/html/?q={query_encoded}"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for a in soup.select('.result__a', limit=num_results):
        href = a.get('href', '')
        # Decode DuckDuckGo redirect URL
        parsed = urlparse(href)
        qs = parse_qs(parsed.query)
        if 'uddg' in qs:
            real_url = unquote(qs['uddg'][0])
            results.append(real_url)
        else:
            results.append(href)
    return results

