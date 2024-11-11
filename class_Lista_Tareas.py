from Estructuras import ListaEnlazada  
from class_App import Aplicacion  

# Clase Lista_Tareas que hereda de la clase Aplicacion
class Lista_Tareas(Aplicacion):
    
    # Constructor de la clase Lista_Tareas
    def __init__(self):
        super().__init__(9, 'Lista_Tareas')  # Llama al constructor de la clase base Aplicacion con codigo 9 y nombre 'Lista_Tareas'
        self.lista_tareas = ListaEnlazada()  # Crea una instancia de ListaEnlazada para almacenar las tareas

    # Metodo para agregar una tarea a la lista
    def agregar_tarea(self, tarea):
        self.lista_tareas.agregar(tarea)  # Llama al metodo agregar de ListaEnlazada para agregar la tarea
        print(f"Tarea '{tarea}' agregada.")  # Muestra un mensaje de confirmacion de que la tarea fue agregada

    # Metodo para mostrar todas las tareas de la lista
    def mostrar_tareas(self):
        print("Lista de Tareas:")  # Muestra el encabezado para la lista de tareas
        self.lista_tareas.mostrar()  # Llama al metodo mostrar de ListaEnlazada para imprimir todas las tareas

    # Metodo para eliminar una tarea de la lista
    def eliminar_tarea(self, tarea):
        if self.lista_tareas.eliminar(tarea):  # Llama al metodo eliminar de ListaEnlazada para eliminar la tarea
            print(f"Tarea '{tarea}' eliminada.")  # Si la tarea fue eliminada, muestra un mensaje de confirmacion
        else:
            print(f"Tarea '{tarea}' no encontrada.")  # Si la tarea no se encuentra, muestra un mensaje indicando que no se encontro

