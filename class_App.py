
class Aplicacion:
    def __init__(self,Id,nombre):
        self.Id = Id
        self.nombre = nombre
        self.estado=False
        self.descargada= False 
        
    # Abrir aplicacion
    def abrir(self):
            self.estado = True
            print(f"Abriendo {self.nombre}.")

     # Cerrar aplicacion 
    def cerrar(self):
        if self.estado:
            self.estado = False
            print(f"Cerrando {self.nombre}.")
        else:
            print(f'La app no esta abierta')

        
        

    
