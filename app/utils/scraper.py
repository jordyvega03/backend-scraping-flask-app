import requests
from bs4 import BeautifulSoup

def scrape_html_content(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.get_text(separator="\n").strip()

    return content
