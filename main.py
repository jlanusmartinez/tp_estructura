#PREGUNTAR A LUCAS CUESTION DEL MAIN, COMO LO HACEMOS?
#PARA MANDAR MSJS/LLAMADAS NECESITO VERIFICAR YA LO TENGA AGENDADO
from class_App import Aplicacion
from class_Celular import Celular
from class_Central import Central
from class_Configuracion import Configuracion
from class_Contactos  import Contactos
from class_Email import Email
from class_Mensajeria import Mensajeria
from class_Tienda import Tienda 
from class_Calculadora import Calculadora
from class_Cronometro import Cronometro



if __name__ == '__main__':
    central=Central()
    celular1=Celular(1,'pedro',1234,'phone 8','IOs','version 8',200,123,1129999999)
    print(celular1)
    celular2=Celular(1,'franco','phone','sistema','3','4','200 gb',123,11111111)
    celular3=Celular(1,'franco','phone','sistema','3','4','200 gb',123,29292929)
    central.agregar_celular(celular2)
    central.agregar_celular(celular1)
    celular1.encender_celular()
    celular1.desbloquear_celular(1234)
    celular2.encender_celular()
    celular2.desbloquear_celular('phone')
    print(celular1)
    
    
    # celular1.descargar_app(8,'Calculadora')
    # celular1.descargar_app(7,'Cronometro')
    
    # celular1.abrir_calculadora()
    # celular1.usar_calculadora('sumar',2,4)
    
    # celular1.abrir_cronometro()
    # celular1.usar_cronometro('iniciar')
    
    
    
    # celular1.recibir_email_celular('franco','hola, como va')
    # celular1.recibir_email_celular('joaco','boca','10/10/2021 10:10:10')
    
    # celular1.ver_emails_por_fecha_celular()
    # celular1.recibir_email_celular('joaco','bocaaaaaaaaaaaaaaaaa','8/10/2017 10:10:10')
    # celular1.ver_emails_por_leidos_celular()
    
    # celular1.descargar_app(1,'Contactos')
    # celular1.agregar_contacto_celular('franco','11111111')
    # celular1.agregar_contacto_celular('franco','11111111')
    # celular1.ver_contactos_celular()
    # central.llamada(1234,11111111,10)
    # celular1.telefono.imprimir_registro()    
    # central.llamada(29292929,1234,50)
    # celular1.telefono.imprimir_registro()
    # central.enviar_sms(1234,11111111,'hola')
    # celular2.mensajeria.ver_bandeja_sms()
    # central.eliminar_sms(1234,11111111,'hola')
    # celular2.mensajeria.ver_bandeja_sms()
    
    
    
    
    # celular1.descargar_app(8,'Caluladora')

    # celular1.abrir_calculadora()
    # celular1.usar_calculadora('sumar',2,4)
    # celular1.cerrar_calculadora()
    # celular1.abrir_calculadora()
    # celular1.usar_calculadora('multiplicar',2,5)
    # celular1.mostrar_apps()
    
    
    
    # celular1.descargar_app(7,'Cronometro')

    # celular1.abrir_calculadora()
    # celular1.usar_cronometro('iniciar')
    # celular1.usar_calculadora('multiplicar',2,5)
    # celular1.mostrar_apps()
    
    
    celular1.abrir_tienda()
    celular1.descargar_app(1,'Contactos')
    celular1.cerrar_tienda()
    celular1.abrir_contactos()
    
    celular1.abrir_contactos()
    
    celular1.agregar_contacto_celular('franco','11111111')
    
    celular1.cerrar_contactos()
    celular1.abrir_tienda()
    celular1.descargar_app(2,'Mensajeria')   
    celular1.cerrar_tienda() 
    celular1.abrir_mensajeria()
    # celular1.ver_contactos_celular()
    # central.llamada(1234,11111111,10)
    # celular1.telefono.imprimir_registro()    
    # central.llamada(29292929,1234,50)
    central.enviar_sms(1129999999,11111111,'hola')
    
    # celular2.descargar_app(2,'Mensajeria')
    
    # celular2.ver_bandeja_sms()
    
   
    
    # celular1.ver_bandeja_sms()
    
    
    # celular2.ver_bandeja_sms()
    
    celular1.ver_bandeja_sms()
    
    celular2.abrir_tienda()
    
    celular2.descargar_app(2,'Mensajeria')
    
    celular2.cerrar_tienda()
    
    celular2.abrir_mensajeria()
    
    celular2.ver_bandeja_sms()
    
    central.enviar_sms(1129999999,11111111,'chauuu no contestess')
    
    celular2.ver_bandeja_sms()
    
    celular1.ver_bandeja_sms()  
    celular1.cerrar_mensajeria()
    
    

    celular1.ver_bandeja_sms()
    celular2.ver_bandeja_sms()
    
    #Hasta aca todo ok
    
    
    
    
    
    
    



          
    
    
