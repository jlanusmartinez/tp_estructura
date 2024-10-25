from class_App import Aplicacion
from class_Celular import Celular
from class_Central import Central
from class_Configuracion import Configuracion
from class_Contactos  import Contactos
from class_Email import Email
from class_Mensajeria import Mensajeria
from class_Tienda import Tienda 



if __name__ == '__main__':
    central=Central()
    celular1=Celular(1,'pedro','phone','sistema','3','4','200 gb',123,1234)
    print(celular1)
    celular2=Celular(1,'franco','phone','sistema','3','4','200 gb',123,11111111)
    celular3=Celular(1,'franco','phone','sistema','3','4','200 gb',123,29292929)
    central.agregar_celular(celular1)
    central.agregar_celular(celular2)
    central.agregar_celular(celular3)
    celular1.encender_celular()
    celular2.encender_celular()
    celular1.desbloquear_celular()
    celular2.desbloquear_celular()
    celular3.encender_celular()
    celular3.desbloquear_celular()
    celular1.mostrar_apps()
    celular1.descargar_app(3,'Email')
    celular1.mostrar_apps()
    celular1.mostrar_apps()
    celular1.recibir_email_celular('franco','hola',"22/10/2024 10:00:00")
    central.llamada(1234,11111111,10)
    central.llamada(29292929,11111111,90)
    celular1.telefono.imprimir_registro()
    celular3.telefono.imprimir_registro()    
    
    

    
    
    



          
    
    
