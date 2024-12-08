import requests
from bs4 import BeautifulSoup

# URL веб-сайта
url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    # Парсинг HTML-кода с использованием BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h2')
    for article in articles:
        print(article.text)
else:
    print(f"Ошибка при запросе: {response.status_code}")
