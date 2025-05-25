# 🌦️📰 Weather & News Dashboard

Aplicación de escritorio en Python que muestra el clima actual, las noticias principales y la moneda del país correspondiente a una ciudad ingresada. Desarrollada con una interfaz gráfica (GUI) moderna con estilo oscuro utilizando `tkinter`.

 # 📁 Estructura del Proyecto

drr/
 weather_news_dashboard/
 
  main.py # Interfaz gráfica principal (GUI)
  
  config.py # Configuración de claves API
  
  weather_service.py # Funciones para obtener datos del clima (OpenWeatherMap)
  
  news_service.py # Funciones para obtener noticias (NewsAPI)
  
  country_service.py # Funciones para mapear ciudad a país (REST Countries)
  
  dashboard.py # Lógica para coordinar y generar el reporte
  
  requirements.txt # Dependencias necesarias para ejecutar el proyecto


 # 🔧 Requisitos

Instala las dependencias necesarias usando:

bash
pip install -r requirements.txt

  #🔑 APIs Utilizadas
  
1. OpenWeatherMap API
Clima actual por ciudad.

https://openweathermap.org/api

2. NewsAPI
Noticias destacadas según el país.

https://newsapi.org

1. REST Countries API
Para obtener la moneda del país ingresado.

https://restcountries.com

   #🖥️ Funcionalidades

Temperatura actual, condiciones meteorológicas y humedad.

Noticias destacadas del país correspondiente.

Moneda oficial del país.

  #▶️ Ejecución
Desde la terminal, en la carpeta del proyecto:

python main.py o correr directamente main.py


