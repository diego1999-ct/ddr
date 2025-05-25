import json
from weather_service import get_current_weather
from news_service import get_news
from country_service import get_country_info

def generate_report():
    city = "La Serena"
    country_code = "CL"
    try:
        weather = get_current_weather(city, country_code)
        news = get_news("Chile")
        country_info = get_country_info("chile")

        report = {
            "current_weather": weather,
            "recent_news": news,
            "country_info": country_info
        }

        with open("daily_report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        # Construir texto del reporte
        lines = []
        lines.append("=== DAILY REPORT ===")
        lines.append(f"Ciudad: {weather['ciudad']}")
        lines.append(f"Clima: {weather['descripcion']}")
        lines.append(f"Temperatura: {weather['temperatura']} °C")
        lines.append(f"Humedad: {weather['humedad']} %")
        lines.append(f"Viento: {weather['viento']} m/s")
        lines.append("\n--- Noticias Recientes ---")
        for article in news:
            lines.append(f"- {article['titulo']} (Fuente: {article['fuente']}, Fecha: {article['fecha']})")
        lines.append("\n--- Información del País ---")
        lines.append(f"Capital: {country_info['capital']}")
        lines.append(f"Población: {country_info['poblacion']}")
        lines.append(f"Moneda: {country_info['moneda']}")

        return "\n".join(lines)

    except Exception as e:
        return f"Error al generar el reporte: {e}"
