from class_App import Aplicacion 
from datetime import datetime, timedelta  

class Telefono(Aplicacion):  # Define la clase Telefono que hereda de Aplicacion
    def __init__(self, numero):  # Método de inicialización con el parámetro numero
        super().__init__(4, 'Telefono')  # Llama al constructor de la clase base Aplicacion con dos argumentos
        self.numero = numero  # Inicializa la variable de instancia numero
        self.ultima_llamada = 0  # Inicializa la variable de instancia ultima_llamada en 0
        self.ultima_mensajeria = 0  # Inicializa la variable de instancia ultima_mensajeria en 0
        self.ultima_email = 0  # Inicializa la variable de instancia ultima_email en 0
        self.ocupado_hasta = None  # Inicializa la variable de instancia ocupado_hasta en None
        self.registro_llamadas = []  # Inicializa registro_llamadas como una lista vacía

    def llamada_realizada(self, destinatario, duracion, hora):  # Define el método llamada_realizada con tres parámetros
        tiempo_finalizacion = hora + timedelta(minutes=duracion)  # Calcula el tiempo de finalización de la llamada

        # Crea un diccionario llamada con los datos de la llamada
        llamada = {
            'destinatario': destinatario,
            'hora_inicio': hora,
            'duracion_minutos': duracion,
            'tiempo_finalizacion': tiempo_finalizacion
        }
        self.registro_llamadas.append(llamada)  # Añade el diccionario llamada a la lista registro_llamadas
        self.ocupado_hasta = tiempo_finalizacion  # Actualiza la variable ocupado_hasta con el tiempo de finalización

    def recibir_llamada(self, emisor, duracion, hora):  # Define el método recibir_llamada con tres parámetros
        tiempo_finalizacion = hora + timedelta(minutes=duracion)  # Calcula el tiempo de finalización de la llamada

        # Crea un diccionario llamada con los datos de la llamada recibida
        llamada = {
            'emisor': emisor,
            'hora_inicio': hora,
            'duracion_minutos': duracion,
            'tiempo_finalizacion': tiempo_finalizacion
        }
        self.registro_llamadas.append(llamada)  # Añade el diccionario llamada a la lista registro_llamadas
        self.ocupado_hasta = tiempo_finalizacion  # Actualiza la variable ocupado_hasta con el tiempo de finalización

    def imprimir_registro_emisor(self):  # Define el método imprimir_registro_emisor
        if not self.registro_llamadas:  # Verifica si la lista registro_llamadas está vacía
            print("No hay registros de llamadas.")  # Imprime un mensaje si no hay registros
            return

        print("Registro de llamadas:")  # Imprime un encabezado
        for llamada in self.registro_llamadas:  # Itera sobre cada diccionario llamada en registro_llamadas
            print(f"- Destinatario: {llamada['destinatario']}, "
                  f"Hora de inicio: {llamada['hora_inicio']}, "
                  f"Duración: {llamada['duracion_minutos']} minutos, "
                  f"Tiempo de finalización: {llamada['tiempo_finalizacion']}")  # Imprime los detalles de la llamada

    def imprimir_registro_destinatario(self):  # Define el método imprimir_registro_destinatario
        if not self.registro_llamadas:  # Verifica si la lista registro_llamadas está vacía
            print("No hay registros de llamadas.")  # Imprime un mensaje si no hay registros
            return

        print("Registro de llamadas:")  # Imprime un encabezado
        for llamada in self.registro_llamadas:  # Itera sobre cada diccionario llamada en registro_llamadas
            print(f"- Emisor: {llamada['emisor']}, "
                  f"Hora de inicio: {llamada['hora_inicio']}, "
                  f"Duración: {llamada['duracion_minutos']} minutos, "
                  f"Tiempo de finalización: {llamada['tiempo_finalizacion']}")  # Imprime los detalles de la llamada








    
