import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
from dashboard import generate_report

# Configuración
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
SENDER_EMAIL = "tu_correo_autenticado@gmail.com"  # <-- Cambia esto al que autorizas en Google
DEST_EMAIL = "tabajoapidrr@gmail.com"

def get_gmail_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text, "plain")
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}

def send_email(subject, body):
    service = get_gmail_service()
    message = create_message(SENDER_EMAIL, DEST_EMAIL, subject, body)
    send_message = service.users().messages().send(userId="me", body=message).execute()
    print(f"✅ Correo enviado con ID: {send_message['id']}")

def main():
    reporte = generate_report()
    send_email("Reporte diario automático", reporte)

if __name__ == "__main__":
    main()
