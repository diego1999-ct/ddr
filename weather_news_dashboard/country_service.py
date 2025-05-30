# Importa la biblioteca 'requests' para realizar solicitudes HTTP a APIs web.
import requests

# Define una función que recibe el nombre de un país como argumento.
def get_country_info(country_name: str):
    # Construye la URL para hacer la solicitud a la API de REST Countries.
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    # Realiza una solicitud GET a la URL.
    response = requests.get(url)
    
    # Verifica si la respuesta tiene un código HTTP diferente de 200 (éxito).
    # Si es así, lanza una excepción con un mensaje de error.
    if response.status_code != 200:
        raise Exception(f"Error fetching country data: HTTP {response.status_code}")
    
    # Convierte la respuesta JSON en un diccionario Python.
    # Se toma solo el primer resultado de la lista.
    data = response.json()[0]

    # Obtiene la capital del país. Si no está disponible, se usa "N/A".
    capital = data.get("capital", ["N/A"])[0]
    
    # Obtiene la población del país. Si no está disponible, se usa "N/A".
    population = data.get("population", "N/A")
    
    # Obtiene el diccionario de monedas del país. Si no hay, se usa uno vacío.
    currencies = data.get("currencies", {})
    
    # Inicializa la variable de la moneda con "N/A".
    currency = "N/A"
    
    # Si existe al menos una moneda, se toma la clave (el código, como "CLP" o "USD").
    if currencies:
        currency = list(currencies.keys())[0]

    # Retorna un diccionario con la capital, población y moneda del país.
    return {
        "capital": capital,
        "poblacion": population,
        "moneda": currency
    }
