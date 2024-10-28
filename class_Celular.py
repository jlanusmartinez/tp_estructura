from class_App import *
from class_Tienda import *
from class_App import *
from class_Configuracion import *
from class_Contactos import *
from class_Mensajeria import *
from class_Email import*
from class_Telefono import*
from class_Calculadora import*
from class_Cronometro import*

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
        self.calculadora=Calculadora()
        self.cronometro=Cronometro()
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
    
    
    # Valida que la aplicacion esta descargada.
    
    def validar_aplicacion(self, codigo):
        """Verifica si la aplicación está descargada."""
        return codigo in self.tienda.aplicaciones_descargadas
    
    
    
    
    
    
# Accede a los metodos de configuracion, verificando el estado del celular.

    def on_off_red_movil_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(5):
                return self.configuracion.red_movil_activada
            else: 
                print('Aplicacion no descargada')
        else:
            print('El celular tiene que estar encendido y desploqueado')
    
    def on_off_datos_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(5):
                return self.configuracion.datos_activados
            else: 
                print('Aplicacion no descargada')
        else:
            print('El celular tiene que estar encendido y desploqueado')
    def nombre_dispositivo(self):
      if self.encendido and not self.bloqueado:  
        return  self.configuracion.nombre_telefono
      else:
         print('El celular tiene que estar encendido y desploqueado') 
  
    def codigo_actual(self):
      if self.encendido and not self.bloqueado:  
        return  self.configuracion.codigo_desbloqueo
      else:
         print('El celular tiene que estar encendido y desploqueado')
         
         
         
         
# Accede a los metodos de Tienda, verificando el estado del celular.
        
    def descargar_app(self,codigo,nombre):
        if self.encendido and not self.bloqueado:
            self.tienda.descargar_aplicacion(codigo,nombre)
        else:
          print('El celular tiene que estar encendido y desploqueado')  
    
    def mostrar_apps(self):
        if self.encendido and not self.bloqueado:
            self.tienda.mostrar_aplicaciones()
        else:
            print('El celular tiene que estar encendido y desploqueado')
    
    def eliminar_app(self,codigo):
        if self.encendido and not self.bloqueado:
            self.tienda.eliminar_aplicacion(codigo)
        else:
            print('El celular tiene que estar encendido y desploqueado')
            
            
            
            
            
# Accede a los metodos de email, verificando el estado del celular.
    
    def recibir_email_celular(self, email_origen, mensaje, fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                self.email.recibir_email(email_origen, mensaje, fecha)
            else:
                print('Aplicacion: Email no descargada')
        else:
           print('El celular tiene que estar encendido y desploqueado')
           
               
    def ver_emails_por_leidos_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                self.email.ver_emails_por_leidos()
            else:
                print('Aplicacion: Email no descargada')
        else:
            print('El celular tiene que estar encendido y desploqueado')
    
    def ver_emails_por_fecha_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                self.email.ver_emails_por_fecha()
            else:
                print('Aplicacion:Email no descargada')
        print('El celular tiene que estar encendido y desploqueado')
        
        
        

# Accede a los metodos de contactos, verificando el estado del celular.
    
    def agregar_contacto_celular(self, nombre, numero):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                self.contactos.agregar_contacto(nombre, numero)
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desploqueado')
            
    def eliminar_contacto_celular(self, nombre):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                self.contactos.eliminar_contacto(nombre)
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desploqueado')
    
    def actualizar_contacto_celular(self, nombre, nuevo_nombre):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                self.contactos.actualizar_contacto(nombre, nuevo_nombre)
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desploqueado')
           
    def ver_contactos_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                self.contactos.ver_contactos()
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desploqueado')
           
           
           
           
           
 # Accede a los metodos de telefono, verificando el estado de celular.           
           
    def hacer_llamada(self,destino,duracion,hora):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                self.telefono.llamada_realizada(self,destino,duracion,hora)
            else:
                print('Aplicacion:Telefono no descargada')
        else:
            print('El celular tiene que estar encendido y desploqueado')
        
    def imprimir_registro(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):              
                self.telefono.imprimir_registro()
            else: 
                print('Aplicacion:Telefono no descargada')
        else:
            print('El celular tiene que estar encendido y desploqueado')
            
            


# Accede a los metodos de Mensajeria, verificando el estado de celular.
   
    def enviar_sms(self, numero_destino, mensaje,fecha):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):              
                self.mensajeria.enviar_sms(numero_destino, mensaje,fecha)
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desploqueado')   
    


    def recibir_sms(self, numero_destino, mensaje,fecha):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):              
                self.mensajeria.recibir_sms(numero_destino, mensaje,fecha)
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desploqueado')

    
    def ver_bandeja_sms(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):              
                self.mensajeria.ver_bandeja_sms()
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desploqueado')
   
   
          
               
# Accede a la calculadora, verificando el estado del celular.       
    def usar_calculadora(self, operacion, a, b):
        """Accede a la calculadora, verificando el estado del celular."""
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(8):
                if operacion == "sumar":
                    return self.calculadora.sumar(a, b)
                elif operacion == "restar":
                    return self.calculadora.restar(a, b)
                elif operacion == "multiplicar":
                    return self.calculadora.multiplicar(a, b)
                elif operacion == "dividir":
                    return self.calculadora.dividir(a, b)
                else:
                    print("Operación no válida.")
            else: 
                print('Aplicacion:Calculadora no descargada')
        else:
                print("El celular debe estar encendido y desbloqueado")





# Accede al cronómetro, verificando el estado del celular.
    def usar_cronometro(self, accion):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(7):
                if accion == "iniciar":
                    self.cronometro.iniciar()
                elif accion == "detener":
                    self.cronometro.detener()
                else:
                    print("Acción no válida. Usa 'iniciar' o 'detener'.")
            else: 
                print('Aplicacion:Cronometro no descargada')
        else:
                print("El celular debe estar encendido y desbloqueado")           
    
    
        
    
    
        
        
        
        
        
          
    
    
        
    
            

            

