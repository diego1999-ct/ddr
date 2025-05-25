import requests
from config import NEWSAPI_API_KEY

def get_news(query: str, language: str = "es", page_size: int = 5):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&language={language}&sortBy=publishedAt&pageSize={page_size}&apiKey={NEWSAPI_API_KEY}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching news data: HTTP {response.status_code}")
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        articles.append({
            "titulo": article.get("title"),
            "fuente": article.get("source", {}).get("name"),
            "fecha": article.get("publishedAt")
        })
    return articles
