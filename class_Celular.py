from class_App import *
from class_Tienda import *
from class_App import *
from class_Configuracion import *
from class_Contactos import *
from class_Mensajeria import *
from class_Email import*
from class_Telefono import*

class Celular:
    def __init__(self, id_unico, nombre,codigo_desbloqueo, modelo, sistema_operativo, version, memoria_ram, almacenamiento, numero_telefono):
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
        self.tienda = Tienda()
        self.telefono= Telefono(self.numero_telefono)
        self.contactos=Contactos()
        self.mensajeria=Mensajeria(self.numero_telefono)
        self.email=Email()
        self.configuracion = Configuracion(self.nombre,self.codigo_desbloqueo)
        self.tienda.descargada=True 
    
    def __str__(self):
        return (f"Celular(ID: {self.id_unico}, Nombre: {self.nombre}, Modelo: {self.modelo}, "
                f"Sistema Operativo: {self.sistema_operativo} {self.version}, "
                f"Memoria RAM: {self.memoria_ram}GB, Almacenamiento: {self.almacenamiento}GB, "
                f"Número de Teléfono: {self.numero_telefono}, "
                f"Encendido: {self.encendido}, Bloqueado: {self.bloqueado})")

    def encender_celular(self):
        self.encendido = True
        self.red= True
        print("El telefono esta encendido.")
        self.configuracion.red_movil_activada= True
        self.configuracion.datos_activados=True

    def apagar_celular(self):
        self.encendido = False
        self.red = False
        self.configuracion.red_movil_activada = False
        self.configuracion.datos_activados=False
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
        return codigo in self.tienda.aplicaciones_descargadas
    
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
        self.tienda.descargar_aplicacion(codigo,nombre)
    
    def mostrar_apps(self):
        self.tienda.mostrar_aplicaciones()
    
    def eliminar_app(self,codigo):
        self.tienda.eliminar_aplicacion(codigo)
    
    def recibir_email_celular(self, email_origen, mensaje, fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        if self.validar_aplicacion(3):
            self.email.recibir_email(email_origen, mensaje, fecha)
        else:
            print('Aplicacion no descargada')
        
        
        
        
          
    
    
        
    
            

            

