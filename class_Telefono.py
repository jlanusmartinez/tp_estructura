class TelefonoCelular:
    def _init_(self, id_unico, nombre, modelo, sistema_operativo, version, memoria_ram, almacenamiento, numero_telefono):
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
        self.contactos = {}
        self.sms = []
        self.llamadas = []
        self.aplicaciones = ['Contactos', 'Mensajería', 'E-mail', 'Teléfono', 'App Store', 'Configuración']

    def encender(self):
        self.encendido = True
        print("El teléfono está encendido.")
        self.activar_red_movil()

    def apagar(self):
        self.encendido = False
        print("El teléfono está apagado.")

    def bloquear(self):
        self.bloqueado = True
        print("El teléfono está bloqueado.")

    def desbloquear(self):
        self.bloqueado = False
        print("El teléfono está desbloqueado.")

    def abrir_aplicacion(self, aplicacion):
        if aplicacion in self.aplicaciones and self.encendido:
            print(f"Abriendo {aplicacion}...")
            # Lógica de interacción según la aplicación
        else:
            print("No se puede abrir la aplicación.")

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

    def agendar_contacto(self, nombre, numero):
        self.contactos[nombre] = numero
        print(f"Contacto {nombre} agregado.")

    def enviar_sms(self, numero_destino, mensaje):
        if self.encendido and not self.bloqueado:
            self.sms.append((numero_destino, mensaje))
            print(f"Mensaje enviado a {numero_destino}: {mensaje}")

    def recibir_sms(self, numero_remitente, mensaje):
        self.sms.append((numero_remitente, mensaje))
        print(f"Mensaje recibido de {numero_remitente}: {mensaje}")

    def ver_bandeja_sms(self):
        for numero, mensaje in self.sms:
            print(f"{numero}: {mensaje}")

    def eliminar_sms(self, indice):
        if 0 <= indice < len(self.sms):
            del self.sms[indice]
            print("Mensaje eliminado.")

    def ver_llamadas(self):
        for llamada in self.llamadas:
            print(llamada)

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