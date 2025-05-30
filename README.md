# 🌦️📰 Weather & News Dashboard

Aplicación de escritorio en Python que muestra el clima actual, las noticias principales y la moneda del país correspondiente a una ciudad ingresada. Desarrollada con una interfaz gráfica (GUI) moderna con estilo oscuro utilizando `tkinter`.

  Estructura del Proyecto
drr/

└── weather_news_dashboard/

  ├── config.py              # Configuración: claves API y constantes
  
  ├── country_service.py     # Servicio: datos del país (REST Countries)
  
  ├── credentials.json       # Credenciales OAuth 2.0 (descargadas desde Google Cloud Console)
  
  ├── daily_report.json      # (Opcional) Datos del reporte diario (si aplica)
  
  ├── dashboard.py           # Coordinador: integra datos de todos los servicios y construye el reporte
  
  ├── main.py                # Interfaz gráfica (GUI principal)
  
  ├── news_service.py        # Servicio: obtiene noticias desde NewsAPI
  
  ├── requirements.txt       # Lista de dependencias necesarias (para pip)
  
  ├── send_daily_report.py   # Script que genera y envía el reporte diario por correo
  
  ├── token.json             # Token de autenticación OAuth generado automáticamente
  
  └── weather_service.py     # Servicio: obtiene datos del clima (OpenWeatherMap)
  


 #  Requisitos

Instala las dependencias necesarias usando:

bash
pip install -r requirements.txt

  # APIs Utilizadas
  
1. OpenWeatherMap API
Clima actual por ciudad.

https://openweathermap.org/api

2. NewsAPI
Noticias destacadas según el país.

https://newsapi.org

1. REST Countries API
Para obtener la moneda del país ingresado.

https://restcountries.com

   # Funcionalidades

Temperatura actual, condiciones meteorológicas y humedad.

Noticias destacadas del país correspondiente.

Moneda oficial del país.

  # Ejecución
Desde la terminal, en la carpeta del proyecto:

python main.py o correr directamente main.py

Parte 1: Exploración con curl

Tarea 1.1: Clima en La Serena o Coquimbo
*Comando curl:*

curl -s "https://api.openweathermap.org/data/2.5/weather?q=La%20Serena,CL&appid=c4dae954b16df24a1acb3ce3acd79be3&units=metric&lang=es" | jq
![image](https://github.com/user-attachments/assets/663d02a6-0736-439a-8d6b-262327036923)

Explicación:

 q: ciudad y país
 appid: clave de API
 units: métrica
 Campos relevantes:
 main.temp: Temperatura actual
 main.humidity: Humedad
 weather[0].description: Descripción del clima
 wind.speed: Velocidad del viento
 main.pressure: Presión atmosférica

 Tarea 1.2: Noticias de Chile
 
 curl -s "https://newsapi.org/v2/everything?q=Chile&language=es&sortBy=publishedAt&apiKey=ba3486b0141d404285ebe9cdccd06611" | jq ".articles[] | {titulo: .title, fuente: .source.name, fecha: .publishedAt}"

![image](https://github.com/user-attachments/assets/79adfbbf-633e-49b0-8590-90f26eed2304)

Tarea 1.3: Información de Chile (REST Countries)

curl -s "https://restcountries.com/v3.1/name/chile" | jq
![image](https://github.com/user-attachments/assets/dae50d21-830f-43dc-9d4f-2bff28989b4c)

Datos extraídos:

Nombre: Chile
Nombre oficial: República de Chile
Capital: Santiago
Región: Americas
Subregión: South America
Moneda:
 Nombre: Chilean peso
 Símbolo: $
Idioma principal: Spanish
Dominio de nivel superior: .cl
Población: 19.116.209
Continente: South America
Código de país (CCA2): CL
Países fronterizos: Argentina, Bolivia, Perú
Coordenadas: Latitud -30.0, Longitud -71.0
Miembro de la ONU: Sí
Bandera: 🇨🇱

•	Estructura anidada del JSON

 1. Objeto (name)
 ![image](https://github.com/user-attachments/assets/674ce5b0-e7f7-4b1c-86c7-dcc10b91fecb)

Aquí, "name" es un objeto que contiene:

-"common" y "official" como claves de nivel superior.
-"nativeName" como un objeto anidado, el cual a su vez contiene un objeto "spa" con su propio par de claves.

2. Objeto (currencies)
   ![image](https://github.com/user-attachments/assets/0638fec9-f208-40af-835a-bec3bb3b5ec1)

  - "currencies" es un objeto que contiene un código de moneda ("CLP") como clave, y este a su vez contiene otro objeto con la información de símbolo y nombre.

3. Objeto (translations)

   ![image](https://github.com/user-attachments/assets/e65363db-7357-4f54-9634-e0acf993dbf4)
   ![image](https://github.com/user-attachments/assets/b21c963f-888c-4c5e-8333-e26361e2e9d2)
   ![image](https://github.com/user-attachments/assets/fe2db023-cd69-42b5-ae77-c505aff2f1d6)
   
  - "translations" agrupa varios objetos por idioma (como "fra", "spa"), y cada uno de ellos tiene versiones comunes y oficiales del nombre del país.

4. Objeto (flags)

![image](https://github.com/user-attachments/assets/5018a0f4-e9e6-436d-880e-8e97394d582b)

Contiene varias representaciones de la bandera (en formato imagen y descripción), organizadas dentro del mismo objeto.


5. Objeto (maps)

![image](https://github.com/user-attachments/assets/ad806e1d-cca0-4325-8240-df606c5873d7)

Contiene URLs a diferentes plataformas de mapas, agrupadas por tipo.

6. Objeto (car)

![image](https://github.com/user-attachments/assets/f6f96831-44ab-4f73-b546-14291a80edd1)

Información sobre señalización y dirección de manejo, dentro de un mismo objeto.

La estructura anidada permite representar datos complejos de forma clara y organizada. Para acceder a estos datos, se puede usar una notación de punto en herramientas como jq, por ejemplo:

.name.official : "Republic of Chile"
.currencies.CLP.name : "Chilean peso"
.translations.spa.official : "República de Chile"

Tarea 1.4: Filtros y errores}

Pronóstico extendido:

A) Modifica la consulta meteorológica para obtener pronóstico de 5 días

curl -s "https://api.openweathermap.org/data/2.5/forecast?q=La%20Serena,CL&appid=c4dae954b16df24a1acb3ce3acd79be3&units=metric&lang=es" | jq

![image](https://github.com/user-attachments/assets/1d7a0098-8992-4258-ac7c-4876311d2b39)

Proporciona: un pronóstico del clima a 5 días, con datos cada 3 horas.
Devuelve: un arreglo (list[]) con múltiples entradas, cada una correspondiente a una hora diferente.

b) Filtrar noticias por categoría (NewsAPI)

curl -s "https://newsapi.org/v2/top-headlines?country=cl&category=business&apiKey=ba3486b0141d404285ebe9cdccd06611" | jq

![image](https://github.com/user-attachments/assets/6bbb9e35-9af5-4b5c-9db7-6fcb2c67bf5c)

C)	Maneja errores HTTP y documenta códigos de respuesta

curl -s -w "%{http_code}\n" -o response.json "https://newsapi.org/v2/top-headlines?country=cl&category=business&apiKey=ba3486b0141d404285ebe9cdccd06611"

![image](https://github.com/user-attachments/assets/8d3cff59-8b21-4981-b809-9b3bfe3b4a67)

Resultado del código HTTP:
200 (OK)  Significa que la consulta fue válida y la respuesta fue entregada con éxito.

Verificar contenido del archivo
type response.json

![image](https://github.com/user-attachments/assets/b357a08a-37f1-47d6-a8fa-49a5ba61f2e6)

Parte 2: Implementación en Python.

![image](https://github.com/user-attachments/assets/55389381-38f2-48e5-b917-1b2b627d27cc)

Parte 3: Conectar API de Gmail.

send_daily_report.py

Este script genera y envía un reporte diario automatizado con la siguiente información:

- Clima actual en La Serena, Chile.
- Noticias recientes relacionadas con Chile.
- Información general del país.

El reporte se envía automáticamente por correo electrónico mediante la API de Gmail a:
- Destinatario: tabajoapidrr@gmail.com

Requisitos previos:

1. Archivo `credentials.json` obtenido desde Google Cloud Console.
   - Tipo de credencial: OAuth 2.0 (Aplicación de escritorio)
2. Primera ejecución manual para generar `token.json` (proceso de autenticación OAuth).
3. Instalación de librerías necesarias:
   pip install --upgrade google-api-python-client google-auth-oauthlib google-auth-httplib2 requests

Automatización sugerida (Windows):

Utilizar el Programador de tareas para ejecutar este script todos los días a las 07:30 AM:
- Programa: Ruta hacia python.exe (por ejemplo: .venv\Scripts\python.exe)
- Argumentos: send_daily_report.py
- Directorio de inicio: Carpeta donde se encuentra este archivo

Archivos requeridos:

- `dashboard.py`: Debe contener la función `generate_report()`
- `config.py`: Debe contener las claves y configuraciones necesarias para las APIs
- `token.json`: Se genera automáticamente tras la primera autorización OAuth

Parte 3.1: Configuracion de programador de tareas para envio de correos automaticos.

1.- Abrir el programador de tareas de Windows.

![image](https://github.com/user-attachments/assets/bd47979e-03c7-466e-abab-2c220240c496)

2.- Crear una nueva tarea con los siguientes valores.

![image](https://github.com/user-attachments/assets/032628f2-f228-448a-a672-0c0009c6bab9)

Generales: 
Nombre: Enviar reporte diario
Ejecutar con privilegios elevados

Desencadenadores:
Programado diariamente
Hora: 07:30

![image](https://github.com/user-attachments/assets/47c45034-fd10-42ce-a9a9-f5d584fd34e1)

Acciones:

![image](https://github.com/user-attachments/assets/8630102c-7983-4b83-899c-30e77104bf0a)

Programa: C:\Users\raver\Downloads\drr-main\.venv\Scripts\python.exe
Argumentos: send_daily_report.py
Iniciar en: C:\Users\raver\Downloads\drr-main\drr-main
Finalmente guarda y asegúrate de que el script se ejecuta correctamente manualmente antes de automatizar.

Resultados: 

Cada día a las 7:30 AM, se generará un reporte con:
Clima actual de La Serena, Chile
Noticias recientes relacionadas con Chile
Información general del país
Y se enviará automáticamente al correo tabajoapidrr@gmail.com.

![image](https://github.com/user-attachments/assets/a729351b-b5f1-40a7-868f-8eab203c0ea8)














