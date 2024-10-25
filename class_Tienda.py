from class_App import Aplicacion

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
# def descargar_app(self,nombre_app):
    #     if self.estado==True:
    #         if (hasattr(self.celular,nombre_app)):
    #             app= getattr(self.celular,nombre_app)
    #             if app.descargada:
    #               print('App ya descargada')
    #             else:
    #                 app.descargada=True
    #                 print('App descargada')
    #         else:
    #             print('App no existente')
    #     else:
    #         print('App Tienda no abierta ')

    # def eliminar_app(self,nombre_app):
    #     if self.estado==True:
    #         if (hasattr(self.celular,nombre_app)):
    #             app= getattr(self.celular,nombre_app)
    #             if not(app.descargada):
    #               print('App no descargada')
    #             else:
    #                 app.descargada=False
    #                 print('App eliminda')
    #         else:
    #             print('App no existente')
    #     else:
    #         print('App Tienda no abierta ')
class Tienda(Aplicacion):

    def __init__(self):
        super().__init__(6,"Tienda")
        self.aplicaciones_descargadas={6:"Tienda",5:"Configuracion"}
    
    def descargar_aplicacion(self, codigo, nombre):
        if codigo in self.aplicaciones_descargadas:
            print(f"La aplicación con código {codigo} ya está descargada.")
        else:
            self.aplicaciones_descargadas[codigo] = nombre
            print(f"Aplicación {nombre} descargada con el código {codigo}.")

    def mostrar_aplicaciones(self):
        print("Aplicaciones descargadas:")
        for codigo, nombre in self.aplicaciones_descargadas.items():
            print(f"Código: {codigo}, Nombre: {nombre}")
        
    def eliminar_aplicacion(self, codigo):
        # Comprobar si el código es para "Tienda" o "Configuración"
        if codigo in [6, 5]:
            print("No se puede eliminar la aplicación preinstalada:", self.aplicaciones_descargadas[codigo])
        else:
            if codigo in self.aplicaciones_descargadas:
                del self.aplicaciones_descargadas[codigo]
                print(f"Aplicación con código {codigo} eliminada.")
            else:
                print(f"No se encontró la aplicación con código {codigo}.")
    
        
        
    
