
from datetime import datetime

class Central :
    
    def __init__(self):
        self.dispositivos_registrados= {}
        self.registro_llamadas=[]
        self.registro_sms=[]
        

    def agregar_celular(self,celular):
        self.dispositivos_registrados[celular.numero_telefono]=celular
    
    def eliminar_dispositivo(self, numero):
        if numero in self.dispositivos_registrados:
            del self.dispositivos_registrados[numero]
            print('número  eliminado del registro')
        else:
            print("El número  no está registrado en la central")
    
    def estado_dispositivo(self, numero):
            if numero not in self.dispositivos_registrados:
                print("El número  no está registrado en la central.")
                return False
        
            celular = self.dispositivos_registrados[numero]
            if not celular.encendido:
                print("El dispositivo  está apagado.")
                return False
            if celular.bloqueado:
                print("El dispositivo  está bloqueado.")
                return False
            return True

    def internet(self, numero):
        if numero not in self.dispositivos_registrados:
            print("El número no está registrado en la central.")
            return False
        
        celular = self.dispositivos_registrados[numero]
        if not celular.datos:
            print("El dispositivo  no tiene datos móviles activados.")
            return False
        return True
    
    
    def llamada(self,numero_emisor,numero_recive):
        if not self.estado_dispositivo(numero_emisor):
            print("Llamada fallida: El emisor no está disponible.")
            return 
        if not self.estado_dispositivo(numero_recive):
            print("Llamada fallida: El receptor no está disponible.")
            return

        print(f"Llamada conectada entre {numero_emisor} y {numero_recive}.")
        self.registro_llamadas.append((numero_emisor, numero_recive, "conectada",datetime.now()))
    
    def sms(self,numero_emisor,numero_recive,mensaje):
        if not self.estado_dispositivo(numero_emisor):
            print("SMS fallido: El emisor no está disponible.")
            return  
        if not(self.estado_dispositivo(numero_recive)):
            print('SMS fallido: El receptor no esta diponible')
        print(f"SMS enviado de {numero_emisor} a {numero_recive}: {mensaje}")
        self.registro_sms.append((numero_emisor, numero_recive, mensaje))
    
        