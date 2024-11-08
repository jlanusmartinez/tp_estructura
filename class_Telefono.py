from class_App import Aplicacion
from datetime import datetime,timedelta

class Telefono(Aplicacion):
    def __init__(self,numero):
        super().__init__(4,'Telefono')
        self.numero=numero
        self.ultima_llamada = 0
        self.ultima_mensajeria = 0
        self.ultima_email = 0
        self.ocupado_hasta=None
        self.registro_llamadas=[]
    
    def llamada_realizada(self,destinatario,duracion,hora):
        # Calcular el tiempo de finalización sumando la duración
        tiempo_finalizacion = hora + timedelta(minutes=duracion)

        # Guardar los datos de la llamada en el registro
        llamada = {
            'destinatario': destinatario,
            'hora_inicio': hora,
            'duracion_minutos': duracion,
            'tiempo_finalizacion': tiempo_finalizacion
        }
        self.registro_llamadas.append(llamada)
        self.ocupado_hasta = tiempo_finalizacion
    
    def recibir_llamada(self,emisor,duracion,hora):
        # Calcular el tiempo de finalización sumando la duración
        tiempo_finalizacion = hora + timedelta(minutes=duracion)

        # Guardar los datos de la llamada en el registro
        llamada = {
            'emisor': emisor,
            'hora_inicio': hora,
            'duracion_minutos': duracion,
            'tiempo_finalizacion': tiempo_finalizacion
        }
        self.registro_llamadas.append(llamada)
        self.ocupado_hasta = tiempo_finalizacion
    
    
    def imprimir_registro_emisor(self):
            if not self.registro_llamadas:
                print("No hay registros de llamadas.")
                return
        
            print("Registro de llamadas:")
            for llamada in self.registro_llamadas:
                print(f"- Destinatario: {llamada['destinatario']}, "
                  f"Hora de inicio: {llamada['hora_inicio']}, "
                  f"Duración: {llamada['duracion_minutos']} minutos, "
                  f"Tiempo de finalización: {llamada['tiempo_finalizacion']}")
    
    
    def imprimir_registro_destinatario(self):
            if not self.registro_llamadas:
                print("No hay registros de llamadas.")
                return
        
            print("Registro de llamadas:")
            for llamada in self.registro_llamadas:
                print(f"- Emisor: {llamada['emisor']}, "
                  f"Hora de inicio: {llamada['hora_inicio']}, "
                  f"Duración: {llamada['duracion_minutos']} minutos, "
                  f"Tiempo de finalización: {llamada['tiempo_finalizacion']}")
        

        

        
        
        








    
