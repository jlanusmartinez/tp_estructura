
from datetime import datetime
from class_Celular import Celular
from class_Telefono import *
from class_Mensajeria import *
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
    #PROBAR FUNCIONAMIENTO
    
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
    
    'CODIGO VIEJO DE JOACO'
    # def llamada(self,numero_emisor,numero_recibe,duracion):

    #     if not self.estado_dispositivo(numero_emisor):
    #         print("Llamada fallida: El emisor no está disponible.")
    #         return 
    #     if not self.estado_dispositivo(numero_recibe):
    #         print("Llamada fallida: El receptor no está disponible.")
    #         return
    #     celular_1= self.dispositivos_registrados.get(numero_emisor)
    #     celular_2= self.dispositivos_registrados.get(numero_recibe)
    #     hora_actual=datetime.now()
    #     if celular_1.telefono.ocupado_hasta and hora_actual < celular_1.telefono.ocupado_hasta:
    #             print(f"No se puede realizar la llamada. El teléfono estará ocupado hasta: {celular_1.telefono.ocupado_hasta}.")
    #             return
    #     celular_1.telefono.llamada_realizada(numero_recibe,duracion,datetime.now())

    #     print(f"Llamada conectada entre {numero_emisor} y {numero_recibe}.")
    #     self.registro_llamadas.append((numero_emisor, numero_recibe, "conectada",datetime.now()))
    
    def llamada(self, numero_emisor, numero_recibe, duracion):
        if not self.estado_dispositivo(numero_emisor):
            print("Llamada fallida: El emisor no está disponible.")
            return 
        
        if not self.estado_dispositivo(numero_recibe):
            print("Llamada fallida: El receptor no está disponible.")
            return
        
        celular_1 = self.dispositivos_registrados.get(numero_emisor)
        celular_2 = self.dispositivos_registrados.get(numero_recibe)
        
        hora_actual = datetime.now()
        
        # Verificar si el receptor está ocupado
        if celular_2.telefono.ocupado_hasta and hora_actual < celular_2.telefono.ocupado_hasta:
            print(f"No se puede realizar la llamada. El receptor está ocupado hasta: {celular_2.telefono.ocupado_hasta}.")
            return
        
        # Verificar si el emisor está ocupado
        if celular_1.telefono.ocupado_hasta and hora_actual < celular_1.telefono.ocupado_hasta:
            print(f"No se puede realizar la llamada. El emisor está ocupado hasta: {celular_1.telefono.ocupado_hasta}.")
            return
        
        # Si ambos están disponibles, registrar la llamada
        celular_1.telefono.llamada_realizada(numero_recibe, duracion, datetime.now())
        print(f"Llamada conectada entre {numero_emisor} y {numero_recibe}.")
        self.registro_llamadas.append((numero_emisor, numero_recibe, "conectada", datetime.now()))
    
    def enviar_sms(self,numero_emisor,numero_recibe,mensaje,fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        if not self.estado_dispositivo(numero_emisor):
            print("SMS fallido: El emisor no está disponible.")
            return  
        if not(self.estado_dispositivo(numero_recibe)):
            print('SMS fallido: El receptor no esta diponible')
        print(f"SMS enviado de {numero_emisor} a {numero_recibe}: {mensaje} el {fecha}")
        self.registro_sms.append((numero_emisor, numero_recibe, mensaje,fecha))
        
        celular_1 = self.dispositivos_registrados.get(numero_emisor)
        celular_2 = self.dispositivos_registrados.get(numero_recibe)
        
        celular_1.mensajeria.enviar_sms(numero_recibe,mensaje,fecha)
        celular_2.mensajeria.recibir_sms(numero_emisor,mensaje,fecha)
        print('SMS enviado.')  
        
        
    def eliminar_sms(self, numero_emisor, numero_recibe, mensaje):
        for sms in self.registro_sms:
            if sms[0] == numero_emisor and sms[1] == numero_recibe and sms[2] == mensaje:
                self.registro_sms.remove(sms)
                print(f"SMS de {numero_emisor} a {numero_recibe} eliminado.")
                return
        print("SMS no encontrado en el registro.")  
        
print('hola')
        
    
        