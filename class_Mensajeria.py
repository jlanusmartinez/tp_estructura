from class_App import *
from class_pila import *
#Use pila
class Mensajeria(Aplicacion):
    def __init__(self, numero_telefono):
        super().__init__(2,'Mensajeria')
        self.numero_telefono = numero_telefono
        self.bandeja_sms = Pila()
#CODIGO VIEJO (NO ANDA) LANUS
#     def enviar_sms(self, numero_destino, mensaje):
#         if self.estado:
#             self.bandeja_sms.apilar(f"Enviado a {numero_destino}: {mensaje}")
#             print(f"SMS enviado a {numero_destino}: {mensaje}")
#         else :
#             print('Aplicacion cerrada')
        
#     def recibir_sms(self, numero_destino, mensaje):
#         if self.estado:
#             self.bandeja_sms.apilar(f"Recibido: {numero_destino}: {mensaje}")
#             print(f"SMS recibido de {numero_destino}: {mensaje}")
#         else :
#             print('Aplicacion cerrada')       
            
            
#     def ver_bandeja_sms(self):
#         """Muestra todos los mensajes en la bandeja de SMS."""
#         if self.bandeja_sms.esta_vacia():
#             print("No hay mensajes en la bandeja.")
#         else:
#             print("Bandeja de SMS:")
#             while not self.bandeja_sms.esta_vacia():
#                 print(self.bandeja_sms.desapilar())
                
#        # NI idea como se hacia hecho por gpt         
#         """""
#     def ver_sms(self):
#         for numero, mensaje in self.sms:
#             print(f"{numero}: {mensaje}")
    
#         """"" 

#     def eliminar_sms(self, indice):
#         if 0 <= indice < len(self.sms):
#             del self.central.sms[indice]
#             print("Mensaje eliminado.")   
            
# #PARA ELIMINAR EL MENSAJE LE TENGO QUE PASAR EL NOMBRE DE MI AMIGO Y EL MENSAJE TEXTUAL --> ARREGLAR

    def enviar_sms(self, numero_destino, mensaje,fecha):
            mensaje_enviado = f"Enviado a {numero_destino}: {mensaje} el {fecha}"
            self.bandeja_sms.apilar(mensaje_enviado)
    
    


    def recibir_sms(self, numero_destino, mensaje,fecha):
            mensaje_recibido = f"Recibido de {numero_destino}: {mensaje} el {fecha}"
            self.bandeja_sms.apilar(mensaje_recibido)

    
    def ver_bandeja_sms(self):
            if self.bandeja_sms.esta_vacia():
                print("La bandeja de SMS está vacía.")
            else:
                print("Bandeja de SMS:")
                mensajes = []
                while not self.bandeja_sms.esta_vacia():
                    mensaje = self.bandeja_sms.desapilar()
                    mensajes.append(mensaje)
                    print(mensaje)
                
                # Reapilar los mensajes para mantener la pila original
                for mensaje in mensajes:
                    self.bandeja_sms.apilar(mensaje)
    
    def eliminar_sms(self, numero_destino, mensaje):
        mensajes_temp = []
        mensaje_eliminado = False

        # Desapilar los mensajes hasta encontrar el que se quiere eliminar
        while not self.bandeja_sms.esta_vacia():
            sms = self.bandeja_sms.desapilar()
            if sms == f"Enviado a {numero_destino}: {mensaje}":
                mensaje_eliminado = True
                print(f"SMS de {numero_destino} eliminado.")
                break  # Salimos del bucle una vez encontrado el mensaje
            else:
                mensajes_temp.append(sms)  # Guardamos el mensaje en la lista temporal

        # Volver a apilar los mensajes que no se eliminaron
        for sms in mensajes_temp:
            self.bandeja_sms.apilar(sms)

        if not mensaje_eliminado:
            print("SMS no encontrado en la bandeja.")
    
