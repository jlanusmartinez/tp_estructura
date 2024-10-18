from class_App import *
from class_central import *

class Celular:
    def _init_(self, id_unico, nombre, modelo, sistema_operativo, version, memoria_ram, almacenamiento, numero_telefono,red):
        self.id_unico = id_unico
        self.nombre = nombre
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.version = version
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento
        self.numero_telefono = numero_telefono
        self.encendido = False
        self.bloqueado = True
        self.red=True
        self.aplicaciones = []
        self.tienda = Tienda()

    def encender(self):
        self.encendido = True
        print("El teléfono está encendido.")
        self.activar_red_movil()

    def apagar(self):
        self.encendido = False
        print("El teléfono está apagado.")

    def bloquear(self):
        self.bloqueado = True
        print("El teléfono está bloqueado.")

    def desbloquear(self):
        self.bloqueado = False
        print("El teléfono está desbloqueado.")

    def abrir_aplicacion(self, aplicacion):
        if aplicacion in self.aplicaciones and self.encendido:
            print(f"Abriendo {aplicacion}...")
            # Lógica de interacción según la aplicación
        else:
            print("No se puede abrir la aplicación.")



    