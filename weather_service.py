import requests  # Importa la librería para hacer solicitudes HTTP
from config import OPENWEATHER_API_KEY  # Importa la clave API para OpenWeatherMap desde config.py

def get_current_weather(city: str, country_code: str):
    """
    Función que obtiene el clima actual para una ciudad y código de país dados.
    """
    # Construye la URL para la API de OpenWeatherMap con parámetros:
    # ciudad, código país, API key, unidades métricas (°C), idioma español
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"
    
    # Realiza una solicitud GET a la URL
    response = requests.get(url)
    
    # Si la respuesta HTTP no es exitosa (código diferente de 200), lanza una excepción
    if response.status_code != 200:
        raise Exception(f"Error fetching weather data: HTTP {response.status_code}")
    
    # Parsea la respuesta JSON a un diccionario de Python
    data = response.json()

    # Extrae y organiza los datos relevantes del clima en un diccionario
    weather_data = {
        "ciudad": data.get("name"),  # Nombre de la ciudad
        "descripcion": data["weather"][0]["description"],  # Descripción del clima (ej. 'lluvioso')
        "temperatura": data["main"]["temp"],  # Temperatura actual en grados Celsius
        "humedad": data["main"]["humidity"],  # Porcentaje de humedad
        "viento": data["wind"]["speed"]  # Velocidad del viento en m/s
    }
    
    # Retorna el diccionario con los datos del clima
    return weather_data
