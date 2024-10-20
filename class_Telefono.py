from class_App import Aplicacion
from class_Celular import Celular
from datetime import datetime
class Telefono(Aplicacion):
    def __init__(self,central,celular):
        super().__init__(4,'Telefono')
        self.central=central
        self.celular=celular
        self.ultima_llamada = 0
        self.ultima_mensajeria = 0
        self.ultima_email = 0
        self.historial_llamadas_realizadas = set()  
        self.historial_llamadas_recibidas = set()  
        

    def hacer_llamada(self,numero): 
        if self.abierta:
            self.historial_llamadas_realizadas.add(numero)
            self.central.llamada(self.celular.numero, numero)
            if datetime.now() > self.ultima_llamada:  
                self.ultima_llamada = datetime.now()  
                print(f"Haciendo llamada a {self.nombre} a las {datetime.now()}") 
        else:
            print("La aplicación Teléfono no está abierta.") 
    
    
    #No estoy seguro de como funciona lo de recibir llamadas!!
    
    def recibir_llamada(self,numero): 
        if self.abierta:
            self.historial_llamadas_recibidas.add(numero)

            if datetime.now() > self.ultima_llamada:  
                self.ultima_llamada = datetime.now()  
                print(f"Recibiendo llamada de {self.nombre} a las {datetime.now()}") 
        else:
            print("La aplicación Teléfono no está abierta.")    
    
    
    
    
    
    
    """""
    #USAR CONJUNTOS PARA TELEFONO
    #METODOS CHATGPT DE TELEFONO 
    def realizar_llamada(self, numero_destino):
        if self.encendido and not self.bloqueado:
            print(f"Llamando a {numero_destino}...")
            self.llamadas.append(numero_destino)
        else:
            print("El teléfono está apagado o bloqueado.")

    def recibir_llamada(self, numero_remitente):
        if self.encendido:
            print(f"Recibiendo llamada de {numero_remitente}...")
            self.llamadas.append(numero_remitente)
        else:
            print("El teléfono está apagado.")

    def terminar_llamada(self):
        print("Llamada terminada.")
        
        """""