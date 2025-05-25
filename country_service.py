import requests

def get_country_info(country_name: str):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching country data: HTTP {response.status_code}")
    data = response.json()[0]

    capital = data.get("capital", ["N/A"])[0]
    population = data.get("population", "N/A")
    currencies = data.get("currencies", {})
    currency = "N/A"
    if currencies:
        currency = list(currencies.keys())[0]

    return {
        "capital": capital,
        "poblacion": population,
        "moneda": currency
    }
