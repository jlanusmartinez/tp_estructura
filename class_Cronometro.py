from class_App import*
import time

class Cronometro(Aplicacion):
    def __init__(self):
        super().__init__(7,"Cronometro")
        self.iniciado = False
        self.tiempo_inicio = 0

    def iniciar(self):
        #Inicia el cronometro.
        if self.estado:
            self.iniciado = True
            self.tiempo_inicio = time.time()
            print("Cronometro iniciado...")
        else:
            print("La aplicacion Cronometro no esta abierta.")

    def detener(self):
        #Detiene el cronometro y muestra el tiempo transcurrido.
        if self.estado:
            if self.iniciado:
                tiempo_transcurrido = time.time() - self.tiempo_inicio
                self.iniciado = False
                print(f"Cronometro detenido. Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos.")
            else:
                print("El cronometro no esta en ejecucion.")
        else:
            print("La aplicacion Cronometro no esta abierta.")