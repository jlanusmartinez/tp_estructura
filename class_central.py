
from datetime import datetime
from class_Celular import Celular
from class_Telefono import *
from class_Mensajeria import *
import pickle
import csv
from class_registro_dispositivo import Registro_dispositivos
class Central :
    
    def __init__(self):
        self.dispositivos_registrados=Registro_dispositivos()
        self.registro_llamadas=[]
        self.registro_sms=[]
        

    def agregar_celular(self,celular):
        self.dispositivos_registrados[celular.numero_telefono]=celular
    
    def eliminar_dispositivo(self, numero):
        if numero in self.dispositivos_registrados:
            del self.dispositivos_registrados[numero]
            print('numero  eliminado del registro')
        else:
            print("El numero  no esta registrado en la central")
    
    def estado_dispositivo(self, numero):
            if numero not in self.dispositivos_registrados:
                print("El numero  no esta registrado en la central.")
                return False
        
            celular = self.dispositivos_registrados[numero]
            if not celular.encendido:
                print("El dispositivo  esta apagado.")
                return False
            if celular.bloqueado:
                print("El dispositivo  esta bloqueado.")
                return False
            return True

    def internet(self, numero):
        if numero not in self.dispositivos_registrados:
            print("El numero no esta registrado en la central.")
            return False
        
        celular = self.dispositivos_registrados[numero]
        if not celular.datos:
            print("El dispositivo  no tiene datos moviles activados.")
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
        
        if not celular_1.estado_red_movil:
            print ("Llamada fallida: El emisor no tiene red activada.")
            return 
        if not celular_1.estado_datos:
             print('Llamada fallida: El emisor no tiene datos activados.')
        if not celular_2.estado_red_movil or not celular_2.estado_datos:
            print ("Llamada fallida: El receptor no tiene red activada ni datos activados.")
            return
        if celular_1.validar_aplicacion(4):
                    if celular_1.telefono.estado:
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
                            celular_2.telefono.recibir_llamada(numero_emisor, duracion, datetime.now())
                            print(f"Llamada conectada entre {numero_emisor} y {numero_recibe}.")
                            self.registro_llamadas.append((numero_emisor, numero_recibe, "conectada", datetime.now()))   
                    
                    else:
                        print('Aplicacion no abierta')
        else: 
                print('Aplicacion:Telefono no descargada')

        
        hora_actual = datetime.now()
        
       
        
        
#MENSAJERIA
    
    def enviar_sms(self,numero_emisor,numero_recibe,mensaje,fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        if not self.estado_dispositivo(numero_emisor):
            print("SMS fallido: El emisor no esta disponible.")
            return  

        
        celular_1 = self.dispositivos_registrados.get(numero_emisor)
        celular_2 = self.dispositivos_registrados.get(numero_recibe)

        if not celular_1.estado_red_movil:
            print ("Llamada fallida: El emisor no tiene red activada.")
            return 
        if not celular_1.estado_datos:
             print('Llamada fallida: El emisor no tiene datos activados.')
        if not celular_2.estado_red_movil or not celular_2.estado_datos:
            print ("Llamada fallida: El receptor no tiene red activada ni datos activados.")
            return
        if celular_1.encendido and not celular_1.bloqueado:
            if celular_1.validar_aplicacion(2):
                    if celular_1.mensajeria.estado:     
                            celular_2.recibir_sms(numero_emisor,mensaje,fecha)      
                            celular_1.enviar_sms(numero_recibe,mensaje,fecha)
                            print(f"SMS enviado de {celular_1.nombre} a {celular_2.nombre}: '{mensaje}' el {fecha}")
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

                        # Eliminar el mensaje usando el metodo de Mensajeria
                        mensajeria_emisor.eliminar_sms(numero_recibe, mensaje)

                        # Tambien eliminar el registro de SMS
                        for sms in self.registro_sms:
                            if sms[0] == numero_emisor and sms[1] == numero_recibe and sms[2] == mensaje:
                                self.registro_sms.remove(sms)
                                print(f"El SMS '{mensaje}' de {celular_1.nombre} a {celular_2.nombre} ha sido eliminado del registro.")
                                return
                    else:
                        print('Aplicacion no abierta')
                else: 
                    print('Aplicacion:Mensajeria no descargada')
            else:
                print('El celular tiene que estar encendido y desbloqueado') 
    
    

    def guardar_datos(self): #GUARDAR datos  
        try: 
           
            with open('registro_llamadas.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.registro_llamadas)
            with open('registro_sms.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.registro_sms)
            
            print("Datos guardados correctamente.")
        except:
            print("Error al guardar los datos.")
        
    
    def cargar_datos(self): #CARGAR datos
        
        try:
            
                
            with open('registro_llamadas.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    self.registro_llamadas.append(row)
            with open('registro_sms.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    self.registro_sms.append(row)

            print("Datos cargadas correctamente.")  
        except:
            print("Error al cargar los datos.")
              
            
        

        
    
        