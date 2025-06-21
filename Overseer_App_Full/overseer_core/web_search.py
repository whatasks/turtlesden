import random
import time
import requests
from bs4 import BeautifulSoup

def web_search(query):
    """Simulate a human-like web search and return a snippet."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36"
    }
    search_engines = [
        f"https://www.bing.com/search?q={query}",
        f"https://duckduckgo.com/html/?q={query}"
    ]
    for url in search_engines:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            snippets = soup.find_all("p")
            if snippets:
                return snippets[0].text.strip()
            time.sleep(random.uniform(2, 4))
        except Exception:
            continue
    return "Search failed."
