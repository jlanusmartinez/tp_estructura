from class_App import Aplicacion
from class_Celular import Celular
from class_App import *
from class_central import *
from class_Tienda import *
from class_App import *
from class_central import *
from class_Configuracion import *
from class_Contactos import *
from class_Mensajeria import *
from class_Email import*
from class_Telefono import*

"""""
class Tienda(Aplicacion):
    apps=["Mensajeria","Contactos","Email","Configuracion","Telefono"]
    def __innit__(self):
        super().__init__(6,'Tienda')
    def descargar(self, app):
        if app == "Mensajeria":
            return Mensajeria()
        if app == 'Contactos':
            return Contactos()
        if app == 'Email':
            return Email()
        if app == 'Configuracion':
            return Configuracion()
        if app == 'Telefono':
            return Telefono()

class Grafico(Aplicacion):
    def __innit__(self, ID,nombre):
        super().__init__(ID,nombre)
        

#CLASE PARA DESPUES

"""""

class Tienda:

    def __init__(self,celular):
        super().__init__("Tienda")
        self.celular = celular
        
    def descargar_app(self,nombre_app):
        pass