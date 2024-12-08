from class_Celular import Celular
from class_central import Central
import datetime

# Funcionalidades de la aplicación

def funcionalidades_configuracion():
    celular1.abrir_configuracion()
    celular2.abrir_configuracion()
    celular3.abrir_configuracion()

    celular1.on_off_red_movil_celular()
    celular2.on_off_red_movil_celular()
    celular3.on_off_red_movil_celular()

    celular1.on_off_datos_celular()
    celular2.on_off_datos_celular()
    celular3.on_off_datos_celular()

    celular1.cerrar_configuracion()
    celular2.cerrar_configuracion()
    celular3.cerrar_configuracion()

def funcionalidades_tienda():
    celular1.abrir_tienda()
    celular2.abrir_tienda()
    celular3.abrir_tienda()

    celular1.mostrar_apps()
    celular2.mostrar_apps()
    celular3.mostrar_apps()

    celular1.cerrar_tienda()
    celular2.cerrar_tienda()
    celular3.cerrar_tienda()

def funcionalidades_contactos():
    celular1.abrir_contactos()
    celular2.abrir_contactos()
    celular3.abrir_contactos()
    print('\n-Agrego contactos \n')

    celular1.agregar_contacto_celular('Franco', '1111111122')
    celular1.agregar_contacto_celular('Joaco', '1134567890')
    celular2.agregar_contacto_celular('Pedro', '1129999999')
    celular2.agregar_contacto_celular('Joaco', '1134567890')
    celular3.agregar_contacto_celular('Pedro', '1129999999')
    celular3.agregar_contacto_celular('Franco', '1111111122')

    print('\n-Actualizo algun contacto, elimino alguno. \n')

    celular1.actualizar_contacto_celular('Joaco', 'Joaquin')
    celular2.actualizar_contacto_celular('Pedro', 'Pedrito')
    celular3.eliminar_contacto_celular('Franco')

    print('\nMuestro los contactos de cada uno actualizados \n')

    celular1.ver_contactos_celular()
    celular2.ver_contactos_celular()
    celular3.ver_contactos_celular()

    celular1.cerrar_contactos()
    celular2.cerrar_contactos()
    celular3.cerrar_contactos()

def funcionalidades_email():
    celular1.abrir_email()
    print('\nRecibo correos \n')

    celular1.recibir_email_celular('Manuel', 'Esto es un correo de Manuel', datetime.datetime.strptime('22/10/2024 10:00:00', '%d/%m/%Y %H:%M:%S'))
    celular1.recibir_email_celular('Javier', 'Esto es un correo de Javier respondiendo tu duda...',datetime.datetime.strptime('22/10/2019 10:00:00', '%d/%m/%Y %H:%M:%S'))
    celular1.recibir_email_celular('Pablo', 'Esto es un correo de pablo hablando sobre...',datetime.datetime.strptime('22/10/2014 10:00:00', '%d/%m/%Y %H:%M:%S'))
    celular1.recibir_email_celular('Marcela', 'Como va todo?', datetime.datetime.strptime('22/09/2009 10:00:00', '%d/%m/%Y %H:%M:%S'))
    
    print('\nVeo correos no leidos \n')
    celular1.ver_emails_por_leidos_celular()

    print('\nAhora veo correos leidos, porque ya cuentan como leidos. \n')
    celular1.ver_emails_por_leidos_celular()

    print('\nVeo correos por fecha \n')
    celular1.ver_emails_por_fecha_celular()

    celular1.cerrar_email()

def funcionalidades_msj():
    celular1.abrir_mensajeria()
    celular2.abrir_mensajeria()
    celular3.abrir_mensajeria()

    print('\nEnvio mensajes a un contacto. \n')
    central.enviar_sms('1129999999', '1134567890', 'Como va todo...')
    central.enviar_sms('1111111122', '1129999999', 'Como te fue el otro dia?')
    central.enviar_sms('1134567890', '1111111122', 'Me fui a comer')
    central.enviar_sms('1134567890', '1111111122', 'Donde estas?')

    print('\nElimino mensajes. \n')
    central.eliminar_sms('1134567890', '1111111122', 'Donde estas?')

    print('\nMuestro la bandeja de mensajes. \n')
    celular1.ver_bandeja_sms()
    celular2.ver_bandeja_sms()
    celular3.ver_bandeja_sms()

    celular1.cerrar_mensajeria()
    celular2.cerrar_mensajeria()
    celular3.cerrar_mensajeria()

def funcionalidades_telefono():
    celular1.abrir_telefono()
    celular2.abrir_telefono()
    celular3.abrir_telefono()

    print('\nRealizo llamadas a un contacto, estableciendo una duracion. \n')
    central.llamada('1129999999', '1111111122', 5)

    print('\nRealizo llamadas a un contacto ocupado, entonces no me realizar la llamada. \n')
    central.llamada('1134567890', '1129999999', 7)

    print('\nMuestro el registro de llamadas. \n')
    celular1.imprimir_registro_emisor()
    celular2.imprimir_registro_destinatario()

    celular1.cerrar_telefono()
    celular2.cerrar_telefono()

def funcionalidades_calculadora():
    print('\n----------------------- \nAbro Calculadora y aplico los metodos \n----------------------- \n')
    celular1.abrir_calculadora()

    print('\nRealizo operaciones basicas. \n')
    celular1.usar_calculadora('sumar', 3, 5)
    celular1.usar_calculadora('multiplicar', 3, 5)
    celular1.evaluar_expresion("3 + 5 * (2 - 8)")
    celular1.evaluar_expresion("((300-50) + 30) + 2 * (300 * 2) /2")


    celular1.cerrar_calculadora()

def funcionalidades_lista_tareas():
    celular1.abrir_lista_tareas()
    celular1.agregar_tarea('Limpiar mi cuarto')
    celular1.agregar_tarea('Terminar TP de estructuras con los chicos')
    celular1.mostrar_tareas()
    celular1.eliminar_tarea('Limpiar mi cuarto')    
    celular1.mostrar_tareas()

# Main program
try:
      if __name__ == '__main__':
            print('\nSe crea la central \n')
            central = Central()
            central.cargar_datos()

            print('\nSe crean los celulares\n')
            celular1 = Celular(1, 'pedro', '1234', 'phone 8', 'IOs', 'version 8', '10', '123', '1129999999')
            celular2 = Celular(2, 'franco', '2020', 'phone 8', 'IOs', 'version 8', '10', '123', '1111111122')
            celular3 = Celular(3, 'joaco', '3245', 'Galaxy S21', 'Android', '11', '8', '128', '1134567890')

            print(celular1)
            print(celular2)
            print(celular3)

            print('\nSe agregan a la central los dispositivos\n')
            central.agregar_celular(celular1)
            central.agregar_celular(celular2)
            central.agregar_celular(celular3)

            print('\nSe encienden y desbloquean los celulares\n')
            celular1.encender_celular()
            celular1.desbloquear_celular('1234')
            celular2.encender_celular()
            celular2.desbloquear_celular('2020')
            celular3.encender_celular()
            celular3.desbloquear_celular('3245')

            celular1.abrir_tienda()
            celular2.abrir_tienda()
            celular3.abrir_tienda()

            print('\nDescargo las apps \n')    
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
            celular1.descargar_app(9, 'Lista_Tareas')
            celular1.cerrar_tienda()
            celular2.cerrar_tienda()
            celular3.cerrar_tienda()

            # Menú interactivo
            print("\n¿Qué deseas ver?")
            print("1. Funcionalidades de Mensajería")
            print("2. Funcionalidades de Teléfono")
            print("3. Funcionalidades de Calculadora")
            print("4. Funcionalidades de Contactos")
            print("5. Funcionalidades de Email")
            print("6. Funcionalidades de Configuracion")
            print("7. Funcionalidades de Tienda")
            print("8. Funcionalidades de Lista Tareas")

            opcion = input("Selecciona una opción (1-8): ")
            while opcion not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                  print("Opción no válida. Por favor, seleccione una opción correcta.")
                  opcion = input("Selecciona una opción (1-8): ")
                  
            if opcion == '1':
                  print("\nFuncionalidades de Mensajeria:")
                  funcionalidades_msj()

            elif opcion == '2':
                  print("\nFuncionalidades de Teléfono:")
                  funcionalidades_telefono()    

            elif opcion == '3':
                  print("\nFuncionalidades de Calculadora:")
                  funcionalidades_calculadora()

            elif opcion == '4':
                  print("\nFuncionalidades de Contactos:")
                  funcionalidades_contactos()

            elif opcion == '5':
                  print("\nFuncionalidades de Email:")
                  funcionalidades_email()

            elif opcion == '6':
                  print("\nFuncionalidades de Configuracion:")
                  funcionalidades_configuracion()

            elif opcion == '7':
                  print("\nFuncionalidades de Tienda:")
                  funcionalidades_tienda()

            elif opcion == '8':
                  print("\nFuncionalidades de Lista Tareas:")
                  funcionalidades_lista_tareas()

            #central.dispositivos_registrados.guardar()
            '''''

            Al ejecutar el metodo de arriba se van a guaradar todas las instancias de celuar 
            por lo que va a entorpecer la prueba del codigo. Sin embargo removiendo el # 
            el codigo funciona guardando los celulares en un diccionario en la clase Central
             los cuales podes acceder libremente.


            '''''
            central.guardar_datos()
except: 
      print("Error generico") 
      
      

    
    
    
    
    
    
    



          
    
    
