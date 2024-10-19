from class_Celular import Celular
class Central :
    
    def __init__(self):
        self.celulares = []

    def agregar_celular(self,celular):
        self.celulares.append(celular)
    
    def eliminar_celular(self,celular):
        self.celulares.remove(celular) 
        print('usuario eliminado')
    
    def estado_tel(self,celular:Celular):
        if celular.red == True:
            True
        else:
            False

    def datos_moviles(self,celular:Celular):
        if celular.datos == True:
                True
        else:
                False
    