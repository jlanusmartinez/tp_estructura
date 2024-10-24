from class_App import Aplicacion
from class_App import *
from class_Celular import * 

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

class Tienda(Aplicacion):

    def __init__(self,celular:Celular):
        super().__init__(6,"Tienda")
        self.celular = celular
        
    def descargar_app(self,nombre_app):
        if self.estado==True:
            if (hasattr(self.celular,nombre_app)):
                app= getattr(self.celular,nombre_app)
                if app.descargada:
                  print('App ya descargada')
                else:
                    app.descargada=True
                    print('App descargada')
            else:
                print('App no existente')
        else:
            print('App Tienda no abierta ')

    def eliminar_app(self,nombre_app):
        if self.estado==True:
            if (hasattr(self.celular,nombre_app)):
                app= getattr(self.celular,nombre_app)
                if not(app.descargada):
                  print('App no descargada')
                else:
                    app.descargada=False
                    print('App eliminda')
            else:
                print('App no existente')
        else:
            print('App Tienda no abierta ')
