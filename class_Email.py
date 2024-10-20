from class_App import Aplicacion
from class_Celular import Celular

class Email(Aplicacion):
    def __init__(self):
        super().__init__(3,'Email')
        self.emails = []

    def enviar_email(self, email_destino, mensaje):
        self.emails.append((email_destino, mensaje))
        print(f"Email enviado a {email_destino}: {mensaje}")

    def ver_emails(self):
        for email, mensaje in self.emails:
            print(f"{email}: {mensaje}")    