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
    
    #Descargo las apps
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
    
  
   



          
    
    
