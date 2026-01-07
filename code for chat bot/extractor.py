import requests
from bs4 import BeautifulSoup

def extract_text(url):
    try:
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        return " ".join(text.split())
    except:
        return ""
