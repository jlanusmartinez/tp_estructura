from class_App import *
from class_pila import *
from class_Celular import *
#Use pila
class Mensajeria(Aplicacion):
    def __init__(self,central,celular):
        super().__init__(2,'Mensajeria')
        self.central=central
        self.numero_telefono = numero_telefono
        self.bandeja_sms = Pila()

    def enviar_sms(self, numero_destino, mensaje):
        if self.estado:
            self.central.sms(self.celular.numero,numero_destino,mensaje)
            self.bandeja_sms.apilar(f"Enviado a {numero_destino}: {mensaje}")
            print(f"SMS enviado a {numero_destino}: {mensaje}")
        else :
            print('Aplicacion cerrada')
        
    def recibir_sms(self, numero_destino, mensaje):
        if self.estado:
            self.central.sms(self.celular.numero_telefono,numero_destino,mensaje)
            self.bandeja_sms.apilar(f"Recibido: {numero_destino}: {mensaje}")
            print(f"SMS recibido de {numero_destino}: {mensaje}")
        else :
            print('Aplicacion cerrada')       
            
            
    def ver_bandeja_sms(self):
        """Muestra todos los mensajes en la bandeja de SMS."""
        if self.bandeja_sms.esta_vacia():
            print("No hay mensajes en la bandeja.")
        else:
            print("Bandeja de SMS:")
            while not self.bandeja_sms.esta_vacia():
                print(self.bandeja_sms.desapilar())
                
       # NI idea como se hacia hecho por gpt         
        """""
    def ver_sms(self):
        for numero, mensaje in self.sms:
            print(f"{numero}: {mensaje}")
    
        """"" 

    def eliminar_sms(self, indice):
        if 0 <= indice < len(self.sms):
            del self.central.sms[indice]
            print("Mensaje eliminado.")   
            
#PARA ELIMINAR EL MENSAJE LE TENGO QUE PASAR EL NOMBRE DE MI AMIGO Y EL MENSAJE TEXTUAL --> ARREGLAR
 