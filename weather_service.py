import requests
from config import OPENWEATHER_API_KEY

def get_current_weather(city: str, country_code: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching weather data: HTTP {response.status_code}")
    data = response.json()

    weather_data = {
        "ciudad": data.get("name"),
        "descripcion": data["weather"][0]["description"],
        "temperatura": data["main"]["temp"],
        "humedad": data["main"]["humidity"],
        "viento": data["wind"]["speed"]
    }
    return weather_data
