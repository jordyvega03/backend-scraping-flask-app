import requests  

BASE_URL = "http://127.0.0.1:4000/api"

def test_scrape():
    url = f"{BASE_URL}/scrape"
    response = requests.post(url, json={"url": "https://example.com"})
    print("Scrape Response:", response.json())

def test_ask():
    url = f"{BASE_URL}/ask"
    response = requests.post(url, json={
        "content": "Texto de prueba para OpenAI",
        "question": "¿Qué significa este texto?"
    })
    print("Ask Response:", response.json())

if __name__ == "__main__":
    test_scrape()
    test_ask()
