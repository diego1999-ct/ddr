import base64
from email.mime.text import MIMEText  # Para crear mensajes MIME de texto plano
from google.oauth2.credentials import Credentials  # Para manejar credenciales OAuth2
from google_auth_oauthlib.flow import InstalledAppFlow  # Para el flujo OAuth interactivo
from googleapiclient.discovery import build  # Para construir el servicio Gmail API
import os
from dashboard import generate_report  # Función que genera el reporte diario

# Configuración
SCOPES = ['https://www.googleapis.com/auth/gmail.send']  # Permisos para enviar correos
SENDER_EMAIL = "tu_correo_autenticado@gmail.com"  # Cambiar por el correo autorizado en Google Cloud Console
DEST_EMAIL = "tabajoapidrr@gmail.com"  # Correo destinatario

def get_gmail_service():
    """
    Obtiene el servicio autenticado de Gmail usando OAuth2.
    Si existe token guardado, lo usa; si no, inicia flujo OAuth.
    """
    creds = None
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(BASE_DIR, "token.json")
    credentials_path = os.path.join(BASE_DIR, "credentials.json")

    # Verifica si ya existe un archivo token con credenciales guardadas
    if os.path.exists(token_path):
        # Carga las credenciales desde el archivo
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    else:
        # Si no, inicia el flujo de autorización OAuth interactivo
        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=0)  # Abre navegador para autenticación
        # Guarda las credenciales en token.json para uso futuro
        with open(token_path, "w") as token:
            token.write(creds.to_json())

    # Construye y retorna el servicio Gmail API autenticado
    return build("gmail", "v1", credentials=creds)

def create_message(sender, to, subject, message_text):
    """
    Crea un mensaje MIME para enviar por Gmail API.
    Codifica el mensaje en base64 urlsafe.
    """
    message = MIMEText(message_text, "plain")  # Crea mensaje de texto plano
    message["to"] = to  # Destinatario
    message["from"] = sender  # Remitente
    message["subject"] = subject  # Asunto del correo
    # Codifica el mensaje en base64 para enviarlo a Gmail API
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}  # Retorna el mensaje codificado listo para enviar

def send_email(subject, body):
    """
    Envía un correo con asunto y cuerpo especificados usando Gmail API.
    """
    service = get_gmail_service()  # Obtiene servicio autenticado
    message = create_message(SENDER_EMAIL, DEST_EMAIL, subject, body)  # Crea mensaje
    # Envía el mensaje mediante Gmail API y obtiene respuesta
    send_message = service.users().messages().send(userId="me", body=message).execute()
    print(f"✅ Correo enviado con ID: {send_message['id']}")  # Confirmación de envío

def main():
    """
    Función principal que genera el reporte y lo envía por correo.
    """
    reporte = generate_report()  # Genera reporte diario como texto
    send_email("Reporte diario automático", reporte)  # Envía el correo con el reporte

if __name__ == "__main__":
    main()  # Ejecuta la función principal al correr el script

