from class_App import *
from class_Central import *
from class_Tienda import *
from class_App import *
from class_Configuracion import *
from class_Contactos import *
from class_Mensajeria import *
from class_Email import*
from class_Telefono import*

class Celular:
    def _init_(self, id_unico, nombre,codigo_desbloqueo, modelo, sistema_operativo, version, memoria_ram, almacenamiento, numero_telefono):
        self.id_unico = id_unico
        self.nombre = nombre
        self.codigo_desbloqueo=codigo_desbloqueo
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.version = version
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento
        self.numero_telefono = numero_telefono
        self.encendido = False
        self.bloqueado = True
        self.tienda = Tienda(self)
        self.telefono= Telefono(self.numero_telefono)
        self.contactos=Contactos()
        self.mensajeria=Mensajeria(self.numero_telefono)
        self.email=Email()
        self.configuracion = Configuracion(self.nombre,self.codigo_desbloqueo)
        self.tienda.descargada=True 

    def encender_celular(self):
        self.encendido = True
        self.red= True
        print("El telefono esta encendido.")
        self.activar_red_movil()

    def apagar_celular(self):
        self.encendido = False
        self.red = False
        print("El telefono esta apagado.")

    def bloquear_celular(self):
        self.bloqueado = True
        print("El telefono esta bloqueado.")

    def desbloquear_celular(self):
        self.bloqueado = False
        print("El telefono esta desbloqueado.")

    def abrir_aplicacion(self, aplicacion):
        if aplicacion in self.aplicaciones and self.encendido:
            print(f"Abriendo {aplicacion}...")
            # Logica de interaccion segun la aplicacion
        else:
            print("No se puede abrir la aplicacion.")
            
    # def instalar_app(self,app:Aplicacion):
    #     if app not in Tienda.apps and app not in self.aplicaciones_descargadas:
    #         print(f'App inexistente: {app}')
    #     else:
    #         self.aplicaciones_descargadas.append(app)
    #         print('Aplicacion descargada correctamemte')
    
    # def desinstalar_app(self,app:Aplicacion):
    #     if app in self.aplicaciones_descargadas:
    #         self.aplicaciones_descargadas.remove(app)
    #         print('Aplicacion desinstalada correctamente')
    #     else:
    #         print(f'App inexistente: {app}') 
    
    def validar_aplicacion(self, codigo):
        """Verifica si la aplicación está descargada."""
        return codigo in self.aplicaciones_descargadas
    
    def on_off_red_movil_celular(self):
        if self.validar_aplicacion(5):
            return self.configuracion.red_movil_activada
        else: 
            print('Aplicacion no descargada')
    
    def on_off_datos_celular(self):
        if self.validar_aplicacion(5):
            return self.configuracion.datos_activados
        else: 
            print('Aplicacion no descargada')
        
    def nombre_dispositivo(self):
        return  self.configuracion.nombre_telefono
  
    def codigo_actual(self):
            return self.configuracion.codigo_desbloqueo
        
    def descargar_app(self,codigo,nombre):
        self.descargar_aplicacion(codigo,nombre)
    
    def mostrar_apps(self):
        self.mostrar_aplicaciones()
    
    def eliminar_app(self,codigo):
        self.eliminar_aplicacion(codigo)
        
        
        
        
          
    
    
        
    
            

            

