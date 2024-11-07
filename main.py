#PREGUNTAR A LUCAS CUESTION DEL MAIN, COMO LO HACEMOS?
#PARA MANDAR MSJS/LLAMADAS NECESITO VERIFICAR YA LO TENGA AGENDADO
from class_App import Aplicacion
from class_Celular import Celular
from class_central import Central
from class_Configuracion import Configuracion
from class_Contactos  import Contactos
from class_Telefono import Telefono
from class_Email import Email
from class_Mensajeria import Mensajeria
from class_Tienda import Tienda 
from class_Calculadora import Calculadora
from class_Cronometro import Cronometro



if __name__ == '__main__':
    #Se crea la central
    central=Central()
    central.cargar_datos()
    #Se crean instancias de celular
    celular1=Celular(1,'pedro','1234','phone 8','IOs','version 8','10', '123' ,'1129999999')
    print(celular1)
    celular2=Celular(2,'franco','2020','phone 8','IOs','version 8','10','123' ,'1111111122')
    print(celular2)
    celular3 = Celular(3,"joaco", '3245', "Galaxy S21", "Android", "11", '8', '128', '1234567890')
    
    print(celular3)
    
    #Se agregan a la central los dispositivos
    central.agregar_celular(celular1)
    central.agregar_celular(celular2)
    central.agregar_celular(celular3)
    
    #Se encienden y desbloquean los celulares
    celular1.encender_celular()
    celular1.desbloquear_celular('1234')
    celular2.encender_celular()
    celular2.desbloquear_celular('2020')
    celular3.encender_celular()
    celular3.desbloquear_celular('3245')
    
    print('\n----------------------- \n'
          'Abro Configuracion y aplico los metodos \n'
          '----------------------- \n')
    #Utilizo metodos de configuracion    
    celular1.abrir_configuracion()
    celular2.abrir_configuracion()
    celular3.abrir_configuracion()
    
    celular1.on_off_red_movil_celular()
    celular2.on_off_red_movil_celular()
    celular3.on_off_red_movil_celular()
    
    celular1.cerrar_configuracion()
    celular2.cerrar_configuracion()
    celular3.cerrar_configuracion()
    
    print('\n----------------------- \n'
    'Abro Tienda y aplico los metodos \n'
    '----------------------- \n')
    #Utilizo metodos de Tienda
    celular1.abrir_tienda()
    celular2.abrir_tienda()
    celular3.abrir_tienda()
    
    print('\n' 
          '-Descargo las apps \n')    
    celular1.descargar_app(1, 'Contactos')
    celular2.descargar_app(1, 'Contactos')
    celular3.descargar_app(1, 'Contactos')
    celular1.descargar_app(3, 'Email')
    celular2.descargar_app(3, 'Email')    
    celular3.descargar_app(3, 'Email')
    celular1.descargar_app(2, 'Mensajeria')
    celular2.descargar_app(2, 'Mensajeria')
    celular3.descargar_app(2, 'Mensajeria')
    celular1.descargar_app(4, 'Telefono')
    celular2.descargar_app(4, 'Telefono')
    celular3.descargar_app(4, 'Telefono')
    celular1.descargar_app(8, 'Calculadora')
    celular2.descargar_app(8, 'Calculadora')
    celular3.descargar_app(8, 'Calculadora')
    celular1.descargar_app(7, 'Cronometro')
    celular2.descargar_app(7, 'Cronometro')
    celular3.descargar_app(7, 'Cronometro')
    print('\n' 
          '-Descargo las apps \n') 
    
    celular1.mostrar_apps()
    celular2.mostrar_apps()
    celular3.mostrar_apps()
    
    celular1.cerrar_tienda()
    celular2.cerrar_tienda()
    celular3.cerrar_tienda()
    
    print('\n----------------------- \n'
    'Abro Contactos y aplico los metodos \n'
    '----------------------- \n')
    
    #Utilizo metodos de Contactos
    celular1.abrir_contactos()
    celular2.abrir_contactos()
    celular3.abrir_contactos()
    print('\n' 
          '-Agrego contactos \n')
    
    celular1.agregar_contacto_celular('Franco', '1111111122')
    celular1.agregar_contacto_celular('Joaco', '1234567890')
    celular2.agregar_contacto_celular('Pedro', '1129999999')
    celular2.agregar_contacto_celular('Joaco', '1234567890')
    celular3.agregar_contacto_celular('Pedro', '1129999999')
    celular3.agregar_contacto_celular('Franco', '1111111122')
    
    print('\n' 
          '-Actualizo algun contacto, elimino alguno. \n')
    
    celular1.actualizar_contacto_celular('Joaco', 'Joaquin')
    celular2.actualizar_contacto_celular('Pedro', 'Pedrito')
    celular3.eliminar_contacto_celular('Franco')
    
    print('\n'
          'Muestro los contactos de cada uno actualizados \n')
    
    celular1.ver_contactos_celular()
    celular2.ver_contactos_celular()
    celular3.ver_contactos_celular()
    
    celular1.cerrar_contactos()
    celular2.cerrar_contactos()
    celular3.cerrar_contactos()
    
    print('\n----------------------- \n'
    'Abro Email y aplico los metodos \n'
    '----------------------- \n')
    
    #Utilizo metodos de Email
    celular1.abrir_email()

    
    print('\n'
          'Recibo correos \n')
    
    celular1.recibir_email_celular('Manuel', 'Esto es un correo de Manuel', '05/11/2024')
    celular1.recibir_email_celular('Javier', 'Esto es un correo de Javier respondiendo tu duda...')
    celular1.recibir_email_celular('Pablo', 'Esto es un correo de pablo hablando sobre...')
    celular1.recibir_email_celular('Marcela', 'Como va todo?', '03/11/2024')
    
    print('\n'
          'Veo correos no leidos \n')
    
    celular1.ver_emails_por_leidos_celular()
    
    print('\n'
          'Veo correos por fecha \n')
    
    celular1.ver_emails_por_fecha_celular()
    
    celular1.cerrar_email()
    
    
    
    #utilizo metodos de mensajeria
    print('\n----------------------- \n'
    'Abro Mensajeria y aplico los metodos \n'
    '----------------------- \n')
    
    celular1.abrir_mensajeria()
    celular2.abrir_mensajeria()
    celular3.abrir_mensajeria()
    
    print('\n'
          'Realizo mensajes a un contacto. \n')
    
    central.enviar_sms('1129999999', '1234567890', 'Como va todo...')
    central.enviar_sms('1111111122', '1129999999', 'Como te fue el otro dia?')
    central.enviar_sms('1234567890', '1111111122', 'Me fui a comer')
    central.enviar_sms('1234567890', '1111111122', 'Donde estas?')
    
    print('\n'
          'Elimino mensajes. \n')
    
    central.eliminar_sms('1234567890', '1111111122', 'Donde estas?')
    
    print('\n'
          'Muestro la bandeja de mensajes. \n')
    
    celular1.ver_bandeja_sms()
    celular2.ver_bandeja_sms()
    celular3.ver_bandeja_sms()
    
    celular1.cerrar_mensajeria()
    celular2.cerrar_mensajeria()
    celular3.cerrar_mensajeria()
    
    
    
    
    #Utilizo metodos de Telefono
    
    print('\n----------------------- \n'
    'Abro Telefono y aplico los metodos \n'
    '----------------------- \n')
    
    celular1.abrir_telefono()
    celular2.abrir_telefono()
    
    
    print('\n'
          'realizo llamadas a un contacto, estableciendo una duracion. \n')
    
    central.llamada('1129999999', '1111111122', 5)
    
    print('\n'
          'Muestro el registro de llamadas. \n')
    
    celular1.imprimir_registro()
    celular2.imprimir_registro()
    
    celular1.cerrar_telefono()
    celular2.cerrar_telefono()
   
      
    
    

    
    #Utilizo metodos de calculadora
    
    print('\n----------------------- \n'
    'Abro Calculadora y aplico los metodos \n'
    '----------------------- \n')
    
    celular1.abrir_calculadora()
    
    print('\n'
          'Realizo operaciones basicas. \n')
    
    celular1.usar_calculadora('sumar', 3, 5)
    celular1.usar_calculadora('multiplicar', 3, 5)
    
    celular1.cerrar_calculadora()
    
    
    #Utilizo metodos de Cronometro
    
    print('\n----------------------- \n'
    'Abro Cronometro y aplico los metodos \n'
    '----------------------- \n')
    
    celular1.abrir_cronometro()
    
    celular1.usar_cronometro('iniciar')
    
    celular1.cerrar_cronometro()
    
    central.guardar_datos()
    
    

    
    
    
    
    
    
    



          
    
    
