from class_App import *
from datetime import *


class Email(Aplicacion):
    def __init__(self):
        super().__init__(3,'Email')
        self.emails_recibidos = []
    
    def recibir_email(self, email_origen, mensaje, fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        self.emails_recibidos.append({'origen': email_origen, 'mensaje': mensaje, 'leido': False, 'fecha':fecha})
        print(f"Email recibido de {email_origen}: {mensaje} el {fecha}")

    def ver_emails_por_leidos(self):
        no_leidos = []
        leidos = []

        # Iteramos sobre los correos para separarlos en dos listas
        for email in self.emails_recibidos:
            if email['leido']:
                leidos.append(email)
            else:
                no_leidos.append(email)
        
        print("Correos no leídos:")
        for email in no_leidos:
            print(f"{email['origen']}: {email['mensaje']} el: {email['fecha']}")
        
        print("\nCorreos leídos:")
        for email in leidos:
            print(f"{email['origen']}: {email['mensaje']} el {email['fecha']}")
        
        # Marcamos los correos no leídos como leídos después de mostrarlos
        for email in no_leidos:
            email['leido'] = True
    
    def ver_emails_por_fecha(self):
        # Ordenamos los correos por fecha (más reciente primero)
        emails_ordenados = sorted(self.emails_recibidos, key=lambda email: email['fecha'], reverse=True)

        print("Correos (ordenados por fecha):")
        for email in emails_ordenados:
            if email['leido']:
                leido_status = "Leído"
            else:   
                leido_status = "No leído"
            print(f"{email['origen']}: {email['mensaje']} el: {email['fecha']} ({leido_status})")
        
        # Marcamos los correos no leídos como leídos después de mostrarlos
        for email in emails_ordenados:
            if not email['leido']:
                email['leido'] = True
            
            

            