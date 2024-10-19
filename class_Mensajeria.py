from class_App import Aplicacion
from class_Celular import Celular

class Mensajeria(Aplicacion):
    def __init__(self):
        super().__init__(2,'Mensajeria')
        self.sms = []

    def enviar_sms(self, numero_destino, mensaje):
        if self.encendido and not self.bloqueado:   
            self.sms.append([numero_destino, mensaje])
            print(f"SMS enviado a {numero_destino}: {mensaje}")

    def ver_sms(self):
        for numero, mensaje in self.sms:
            print(f"{numero}: {mensaje}")
    

    def eliminar_sms(self, indice):
        if 0 <= indice < len(self.sms):
            del self.sms[indice]
            print("Mensaje eliminado.")   
            
#PARA ELIMINAR EL MENSAJE LE TENGO QUE PASAR EL NOMBRE DE MI AMIGO Y EL MENSAJE TEXTUAL --> ARREGLAR
 