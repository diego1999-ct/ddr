import json
# Importa el módulo para obtener el clima actual
from weather_service import get_current_weather
# Importa el módulo para obtener las noticias actuales
from news_service import get_news
# Importa el módulo para obtener información del país
from country_service import get_country_info

# Función que genera un reporte diario combinando datos de clima, noticias e información del país
def generate_report():
    # Ciudad y código de país para el clima
    city = "La Serena"
    country_code = "CL"
    try:
        # Obtiene el clima actual para la ciudad especificada
        weather = get_current_weather(city, country_code)

        # Obtiene noticias recientes relacionadas con Chile
        news = get_news("Chile")

        # Obtiene información general sobre el país Chile
        country_info = get_country_info("chile")

        # Construye un diccionario con toda la información reunida
        report = {
            "current_weather": weather,
            "recent_news": news,
            "country_info": country_info
        }

        # Guarda el reporte como archivo JSON legible
        with open("daily_report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        # Construcción del reporte en texto plano
        lines = []
        lines.append("=== DAILY REPORT ===")
        lines.append(f"Ciudad: {weather['ciudad']}")
        lines.append(f"Clima: {weather['descripcion']}")
        lines.append(f"Temperatura: {weather['temperatura']} °C")
        lines.append(f"Humedad: {weather['humedad']} %")
        lines.append(f"Viento: {weather['viento']} m/s")

        lines.append("\n--- Noticias Recientes ---")
        # Agrega al reporte las noticias obtenidas
        for article in news:
            lines.append(f"- {article['titulo']} (Fuente: {article['fuente']}, Fecha: {article['fecha']})")

        lines.append("\n--- Información del País ---")
        lines.append(f"Capital: {country_info['capital']}")
        lines.append(f"Población: {country_info['poblacion']}")
        lines.append(f"Moneda: {country_info['moneda']}")

        # Devuelve el reporte en formato de texto plano como string
        return "\n".join(lines)

    # Maneja cualquier error durante el proceso y lo devuelve como mensaje
    except Exception as e:
        return f"Error al generar el reporte: {e}"
