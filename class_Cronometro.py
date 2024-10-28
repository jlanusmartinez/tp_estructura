from class_App import*
import time

class Cronometro(Aplicacion):
    def __init__(self):
        super().__init__(7,"Cronómetro")
        self.iniciado = False
        self.tiempo_inicio = 0

    def iniciar(self):
        """Inicia el cronómetro."""
        if self.abierta:
            self.iniciado = True
            self.tiempo_inicio = time.time()
            print("Cronómetro iniciado...")
        else:
            print("La aplicación Cronómetro no está abierta.")

    def detener(self):
        """Detiene el cronómetro y muestra el tiempo transcurrido."""
        if self.abierta:
            if self.iniciado:
                tiempo_transcurrido = time.time() - self.tiempo_inicio
                self.iniciado = False
                print(f"Cronómetro detenido. Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos.")
            else:
                print("El cronómetro no está en ejecución.")
        else:
            print("La aplicación Cronómetro no está abierta.")