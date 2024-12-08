
from datetime import datetime
from class_Celular import Celular
from class_Telefono import *
from class_Mensajeria import *
import pickle
import csv
from class_registro_dispositivo import Registro_dispositivos
class Central :
    
    def __init__(self):
        self.dispositivos_registrados = Registro_dispositivos()
        self.registro_llamadas = []
        self.registro_sms = []
        self.centrales_conectadas = []  # Lista de otras centrales conectadas


    
    def conectar_central(self, otra_central):
        if otra_central not in self.centrales_conectadas:
            self.centrales_conectadas.append(otra_central)
            otra_central.centrales_conectadas.append(self)  # Conexión bidireccional
            print("Centrales conectadas correctamente.")
        else:
            print("Las centrales ya están conectadas.")

        

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
        
        # Buscar al receptor en esta central
        receptor = self.dispositivos_registrados.get(numero_recibe)
        
        # Si el receptor no está en esta central, buscar en las centrales conectadas
        if not receptor:
            for central in self.centrales_conectadas:
                receptor = central.dispositivos_registrados.get(numero_recibe)
                if receptor:
                    otra_central = central
                    break
            else:
                print("Llamada fallida: El receptor no está registrado en esta central ni en las conectadas.")
                return
        
        # Validar estado del receptor en la central correspondiente
        if not self.estado_dispositivo(numero_emisor) or not otra_central.estado_dispositivo(numero_recibe):
            print("Llamada fallida: El receptor no está disponible.")
            return
        
        emisor = self.dispositivos_registrados[numero_emisor]
        
        # Validar estado de red y datos
        if not emisor.estado_red_movil or not emisor.estado_datos:
            print("Llamada fallida: El emisor no tiene red o datos activados.")
            return
        
        if not receptor.estado_red_movil or not receptor.estado_datos:
            print("Llamada fallida: El receptor no tiene red o datos activados.")
            return
        
        # Verificar ocupación
        hora_actual = datetime.now()
        if emisor.telefono.ocupado_hasta and hora_actual < emisor.telefono.ocupado_hasta:
            print(f"El emisor está ocupado hasta: {emisor.telefono.ocupado_hasta}.")
            return
        
        if receptor.telefono.ocupado_hasta and hora_actual < receptor.telefono.ocupado_hasta:
            print(f"El receptor está ocupado hasta: {receptor.telefono.ocupado_hasta}.")
            return
        
        # Registrar llamada en ambas centrales
        emisor.hacer_llamada(numero_recibe, duracion, hora_actual)
        receptor.telefono.recibir_llamada(numero_emisor, duracion, hora_actual)
        print(f"Llamada conectada entre {numero_emisor} y {numero_recibe}.")
        self.registro_llamadas.append((numero_emisor, numero_recibe, "conectada", hora_actual))
        if receptor in otra_central.dispositivos_registrados.values():
            otra_central.registro_llamadas.append((numero_emisor, numero_recibe, "conectada", hora_actual))

        
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
              
            
        

        
    
        