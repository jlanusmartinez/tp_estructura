from class_App import Aplicacion  

# Clase Contactos que hereda de la clase Aplicacion
class Contactos(Aplicacion):
    
    # Constructor de la clase Contactos
    def __init__(self):
        super().__init__(1, "Contactos")  # Llama al constructor de Aplicacion con codigo 1 y nombre "Contactos"
        self.contactos = {}  # Inicializa un diccionario vacio para almacenar los contactos

    # Metodo para agregar un nuevo contacto
    def agregar_contacto(self, nombre, numero):
        self.contactos[numero] = nombre  # Agrega el contacto al diccionario usando el numero como clave
        print(f"Contacto {nombre} agregado.")  # Muestra un mensaje de confirmacion

    # Metodo para eliminar un contacto por nombre
    def eliminar_contacto(self, nombre):
        numero_a_eliminar = None  # Inicializa una variable para almacenar el numero a eliminar
        for numero, contacto_nombre in self.contactos.items():  # Recorre el diccionario de contactos
            if contacto_nombre == nombre:  # Verifica si el nombre coincide con el contacto buscado
                numero_a_eliminar = numero  # Almacena el numero del contacto a eliminar
        if numero_a_eliminar:  # Si se encontro el numero
            del self.contactos[numero_a_eliminar]  # Elimina el contacto del diccionario
            print(f"Contacto {nombre} eliminado.")  # Muestra un mensaje de confirmacion
        else:
            print(f"El contacto {nombre} no existe.")  # Muestra un mensaje si el contacto no existe

    # Metodo para actualizar el nombre de un contacto
    def actualizar_contacto(self, nombre, nuevo_nombre):
        numero_a_actualizar = None  # Inicializa una variable para almacenar el numero a actualizar
        for numero, contacto_nombre in self.contactos.items():  # Recorre el diccionario de contactos
            if contacto_nombre == nombre:  # Verifica si el nombre coincide con el contacto buscado
                numero_a_actualizar = numero  # Almacena el numero del contacto a actualizar
        if numero_a_actualizar:  # Si se encontro el numero
            self.contactos[numero_a_actualizar] = nuevo_nombre  # Actualiza el nombre del contacto
            print(f"Contacto {nombre} actualizado.")  # Muestra un mensaje de confirmacion
        else:
            print(f"El contacto {nombre} no existe.")  # Muestra un mensaje si el contacto no existe

    # Metodo para ver todos los contactos
    def ver_contactos(self):
        print(f"Contactos: {self.contactos}")  # Muestra el diccionario completo de contactos
