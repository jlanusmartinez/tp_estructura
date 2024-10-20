from class_App import Aplicacion
from class_Celular import Celular

class Configuracion(Aplicacion):
    def __init__(self, nombre_telefono, codigo_desbloqueo):
        super().__init__(5,'Configuracion')
        self.nombre_telefono = nombre_telefono
        self.codigo_desbloqueo = codigo_desbloqueo
        self.red_movil_activada = False
        self.datos_activados = False

    def on_off_red_movil(self,celular:Celular):
        if celular.red == False:
            celular.red = True
            print("Red móvil activada.")
        elif celular.red ==True:
            celular.red = False
            print("Red móvil desactivada.")

    def on_off_datos(self,celular:Celular):
        
        #Activa o desactiva los datos móviles del teléfono.
    
        if celular.datos == False:
            celular.datos = True
            print('Datos móviles activados')
        elif celular.datos == True:
            celular.datos = False
            print('Datos móviles desactivados')




    def activar_datos(self):
        self.datos_activados = True
        print("Datos activados.")

    def desactivar_datos(self):
        self.datos_activados = False
        print("Datos desactivados.")
        
    #METODOS CONFIGURACION CHATGPT
    def configurar(self, nombre_telefono=None, codigo_desbloqueo=None):
        if nombre_telefono:
            self.nombre = nombre_telefono
        if codigo_desbloqueo:
            print("Código de desbloqueo configurado.")

    def activar_red_movil(self):
        if self.encendido:
            print("Red móvil activada.")

    def desactivar_red_movil(self):
        if self.encendido:
            print("Red móvil desactivada.")

    def activar_datos(self):
        if self.encendido:
            print("Datos activados.")

    def desactivar_datos(self):
        if self.encendido:
            print("Datos desactivados.")