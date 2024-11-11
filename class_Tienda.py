from class_App import Aplicacion

# Clase Tienda que hereda de la clase Aplicacion
class Tienda(Aplicacion):

    # Constructor de la clase Tienda
    def __init__(self):
        super().__init__(6,"Tienda")  # Llama al constructor de Aplicacion con codigo 6 y nombre "Tienda"
        self.aplicaciones_descargadas={6:"Tienda",5:"Configuracion"}  # Inicializa un diccionario con aplicaciones preinstaladas
    
    # Metodo para descargar una nueva aplicacion
    def descargar_aplicacion(self, codigo, nombre):
        if codigo in self.aplicaciones_descargadas:  # Verifica si el codigo ya esta en aplicaciones_descargadas
            print(f"La aplicacion con codigo {codigo} ya esta descargada.")  # Informa que la aplicacion ya esta descargada
        else:
            self.aplicaciones_descargadas[codigo] = nombre  # Agrega la aplicacion al diccionario
            print(f"Aplicacion {nombre} descargada con el codigo {codigo}.")  # Informa que la aplicacion fue descargada

    # Metodo para mostrar las aplicaciones descargadas
    def mostrar_aplicaciones(self):
        print("Aplicaciones descargadas:")  # Muestra un titulo
        for codigo, nombre in self.aplicaciones_descargadas.items():  # Recorre el diccionario de aplicaciones descargadas
            print(f"Codigo: {codigo}, Nombre: {nombre}")  # Muestra el codigo y nombre de cada aplicacion descargada
        
    # Metodo para eliminar una aplicacion descargada
    def eliminar_aplicacion(self, codigo):
        # Verifica si el codigo corresponde a una aplicacion preinstalada (Tienda o Configuracion)
        if codigo in [6, 5]:
            print("No se puede eliminar la aplicacion preinstalada:", self.aplicaciones_descargadas[codigo])  # Muestra mensaje de error
        else:
            if codigo in self.aplicaciones_descargadas:  # Verifica si el codigo existe en aplicaciones_descargadas
                del self.aplicaciones_descargadas[codigo]  # Elimina la aplicacion del diccionario
                print(f"Aplicacion con codigo {codigo} eliminada.")  # Informa que la aplicacion fue eliminada
            else:
                print(f"No se encontro la aplicacion con codigo {codigo}.")  # Informa que la aplicacion no existe en el diccionario
