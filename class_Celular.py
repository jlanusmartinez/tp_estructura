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
    def _init_(self, id_unico, nombre, modelo, sistema_operativo, version, memoria_ram, almacenamiento, numero_telefono,central):
        self.id_unico = id_unico
        self.nombre = nombre
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.version = version
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento
        self.numero_telefono = numero_telefono
        self.encendido = False
        self.bloqueado = True
        self.red=False
        self.datos=False
        self.aplicaciones_descargadas= []
        self.central=central
        self.tienda = Tienda(self)
        self.telefono= Telefono(self.central,self)
        self.contactos=Contactos()
        self.mensajeria=Mensajeria(self.central,self)
        self.email=Email()
        self.configuracion = Configuracion()
        self.tienda.descargada=True 

    def encender(self):
        self.encendido = True
        self.red= True
        print("El telefono esta encendido.")
        self.activar_red_movil()

    def apagar(self):
        self.encendido = False
        self.red = False
        print("El telefono esta apagado.")

    def bloquear(self):
        self.bloqueado = True
        print("El telefono esta bloqueado.")

    def desbloquear(self):
        self.bloqueado = False
        print("El telefono esta desbloqueado.")

    def abrir_aplicacion(self, aplicacion):
        if aplicacion in self.aplicaciones and self.encendido:
            print(f"Abriendo {aplicacion}...")
            # Logica de interaccion segun la aplicacion
        else:
            print("No se puede abrir la aplicacion.")
            
    def instalar_app(self,app:Aplicacion):
        if app not in Tienda.apps and app not in self.aplicaciones_descargadas:
            print(f'App inexistente: {app}')
        else:
            self.aplicaciones_descargadas.append(app)
            print('Aplicacion descargada correctamemte')
    
    def desinstalar_app(self,app:Aplicacion):
        if app in self.aplicaciones_descargadas:
            self.aplicaciones_descargadas.remove(app)
            print('Aplicacion desinstalada correctamente')
        else:
            print(f'App inexistente: {app}') 
    
    
        
    
            

            

