import requests
from config import BING_API_KEY, BING_ENDPOINT

TRUSTED_DOMAINS = [
    "nptel.ac.in",
    "mit.edu",
    "ieee.org",
    "edu",
    "ti.com",
    "analog.com"
]

def search_web(query, count=5):
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {
        "q": query + " VLSI electronics",
        "count": count
    }

    response = requests.get(BING_ENDPOINT, headers=headers, params=params)
    results = response.json().get("webPages", {}).get("value", [])

    urls = []
    for r in results:
        if any(domain in r["url"] for domain in TRUSTED_DOMAINS):
            urls.append(r["url"])

    return urls
