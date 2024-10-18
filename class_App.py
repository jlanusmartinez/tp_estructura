
class Aplicacion:
    def __init__(self, ID,nombre):
        self.ID=ID 
        self.nombre = nombre
        self.estado=False

    def abrir(self):
        self.estado = True
        print(f"Abriendo {self.nombre}.")

    def cerrar(self):
        if self.estado:
            self.estado = False
            print(f"Cerrando {self.nombre}.")
        else:
            print(f'La app no esta abierta')


class Contactos(Aplicacion):
    def __init__(self):
        super().__init__(1,"Contactos")
        self.contactos={}

    def agregar_contacto(self, nombre, numero):
        self.contactos[nombre] = numero
        print(f"Contacto {nombre} agregado.")
    
    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado.")
        else:
            print(f"El contacto {nombre} no existe.")
            
    def actualizar_contacto(self, nombre, numero):
        if nombre in self.contactos:
            self.contactos[nombre] = numero
            print(f"Contacto {nombre} actualizado.")
        else:
            print(f"El contacto {nombre} no existe.")

    def ver_contactos(self):
        print(f"Contactos: {self.contactos}")
    
    #METODOS CONTACTOS CHATGPT
    def agendar_contacto(self, nombre, numero):
        self.contactos[nombre] = numero
        print(f"Contacto {nombre} agregado.")
        
class Mensajeria(Aplicacion):
    def __init__(self):
        super().__init__(2,'Mensajeria')
        self.sms = []

    def enviar_sms(self, numero_destino, mensaje):
        self.sms.append((numero_destino, mensaje))
        print(f"SMS enviado a {numero_destino}: {mensaje}")

    def ver_sms(self):
        for numero, mensaje in self.sms:
            print(f"{numero}: {mensaje}")
    



class Email(Aplicacion):
    def __init__(self):
        super().__init__(3,'Email')
        self.emails = []

    def enviar_email(self, email_destino, mensaje):
        self.emails.append((email_destino, mensaje))
        print(f"Email enviado a {email_destino}: {mensaje}")

    def ver_emails(self):
        for email, mensaje in self.emails:
            print(f"{email}: {mensaje}")    
            
            
class Telefono(Aplicacion):
    def __init__(self):
        super().__init__(4,'Telefono')
        self.ultima_llamada = 0
        self.ultima_mensajeria = 0
        self.ultima_email = 0
        

    def hacer_llamada(self, hora):  
        if hora > self.ultima_llamada:  
            self.ultima_llamada = hora  
            print(f"Haciendo llamada a {self.nombre} a las {hora}") 
    
    #USAR CONJUNTOS PARA TELEFONO
    #METODOS CHATGPT DE TELEFONO 
    def realizar_llamada(self, numero_destino):
        if self.encendido and not self.bloqueado:
            print(f"Llamando a {numero_destino}...")
            self.llamadas.append(numero_destino)
        else:
            print("El teléfono está apagado o bloqueado.")

    def recibir_llamada(self, numero_remitente):
        if self.encendido:
            print(f"Recibiendo llamada de {numero_remitente}...")
            self.llamadas.append(numero_remitente)
        else:
            print("El teléfono está apagado.")

    def terminar_llamada(self):
        print("Llamada terminada.")

class Configuracion(Aplicacion):
    def __init__(self, nombre_telefono, codigo_desbloqueo):
        super().__init__(5,'Configuracion')
        self.nombre_telefono = nombre_telefono
        self.codigo_desbloqueo = codigo_desbloqueo
        self.red_movil_activada = False
        self.datos_activados = False

    def activar_red_movil(self):
        self.red_movil_activada = True
        print("Red móvil activada.")

    def desactivar_red_movil(self):
        self.red_movil_activada = False
        print("Red móvil desactivada.")

    def activar_datos(self):
        self.datos_activados = True
        print("Datos activados.")

    def desactivar_datos(self):
        self.datos_activados = False
        print("Datos desactivados.")

        
        
        
class Tienda(Aplicacion):
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

class Grafico(Aplicacion):
    def __innit__(self, ID,nombre):
        super().__init__(ID,nombre)
        

#CLASE PARA DESPUES
        
        

    
