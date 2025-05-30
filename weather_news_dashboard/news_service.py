import requests
from config import NEWSAPI_API_KEY  # Importa la clave API para NewsAPI desde config.py

def get_news(query: str, language: str = "es", page_size: int = 5):
    """
    Obtiene noticias desde NewsAPI basadas en una consulta.
    
    Parámetros:
    - query: término de búsqueda para las noticias.
    - language: idioma de las noticias (por defecto español "es").
    - page_size: cantidad máxima de noticias a retornar (por defecto 5).
    
    Retorna:
    - Lista de diccionarios con título, fuente y fecha de cada noticia.
    """

    # Construye la URL con parámetros para la API NewsAPI
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&language={language}&sortBy=publishedAt&pageSize={page_size}&apiKey={NEWSAPI_API_KEY}"
    )

    # Realiza la petición HTTP GET a la API
    response = requests.get(url)

    # Verifica que la respuesta sea exitosa (código 200)
    if response.status_code != 200:
        # Si no, lanza una excepción con el código de error HTTP
        raise Exception(f"Error fetching news data: HTTP {response.status_code}")

    # Parsea la respuesta JSON
    data = response.json()

    articles = []
    # Itera sobre la lista de artículos que devuelve la API
    for article in data.get("articles", []):
        # Extrae título, fuente y fecha de publicación, y los añade a la lista
        articles.append({
            "titulo": article.get("title"),
            "fuente": article.get("source", {}).get("name"),
            "fecha": article.get("publishedAt")
        })

    # Retorna la lista de artículos procesados
    return articles
