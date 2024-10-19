from class_App import Aplicacion
from class_Celular import Celular

class Telefono(Aplicacion):
    def __init__(self):
        super().__init__(4,'Telefono')
        self.ultima_llamada = 0
        self.ultima_mensajeria = 0
        self.ultima_email = 0
        

    def hacer_llamada(self, hora):  
        if hora > self.ultima_llamada:  
            self.ultima_llamada = hora  
            print(f"Haciendo llamada a {self.nombre} a las {hora}") 
    
    #USAR CONJUNTOS PARA TELEFONO
    #METODOS CHATGPT DE TELEFONO 
    def realizar_llamada(self, numero_destino):
        if self.encendido and not self.bloqueado:
            print(f"Llamando a {numero_destino}...")
            self.llamadas.append(numero_destino)
        else:
            print("El telefono esta apagado o bloqueado.")

    def recibir_llamada(self, numero_remitente):
        if self.encendido:
            print(f"Recibiendo llamada de {numero_remitente}...")
            self.llamadas.append(numero_remitente)
        else:
            print("El telefono esta apagado.")

    def terminar_llamada(self):
        print("Llamada terminada.")