from class_App import Aplicacion

class Contactos(Aplicacion):
    def __init__(self):
        super().__init__(1,"Contactos")
        self.contactos={}

    def agregar_contacto(self, nombre, numero):
        self.contactos[numero] = nombre
        print(f"Contacto {nombre} agregado.")
    
    def eliminar_contacto(self, nombre):
        numero_a_eliminar=None
        for numero, contacto_nombre in self.contactos.items():
            if contacto_nombre == nombre:  
                numero_a_eliminar = numero
        if numero_a_eliminar:
            del self.contactos[numero_a_eliminar]
            print(f"Contacto {nombre} eliminado.")
        else:
            print(f"El contacto {nombre} no existe.")
            
    def actualizar_contacto(self, nombre, nuevo_nombre):
        numero_a_actualizar = None
        for numero, contacto_nombre in self.contactos.items():
            if contacto_nombre == nombre:
                numero_a_actualizar = numero
        if numero_a_actualizar:
            self.contactos[numero_a_actualizar] = nuevo_nombre
            print(f"Contacto {nombre} actualizado.")
        else:
            print(f"El contacto {nombre} no existe.")

    def ver_contactos(self):
        print(f"Contactos: {self.contactos}")
    
