from class_App import Aplicacion
from datetime import datetime
class Telefono(Aplicacion):
    def __init__(self,numero):
        super().__init__(4,'Telefono')
        self.numero=numero
        self.ultima_llamada = 0
        self.ultima_mensajeria = 0
        self.ultima_email = 0
        self.historial_llamadas_realizadas = set()  
        self.historial_llamadas_recibidas = set()  
        

    def hacer_llamada(self,numero_1): 
        if self.estado:
            self.historial_llamadas_realizadas.add(numero_1)
            self.central.llamada(self.numero, numero_1)
            if datetime.now() > self.ultima_llamada:  
                self.ultima_llamada = datetime.now()  
                print(f"Haciendo llamada a {self.nombre} a las {datetime.now()}") 
        else:
            print("La aplicación Teléfono no está abierta.") 
    
    
    #No estoy seguro de como funciona lo de recibir llamadas!!
    
    def recibir_llamada(self,numero): 
        if self.estado:
            self.historial_llamadas_recibidas.add(numero)

            if datetime.now() > self.ultima_llamada:  
                self.ultima_llamada = datetime.now()  
                print(f"Recibiendo llamada de {self.nombre} a las {datetime.now()}") 
        else:
            print("La aplicación Teléfono no está abierta.")    
    
    
