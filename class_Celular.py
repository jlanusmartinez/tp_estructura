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
        self.estado_aplicacion=False
    
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

    def desbloquear_celular(self,codigo):
        if self.codigo_desbloqueo == codigo:
            self.bloqueado = False
        print("El telefono esta desbloqueado.")
    """
    Desbloquea el teléfono si el código proporcionado coincide con el código de desbloqueo.

    Args:
        codigo: El código que se debe verificar para desbloquear el teléfono.

    """
        

    #def abrir_aplicacion(self, aplicacion):
    #    if aplicacion in self.aplicaciones and self.encendido:
    #        print(f"Abriendo {aplicacion}...")
    #        # Logica de interaccion segun la aplicacion
    #    else:
    #        print("No se puede abrir la aplicacion.")
            
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
            print('El celular tiene que estar encendido y desbloqueado')
    
    def on_off_datos_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(5):
                return self.configuracion.datos_activados
            else: 
                print('Aplicacion no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    def nombre_dispositivo(self):
      if self.encendido and not self.bloqueado:  
        return  self.configuracion.nombre_telefono
      else:
         print('El celular tiene que estar encendido y desbloqueado') 
  
    def codigo_actual(self):
      if self.encendido and not self.bloqueado:  
        return  self.configuracion.codigo_desbloqueo
      else:
         print('El celular tiene que estar encendido y desbloqueado')
         
         
         
         
# Accede a los metodos de Tienda, verificando el estado del celular.
        
    def descargar_app(self,codigo,nombre):
        if self.encendido and not self.bloqueado:
            self.tienda.descargar_aplicacion(codigo,nombre)
        else:
          print('El celular tiene que estar encendido y desbloqueado')  
    
    def mostrar_apps(self):
        if self.encendido and not self.bloqueado:
            self.tienda.mostrar_aplicaciones()
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    
    def eliminar_app(self,codigo):
        if self.encendido and not self.bloqueado:
            self.tienda.eliminar_aplicacion(codigo)
        else:
            print('El celular tiene que estar encendido y desbloqueado')
            
            
            
            
            
# Accede a los metodos de email, verificando el estado del celular.

    def abrir_email(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                if not self.estado_aplicacion:
                    self.email.abrir()
                    self.estado_aplicacion = True
                    print('App Email abierta.')
                else:
                    print('Ya estas usando otra app! No puedes usar Email')
            else: 
                print('Aplicacion:Email no descargada')
        else:
            print("El celular debe estar encendido y desbloqueado")
    
    def cerrar_email(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                if self.estado_aplicacion:
                    self.email.cerrar()
                    self.estado_aplicacion = False
                    print('App Email cerrada.')
                else:
                    print('Email no esta abierta! No puedes cerrar Email')
            else: 
                print('Aplicacion:Email no descargada')
        else:
            print("El celular debe estar encendido y desbloqueado")
    
    def recibir_email_celular(self, email_origen, mensaje, fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                self.email.recibir_email(email_origen, mensaje, fecha)
            else:
                print('Aplicacion: Email no descargada')
        else:
           print('El celular tiene que estar encendido y desbloqueado')
           
               
    def ver_emails_por_leidos_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                self.email.ver_emails_por_leidos()
            else:
                print('Aplicacion: Email no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    
    def ver_emails_por_fecha_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                self.email.ver_emails_por_fecha()
            else:
                print('Aplicacion:Email no descargada')
        print('El celular tiene que estar encendido y desbloqueado')
        
        
        

# Accede a los metodos de contactos, verificando el estado del celular.

    # def abrir_contactos(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(1):
    #             self.contactos.abrir()
    #             print('App Contactos abierta.')
    #         else: 
    #             print('Aplicacion:Contactos no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")
    
    # def cerrar_contactos(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(1):
    #             self.contactos.cerrar()
    #             print('App Contactos cerrada.')
    #         else: 
    #             print('Aplicacion:Contacto no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")
    def abrir_contactos(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                if not self.estado_aplicacion:  # Validación añadida
                    self.contactos.abrir()
                    self.estado_aplicacion = True  # Asigna el estado
                    print('App Contactos abierta.')
                else:
                    print('Ya estás usando otra app! No puedes usar Contactos.')
            else: 
                print('Aplicación: Contactos no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")
    
    def cerrar_contactos(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                if self.estado_aplicacion:  # Validación añadida
                    self.contactos.cerrar()
                    self.estado_aplicacion = False  # Asigna el estado
                    print('App Contactos cerrada.')
                else:
                    print('Contactos no está abierta! No puedes cerrar Contactos.')
            else: 
                print('Aplicación: Contactos no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    
    def agregar_contacto_celular(self, nombre, numero):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                self.contactos.agregar_contacto(nombre, numero)
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desbloqueado')
            
    def eliminar_contacto_celular(self, nombre):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                self.contactos.eliminar_contacto(nombre)
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desbloqueado')
    
    def actualizar_contacto_celular(self, nombre, nuevo_nombre):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                self.contactos.actualizar_contacto(nombre, nuevo_nombre)
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desbloqueado')
           
    def ver_contactos_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                self.contactos.ver_contactos()
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desbloqueado')
           
           
           
           
           
 # Accede a los metodos de telefono, verificando el estado de celular.    
 
    # def abrir_telefono(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(4):
    #             self.telefono.abrir()
    #             print('App Telefono abierta.')
    #         else: 
    #             print('Aplicacion:Telefono no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")
    
    # def cerrar_telefono(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(4):
    #             self.telefono.cerrar()
    #             print('App Telefono cerrada.')
    #         else: 
    #             print('Aplicacion:Telefono no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")     
    
    def abrir_telefono(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                if not self.estado_aplicacion:  # Validación añadida
                    self.telefono.abrir()
                    self.estado_aplicacion = True  # Asigna el estado
                    print('App Telefono abierta.')
                else:
                    print('Ya estás usando otra app! No puedes usar Teléfono.')
            else: 
                print('Aplicación: Teléfono no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    def cerrar_telefono(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                if self.estado_aplicacion:  # Validación añadida
                    self.telefono.cerrar()
                    self.estado_aplicacion = False  # Asigna el estado
                    print('App Telefono cerrada.')
                else:
                    print('Teléfono no está abierto! No puedes cerrar Teléfono.')
            else: 
                print('Aplicación: Teléfono no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")
  
           
    def hacer_llamada(self,destino,duracion,hora):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                self.telefono.llamada_realizada(self,destino,duracion,hora)
            else:
                print('Aplicacion:Telefono no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
        
    def imprimir_registro(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):              
                self.telefono.imprimir_registro()
            else: 
                print('Aplicacion:Telefono no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
            
            


# Accede a los metodos de Mensajeria, verificando el estado de celular.
   
    # def abrir_mensajeria(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(2):
    #             self.mensajeria.abrir()
    #             print('App Mensajeria abierta.')
    #         else: 
    #             print('Aplicacion:Mensajeria no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")
    
    # def cerrar_mensajeria(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(2):
    #             self.mensajeria.cerrar()
    #             print('App Mensajeria cerrada.')
    #         else: 
    #             print('Aplicacion:Mensajeria no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")
    
    def abrir_mensajeria(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):
                if not self.estado_aplicacion:  # Validación añadida
                    self.mensajeria.abrir()
                    self.estado_aplicacion = True  # Asigna el estado
                    print('App Mensajería abierta.')
                else:
                    print('Ya estás usando otra app! No puedes usar Mensajería.')
            else: 
                print('Aplicación: Mensajería no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    def cerrar_mensajeria(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):
                if self.estado_aplicacion:  # Validación añadida
                    self.mensajeria.cerrar()
                    self.estado_aplicacion = False  # Asigna el estado
                    print('App Mensajería cerrada.')
                else:
                    print('Mensajería no está abierta! No puedes cerrar Mensajería.')
            else: 
                print('Aplicación: Mensajería no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

            
    def enviar_sms(self, numero_destino, mensaje,fecha):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):              
                self.mensajeria.enviar_sms(numero_destino, mensaje,fecha)
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')   
    


    def recibir_sms(self, numero_destino, mensaje,fecha):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):              
                self.mensajeria.recibir_sms(numero_destino, mensaje,fecha)
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')

    
    def ver_bandeja_sms(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):              
                self.mensajeria.ver_bandeja_sms()
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    
    def eliminar_sms(self, numero_destino, mensaje):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):              
                self.mensajeria.eliminar_sms(numero_destino, mensaje)
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
   
   
          
               
# Accede a la calculadora, verificando el estado del celular.  

    # def abrir_calculadora(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(8):
    #             self.calculadora.abrir()
    #             print('App Calculadora abierta.')
    #         else: 
    #             print('Aplicacion:Calculadora no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")
    
    # def cerrar_calculadora(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(8):
    #             self.calculadora.cerrar()
    #             print('App Calculadora cerrada.')
    #         else: 
    #             print('Aplicacion:Calculadora no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")
    
    def abrir_calculadora(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(8):
                if not self.estado_aplicacion:  # Validación añadida
                    self.calculadora.abrir()
                    self.estado_aplicacion = True  # Asigna el estado
                    print('App Calculadora abierta.')
                else:
                    print('Ya estás usando otra app! No puedes usar Calculadora.')
            else: 
                print('Aplicación: Calculadora no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    def cerrar_calculadora(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(8):
                if self.estado_aplicacion:  # Validación añadida
                    self.calculadora.cerrar()
                    self.estado_aplicacion = False  # Asigna el estado
                    print('App Calculadora cerrada.')
                else:
                    print('Calculadora no está abierta! No puedes cerrar Calculadora.')
            else: 
                print('Aplicación: Calculadora no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

             
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


    # def abrir_cronometro(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(7):
    #             self.cronometro.abrir()
    #             print('App Cronometro abierta.')
    #         else: 
    #             print('Aplicacion:Cronometro no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")
    
    # def cerrar_cronometro(self):
    #     if self.encendido and not self.bloqueado:
    #         if self.validar_aplicacion(7):
    #             self.cronometro.cerrar()
    #             print('App Cronometro cerrada.')
    #         else: 
    #             print('Aplicacion:Cronometro no descargada')
    #     else:
    #         print("El celular debe estar encendido y desbloqueado")
    
    def abrir_cronometro(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(7):
                if not self.estado_aplicacion:  # Validación añadida
                    self.cronometro.abrir()
                    self.estado_aplicacion = True  # Asigna el estado
                    print('App Cronómetro abierta.')
                else:
                    print('Ya estás usando otra app! No puedes usar Cronómetro.')
            else: 
                print('Aplicación: Cronómetro no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    def cerrar_cronometro(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(7):
                if self.estado_aplicacion:  # Validación añadida
                    self.cronometro.cerrar()
                    self.estado_aplicacion = False  # Asigna el estado
                    print('App Cronómetro cerrada.')
                else:
                    print('Cronómetro no está abierto! No puedes cerrar Cronómetro.')
            else: 
                print('Aplicación: Cronómetro no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    
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
    
    
        
    
    
        
        
        
        
        
          
    
    
        
    
            

            

