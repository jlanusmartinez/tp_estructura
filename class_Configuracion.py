from class_App import Aplicacion

class Configuracion(Aplicacion):
    def __init__(self, nombre_telefono, codigo_desbloqueo):
        super().__init__(5,'Configuracion')
        self.nombre_telefono = nombre_telefono
        self.codigo_desbloqueo = codigo_desbloqueo
        self.red_movil_activada = False
        self.datos_activados = False
        

    def on_off_red_movil(self):
        if self.red_movil_activada == False:
            self.red_movil_activada = True
            print("Red móvil activada.")
        elif self.red_movil_activada ==True:
            self.red_movil_activada = False
            print("Red móvil desactivada.")

    def on_off_datos(self):
        
        #Activa o desactiva los datos móviles del teléfono.
    
        if self.datos_activados == False:
            self.datos_activados = True
            print('Datos móviles activados')
        elif self.datos_activados == True:
            self.datos_activados = False
            print('Datos móviles desactivados')


    def cambiar_nombre(self, nombre_telefono):
            self.nombre = nombre_telefono
            print("Nombre de dispositivo configurado.")


    def cambiar_codigo(self,  codigo_desbloqueo):
            self.codigo_desbloqueo = codigo_desbloqueo
            print("Código de desbloqueo configurado.")
   