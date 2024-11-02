
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
        celular_1.hacer_llamada(numero_recibe, duracion, datetime.now())
        print(f"Llamada conectada entre {numero_emisor} y {numero_recibe}.")
        self.registro_llamadas.append((numero_emisor, numero_recibe, "conectada", datetime.now()))
        
        
#MENSAJERIA
    
    def enviar_sms(self,numero_emisor,numero_recibe,mensaje,fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        if not self.estado_dispositivo(numero_emisor):
            print("SMS fallido: El emisor no está disponible.")
            return  
        # if not(self.estado_dispositivo(numero_recibe)):
        #     print('SMS fallido: El receptor no esta diponible')
            #CAMBIAR ESTO

        
        celular_1 = self.dispositivos_registrados.get(numero_emisor)
        celular_2 = self.dispositivos_registrados.get(numero_recibe)
        if celular_1.encendido and not celular_1.bloqueado:
            if celular_1.validar_aplicacion(2):
                    if celular_1.mensajeria.estado:     
                            celular_2.recibir_sms(numero_emisor,mensaje,fecha)      
                            celular_1.enviar_sms(numero_recibe,mensaje,fecha)
                            print(f"SMS enviado de {celular_1.nombre} a {celular_2.nombre}: {mensaje} el {fecha}")
                            self.registro_sms.append((numero_emisor, numero_recibe, mensaje,fecha))
                    
                    else:
                        print('Aplicacion no abierta')
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')      
        
         
        
        
        
    def eliminar_sms(self, numero_emisor, numero_recibe, mensaje):
            # Obtener los dispositivos registrados
            celular_1 = self.dispositivos_registrados.get(numero_emisor)
            celular_2 = self.dispositivos_registrados.get(numero_recibe)
            
            if celular_1.encendido and not celular_1.bloqueado:
                if celular_1.validar_aplicacion(2):        
                    if celular_1.mensajeria.estado: 

                        # Acceder al objeto de Mensajeria del emisor
                        mensajeria_emisor = celular_1.mensajeria

                        # Eliminar el mensaje usando el método de Mensajeria
                        mensajeria_emisor.eliminar_sms(numero_recibe, mensaje)

                        # También eliminar el registro de SMS
                        for sms in self.registro_sms:
                            if sms[0] == numero_emisor and sms[1] == numero_recibe and sms[2] == mensaje:
                                self.registro_sms.remove(sms)
                                print(f"El SMS {mensaje} de {celular_1.nombre} a {celular_2.nombre} ha sido eliminado del registro.")
                                return
                    else:
                        print('Aplicacion no abierta')
                else: 
                    print('Aplicacion:Mensajeria no descargada')
            else:
                print('El celular tiene que estar encendido y desbloqueado') 
    
    

               
            
        

        
    
        