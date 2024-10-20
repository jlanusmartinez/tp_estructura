from class_Celular import Celular

class Aplicacion:
    def __init__(self,Id,nombre):
        self.nombre = nombre
        self.estado=False
        self.descargada= False 
        

    def abrir(self):
        if self.descargada==True:
            self.estado = True
            print(f"Abriendo {self.nombre}.")
        else:
            print('Aplicacion no descargada')

    def cerrar(self):
        if self.estado:
            self.estado = False
            print(f"Cerrando {self.nombre}.")
        else:
            print(f'La app no esta abierta')

        
        

    
