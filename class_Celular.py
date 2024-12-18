from class_App import *
from class_Tienda import *
from class_App import *
from class_Configuracion import *
from class_Contactos import *
from class_Mensajeria import *
from class_Email import*
from class_Telefono import*
from class_Calculadora import*
from validaciones import *
from class_Lista_Tareas import*


class Celular:
    ids_unicos_usados=[]
    @staticmethod
    def inicializar_ids(lista):
        for celular in lista:
            Celular.ids_unicos_usados.append(celular.id_unico)
    def __init__(self, id_unico, nombre,codigo_desbloqueo, modelo, sistema_operativo, version, memoria_ram, almacenamiento, numero_telefono):
        if not validar_numero_telefono(numero_telefono):
            raise ValueError('El numero de telefono debe tener 10 digitos')
        if not validar_codigo_telefono(codigo_desbloqueo):
            raise ValueError('El codigo debe ser de 4 digitos')
        if not validar_id_unico(id_unico, self.ids_unicos_usados):
            raise ValueError('El id_unico debe ser unico')
        self.ids_unicos_usados.append(id_unico)
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
        self.configuracion = Configuracion(self.nombre,self.codigo_desbloqueo)
        self.lista_tareas = Lista_Tareas()
        self.tienda.descargada=True 
        self.configuracion.descargada=True
        self.estado_aplicacion=False
        
    
    def __str__(self):
        return (f"Celular(ID: {self.id_unico}, Nombre: {self.nombre}, Modelo: {self.modelo}, "
                f"Sistema Operativo: {self.sistema_operativo} {self.version}, "
                f"Memoria RAM: {self.memoria_ram}GB, Almacenamiento: {self.almacenamiento}GB, "
                f"Numero de Telefono: {self.numero_telefono}, "
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

    #Desbloquea el telefono si el codigo proporcionado coincide con el codigo de desbloqueo
    def desbloquear_celular(self,codigo):
        if self.codigo_desbloqueo == codigo:
            self.bloqueado = False
            print("El telefono esta desbloqueado.")
        else:
            print("El codigo proporcionado no coincide con el codigo de desbloqueo.")
    
    
        
    
    
    # Valida que la aplicacion esta descargada.
    
    def validar_aplicacion(self, codigo):
        """Verifica si la aplicacion esta descargada."""
        return codigo in self.tienda.aplicaciones_descargadas
    

    
    
    
    
# Accede a los metodos de configuracion, verificando el estado del celular.

    def abrir_configuracion(self):
        if self.encendido and not self.bloqueado:
                if not self.estado_aplicacion:
                    self.configuracion.abrir()
                    self.estado_aplicacion = True
                    print('App Configuracion abierta.')
                else:
                    print('Ya estas usando otra app! No puedes usar Configuracion')
        else:
            print("El celular debe estar encendido y desbloqueado")
    
    def cerrar_configuracion(self):
        if self.encendido and not self.bloqueado:
                if self.estado_aplicacion:
                    self.configuracion.cerrar()
                    self.estado_aplicacion = False
                    print('App Configuracion cerrada.')
                else:
                    print('Configuracion no esta abierta! No puedes cerrar Configuracion')
        else:
            print("El celular debe estar encendido y desbloqueado")
            
    def on_off_red_movil_celular(self):
        if self.encendido and not self.bloqueado:
            if self.configuracion.estado:
                self.configuracion.on_off_red_movil()
            else: 
                print('Aplicacion cerrada.')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    
    def on_off_datos_celular(self):
        if self.encendido and not self.bloqueado:
            if self.configuracion.estado:
                self.configuracion.on_off_datos()
            else: 
                print('Aplicacion cerrada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    def nombre_dispositivo(self):
      if self.encendido and not self.bloqueado:
          if self.configuracion.estado:  
            return  self.configuracion.nombre_telefono
          else:
              print('Aplicacion cerrada.')
      else:
         print('El celular tiene que estar encendido y desbloqueado') 
  
    def codigo_actual(self):
      if self.encendido and not self.bloqueado:      
            return  self.configuracion.codigo_desbloqueo
      else:
         print('El celular tiene que estar encendido y desbloqueado')
        
    def cambiar_codigo(self,  codigo_desbloqueo):
      if self.encendido and not self.bloqueado: 
          if self.configuracion.estado:
                self.configuracion.cambiar_codigo(codigo_desbloqueo)
          else:
              print('Aplicacion cerrada.')
      else:
         print('El celular tiene que estar encendido y desbloqueado')
         
    def estado_red_movil(self):
        if self.encendido and not self.bloqueado:
                return self.configuracion.red_movil_activada

        else:
            print('El celular tiene que estar encendido y desbloqueado')
            
    def estado_datos(self):
            if self.encendido and not self.bloqueado:
                    return self.configuracion.datos_activados

            else:
                print('El celular tiene que estar encendido y desbloqueado')    
         
         
         
         
# Accede a los metodos de Tienda, verificando el estado del celular.
        
    def abrir_tienda(self):
        if self.encendido and not self.bloqueado:
                if not self.estado_aplicacion:
                    self.tienda.abrir()
                    self.estado_aplicacion = True
                    print('App Tienda abierta.')
                else:
                    print('Ya estas usando otra app! No puedes usar Tienda')
        else:
            print("El celular debe estar encendido y desbloqueado")
    
    def cerrar_tienda(self):
        if self.encendido and not self.bloqueado:
                if self.estado_aplicacion:
                    self.tienda.cerrar()
                    self.estado_aplicacion = False
                    print('App Tienda cerrada.')
                else:
                    print('Tienda no esta abierta! No puedes cerrar Tienda')
        else:
            print("El celular debe estar encendido y desbloqueado")    
        
    
    def descargar_app(self,codigo,nombre):
        if self.encendido and not self.bloqueado:
            if self.tienda.estado:
                self.tienda.descargar_aplicacion(codigo,nombre)
            else :
                print('Aplicacion cerrada')
        else:
          print('El celular tiene que estar encendido y desbloqueado')  
    
    def mostrar_apps(self):
        if self.encendido and not self.bloqueado:
            if self.tienda.estado:
                self.tienda.mostrar_aplicaciones()
            else: 
                print('Aplicacion cerrada.')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    
    def eliminar_app(self,codigo):
        if self.encendido and not self.bloqueado:
            if self.tienda.estado:
                self.tienda.eliminar_aplicacion(codigo)
            print('Aplicacion cerrada')
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
                if self.email.estado:
                    self.email.recibir_email(email_origen, mensaje, fecha)
                else:
                    print('Aplicacion cerrada')
            else:
                print('Aplicacion: Email no descargada')
        else:
           print('El celular tiene que estar encendido y desbloqueado')
           
               
    def ver_emails_por_leidos_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                if self.email.estado:
                    self.email.ver_emails_por_leidos()
                else:
                    print('Aplicacion cerrada')  
            else:
                print('Aplicacion: Email no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    
    def ver_emails_por_fecha_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(3):
                if self.email.estado:
                    self.email.ver_emails_por_fecha()
                else:
                    print('Aplicacion cerrada')
            else:
                print('Aplicacion:Email no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
        
        
        

# Accede a los metodos de contactos, verificando el estado del celular.


    def abrir_contactos(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                if not self.estado_aplicacion: 
                    self.contactos.abrir()
                    self.estado_aplicacion = True 
                    print('App Contactos abierta.')
                else:
                    print('Ya estas usando otra app! No puedes usar Contactos.')
            else: 
                print('Aplicacion: Contactos no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")
    
    def cerrar_contactos(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                if self.estado_aplicacion:  
                    self.contactos.cerrar()
                    self.estado_aplicacion = False  
                    print('App Contactos cerrada.')
                else:
                    print('Contactos no esta abierta! No puedes cerrar Contactos.')
            else: 
                print('Aplicacion: Contactos no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    
    def agregar_contacto_celular(self, nombre, numero):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                if self.contactos.estado:
                    self.contactos.agregar_contacto(nombre, numero)
                else:
                    print('Aplicacion cerrada.')
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desbloqueado')
            
    def eliminar_contacto_celular(self, nombre):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                if self.contactos.estado:
                    self.contactos.eliminar_contacto(nombre)
                else:
                    print('Aplicacion cerrada')
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desbloqueado')
    
    def actualizar_contacto_celular(self, nombre, nuevo_nombre):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                if self.contactos.estado:
                    self.contactos.actualizar_contacto(nombre, nuevo_nombre)
                else:
                    print('Aplicacion cerrada.')
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desbloqueado')
           
    def ver_contactos_celular(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(1):
                if self.contactos.estado:
                    self.contactos.ver_contactos()
                else:
                    print('Aplicacion cerrada.')
            else:
                print('Aplicacion:Contactos no descargada')
        else :
           print('El celular tiene que estar encendido y desbloqueado')
           
           
           
           
           
 # Accede a los metodos de telefono, verificando el estado de celular.    
 
    
    
    def abrir_telefono(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                if not self.estado_aplicacion:  
                    self.telefono.abrir()
                    self.estado_aplicacion = True  
                    print('App Telefono abierta.')
                else:
                    print('Ya estas usando otra app! No puedes usar Telefono.')
            else: 
                print('Aplicacion: Telefono no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    def cerrar_telefono(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                if self.estado_aplicacion:  
                    self.telefono.cerrar()
                    self.estado_aplicacion = False  
                    print('App Telefono cerrada.')
                else:
                    print('Telefono no esta abierto! No puedes cerrar Telefono.')
            else: 
                print('Aplicacion: Telefono no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")
  
           
    def hacer_llamada(self,destino,duracion,hora):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                if self.telefono.estado:                   
                    self.telefono.llamada_realizada(destino,duracion,hora)
                else:
                    print('Aplicacion no abierta')
            else:
                print('Aplicacion:Telefono no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')

    def recibir_llamada(self, emisor, duracion, hora):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                if self.telefono.estado:                   
                    self.telefono.recibir_llamada(emisor,duracion,hora)
                else:
                    print('Aplicacion no abierta')
            else:
                print('Aplicacion:Telefono no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
        
    def imprimir_registro_emisor(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                if self.telefono.estado:              
                    self.telefono.imprimir_registro_emisor()
                else:
                    print('Aplicacion no abierta')
            else: 
                print('Aplicacion:Telefono no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')

    def imprimir_registro_destinatario(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(4):
                if self.telefono.estado:              
                    self.telefono.imprimir_registro_destinatario()
                else:
                    print('Aplicacion no abierta')
            else: 
                print('Aplicacion:Telefono no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    
            
            


# Accede a los metodos de Mensajeria, verificando el estado de celular.
   
   
    
    def abrir_mensajeria(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):
                if not self.estado_aplicacion: 
                    self.mensajeria.abrir()
                    self.estado_aplicacion = True 
                    print('App Mensajeria abierta.')
                else:
                    print('Ya estas usando otra app! No puedes usar Mensajeria.')
            else: 
                print('Aplicacion: Mensajeria no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    def cerrar_mensajeria(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):
                if self.estado_aplicacion: 
                    self.mensajeria.cerrar()
                    self.estado_aplicacion = False  
                    print('App Mensajeria cerrada.')
                else:
                    print('Mensajeria no esta abierta! No puedes cerrar Mensajeria.')
            else: 
                print('Aplicacion: Mensajeria no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

            
    def enviar_sms(self, numero_destino, mensaje,fecha):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):
                if self.mensajeria.estado:              
                    self.mensajeria.enviar_sms(numero_destino, mensaje,fecha)
                else:
                    print('Aplicacion no abierta')
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')   
    


    def recibir_sms(self, numero_destino, mensaje,fecha):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):
                if self.mensajeria.estado:              
                    self.mensajeria.recibir_sms(numero_destino, mensaje,fecha)
                else:
                    print('Aplicacion no abierta')
            else: 
                print('Aplicacion: El contacto al cual quieres mandar un mensaje no descargo mensajeria')
        else:
            print('El celular tiene que estar encendido y desbloqueado')

    
    def ver_bandeja_sms(self):
        
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(2):        
                if self.mensajeria.estado:      
                    self.mensajeria.ver_bandeja_sms()
                else:
                    print('Aplicacion no abierta')
            else: 
                print('Aplicacion:Mensajeria no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')
    
     
  
          
               
# Accede a la calculadora, verificando el estado del celular.  

 
    
    def abrir_calculadora(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(8):
                if not self.estado_aplicacion: 
                    self.calculadora.abrir()
                    self.estado_aplicacion = True 
                    print('App Calculadora abierta.')
                else:
                    print('Ya estas usando otra app! No puedes usar Calculadora.')
            else: 
                print('Aplicacion: Calculadora no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    def cerrar_calculadora(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(8):
                if self.estado_aplicacion:  
                    self.calculadora.cerrar()
                    self.estado_aplicacion = False  
                    print('App Calculadora cerrada.')
                else:
                    print('Calculadora no esta abierta! No puedes cerrar Calculadora.')
            else: 
                print('Aplicacion: Calculadora no descargada.')
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
                    print("Operacion no valida.")
            else: 
                print('Aplicacion:Calculadora no descargada')
        else:
                print("El celular debe estar encendido y desbloqueado")
    
    def evaluar_expresion(self, expresion):
        """Evalúa una expresión simbólica en la calculadora."""
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(8):  # Verifica que la calculadora esté disponible
                return self.calculadora.evaluar_expresion(expresion)
            else:
                print("Aplicación: Calculadora no descargada.")
        else:
            print("El celular debe estar encendido y desbloqueado.")
    
    def _evaluar(self, expresion):
        """Método auxiliar para evaluar una expresión utilizando la lógica de la calculadora."""
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(8):  # Verifica que la calculadora esté disponible
                return self.calculadora._evaluar(expresion)
            else:
                print("Aplicación: Calculadora no descargada.")
        else:
            print("El celular debe estar encendido y desbloqueado.")


                




      
    
    
# Accede a los metodos de lista_tarea, verificando el estado de celular.
   
   
    
    def abrir_lista_tareas(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(9):
                if not self.estado_aplicacion: 
                    self.lista_tareas.abrir()
                    self.estado_aplicacion = True 
                    print('App Lista_tareas abierta.')
                else:
                    print('Ya estas usando otra app! No puedes usar Lista_tareas.')
            else: 
                print('Aplicacion: Lista_tareas no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")

    def cerrar_lista_tareas(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(9):
                if self.estado_aplicacion: 
                    self.lista_tareas.cerrar()
                    self.estado_aplicacion = False  
                    print('App Lista_tareas cerrada.')
                else:
                    print('Lista_tareas no esta abierta! No puedes cerrar Lista_tareas.')
            else: 
                print('Aplicacion: Lista_tareas no descargada.')
        else:
            print("El celular debe estar encendido y desbloqueado.")      

    def agregar_tarea(self, tarea):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(9):        
                if self.lista_tareas.estado:      
                    self.lista_tareas.agregar_tarea(tarea)
                else:
                    print('Aplicacion no abierta')
            else: 
                print('Aplicacion:lista_tareas no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')       
        


    def mostrar_tareas(self):
        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(9):        
                if self.lista_tareas.estado:      
                    self.lista_tareas.mostrar_tareas()
                else:
                    print('Aplicacion no abierta')
            else: 
                print('Aplicacion:lista_tareas no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')

    def eliminar_tarea(self, tarea):

        if self.encendido and not self.bloqueado:
            if self.validar_aplicacion(9):        
                if self.lista_tareas.estado:      
                    self.lista_tareas.eliminar_tarea(tarea)
                else:
                    print('Aplicacion no abierta')
            else: 
                print('Aplicacion:lista_tareas no descargada')
        else:
            print('El celular tiene que estar encendido y desbloqueado')    
        
        
        
        
        
          
    
    
        
    
            

            

