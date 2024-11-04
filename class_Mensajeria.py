from class_App import *
from Estructuras import *
#Use pila
class Mensajeria(Aplicacion):
    def __init__(self, numero_telefono):
        super().__init__(2,'Mensajeria')
        self.numero_telefono = numero_telefono
        self.bandeja_sms = Pila()
 
            
# #PARA ELIMINAR EL MENSAJE LE TENGO QUE PASAR EL NOMBRE DE MI AMIGO Y EL MENSAJE TEXTUAL --> ARREGLAR

    def enviar_sms(self, numero_destino, mensaje,fecha):
            mensaje_enviado = [f"Enviado a {numero_destino}: {mensaje}", f" el {fecha}"]
            self.bandeja_sms.apilar(mensaje_enviado)
    
    
    def recibir_sms(self, numero_destino, mensaje,fecha):
            mensaje_recibido = [f"Recibido de {numero_destino}: {mensaje}", f" el {fecha}"]
            self.bandeja_sms.apilar(mensaje_recibido)

    
    def ver_bandeja_sms(self):
            if self.bandeja_sms.esta_vacia():
                print("La bandeja de SMS esta vacia.")
            else:
                print(f"Bandeja de SMS de {self.numero_telefono}:")
                mensajes = []
                while not self.bandeja_sms.esta_vacia():
                    mensaje = self.bandeja_sms.desapilar()
                    mensajes.append(mensaje)
                    print(mensaje[0] + mensaje[1])
                
                # Reapilar los mensajes para mantener la pila original
                for mensaje in mensajes:
                    self.bandeja_sms.apilar(mensaje)
    

    def eliminar_sms(self, numero_destino, mensaje):
        mensaje_a_eliminar = f"Enviado a {numero_destino}: {mensaje}"
        mensajes_temp = []
        mensaje_eliminado = False

        # Desapilar los mensajes hasta encontrar el que se quiere eliminar
        while not self.bandeja_sms.esta_vacia():
            sms = self.bandeja_sms.desapilar()
            if sms[0] == mensaje_a_eliminar:
                mensaje_eliminado = True
                print(f"SMS enviado a {numero_destino} eliminado.")
                break  # Salimos del bucle una vez encontrado el mensaje
            else:
                mensajes_temp.append(sms)  # Guardamos el mensaje en la lista temporal

        # Volver a apilar los mensajes que no se eliminaron
        for sms in mensajes_temp:
            self.bandeja_sms.apilar(sms)

        if not mensaje_eliminado:
            print("SMS no encontrado en la bandeja del emisor.")



       

    
    
    
