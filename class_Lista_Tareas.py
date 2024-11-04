from Estructuras import ListaEnlazada
from class_App import Aplicacion

class Lista_Tareas(Aplicacion):
    def __init__(self):
        super().__init__(9,'Lista_Tareas')
        self.lista_tareas = ListaEnlazada()

    def agregar_tarea(self, tarea):
        self.lista_tareas.agregar(tarea)
        print(f"Tarea '{tarea}' agregada.")

    def mostrar_tareas(self):
        print("Lista de Tareas:")
        self.lista_tareas.mostrar()

    def eliminar_tarea(self, tarea):
        if self.lista_tareas.eliminar(tarea):
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print(f"Tarea '{tarea}' no encontrada.")

