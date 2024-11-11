from class_App import *  
from Estructuras import *  

# Clase Mensajeria que hereda de la clase Aplicacion
class Mensajeria(Aplicacion):
    
    # Constructor de la clase Mensajeria
    def __init__(self, numero_telefono):
        super().__init__(2, 'Mensajeria')  # Llama al constructor de Aplicacion con codigo 2 y nombre "Mensajeria"
        self.numero_telefono = numero_telefono  # Guarda el numero de telefono del usuario
        self.bandeja_sms = Pila()  # Crea una pila para almacenar los mensajes SMS

    # Metodo para enviar un SMS
    def enviar_sms(self, numero_destino, mensaje, fecha):
        mensaje_enviado = [f"Enviado a {numero_destino}: {mensaje}", f" el {fecha}"]  # Crea el mensaje a enviar
        self.bandeja_sms.apilar(mensaje_enviado)  # Agrega el mensaje a la pila de mensajes

    # Metodo para recibir un SMS
    def recibir_sms(self, numero_destino, mensaje, fecha):
        mensaje_recibido = [f"Recibido de {numero_destino}: {mensaje}", f" el {fecha}"]  # Crea el mensaje recibido
        self.bandeja_sms.apilar(mensaje_recibido)  # Agrega el mensaje a la pila de mensajes

    # Metodo para ver todos los SMS en la bandeja
    def ver_bandeja_sms(self):
        if self.bandeja_sms.esta_vacia():  # Verifica si la pila de mensajes esta vacia
            print("La bandeja de SMS esta vacia.")  # Imprime mensaje si no hay SMS
        else:
            print(f"Bandeja de SMS de {self.numero_telefono}:")  # Imprime el numero de telefono
            mensajes = []  # Lista temporal para almacenar los mensajes extraidos
            while not self.bandeja_sms.esta_vacia():
                mensaje = self.bandeja_sms.desapilar()  # Extrae el mensaje de la pila
                mensajes.append(mensaje)  # Agrega el mensaje a la lista temporal
                print(mensaje[0] + mensaje[1])  # Imprime el mensaje completo
            
            # Vuelve a apilar los mensajes para restaurar el estado original de la pila
            for mensaje in mensajes:
                self.bandeja_sms.apilar(mensaje)

    # Metodo para eliminar un SMS especifico
    def eliminar_sms(self, numero_destino, mensaje):
        mensaje_a_eliminar = f"Enviado a {numero_destino}: {mensaje}"  # Define el mensaje a eliminar
        mensajes_temp = []  # Lista temporal para almacenar mensajes no eliminados
        mensaje_eliminado = False  # Bandera para indicar si se encontro el mensaje

        # Desapilar los mensajes uno a uno hasta encontrar el mensaje a eliminar
        while not self.bandeja_sms.esta_vacia():
            sms = self.bandeja_sms.desapilar()  # Extrae el mensaje de la pila
            if sms[0] == mensaje_a_eliminar:  # Verifica si el mensaje coincide con el mensaje a eliminar
                mensaje_eliminado = True  # Marca que se encontro el mensaje
                print(f"SMS enviado a {numero_destino} eliminado.")  # Informa que el mensaje fue eliminado
                break  # Detiene el bucle una vez que se elimino el mensaje
            else:
                mensajes_temp.append(sms)  # Agrega el mensaje no eliminado a la lista temporal

        # Vuelve a apilar los mensajes que no se eliminaron para restaurar la pila
        for sms in mensajes_temp:
            self.bandeja_sms.apilar(sms)

        if not mensaje_eliminado:  # Si no se encontro el mensaje
            print("SMS no encontrado en la bandeja del emisor.")  # Informa que no se encontro el mensaje


'OBSERVACION: CUANDO ELIMINO UN MENSAJE, SE ELIMINA EL MENSAJE DE LA CASILLA PERO SOLO DEL QUE LO MANDO, NO DEL QUE LO RECIBE'
'TOMAMOS ESTO COMO SI FUESE EL: ELIMINA PARA TI'
    
