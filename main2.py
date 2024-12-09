from class_Celular import Celular
from class_central import Central
import datetime

# Crear centrales
central1 = Central()
central2 = Central()
central3 = Central()    




celular1 = Celular(1, 'pedro', '1234', 'phone 8', 'IOs', 'version 8', '10', '123', '1129999999')
celular2 = Celular(2, 'franco', '2020', 'phone 8', 'IOs', 'version 8', '10', '123', '1111111122')
celular3 = Celular(3, 'joaco', '3245', 'Galaxy S21', 'Android', '11', '8', '128', '1134567890')
print(celular1)

print('\nSe agregan a la central los dispositivos\n')

central1.agregar_celular(celular1)
central2.agregar_celular(celular2)
central3.agregar_celular(celular3)

central1.conectar_central(central2)
central1.conectar_central(central2)
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
celular1.cerrar_tienda()
celular2.cerrar_tienda()
celular3.cerrar_tienda()


celular1.abrir_telefono()
celular2.abrir_telefono()
celular3.abrir_telefono()

central1.llamada('1129999999', '1111111122', 5)
central3.llamada('1134567890', '1129999999', 7)

celular1.imprimir_registro_emisor()
celular2.imprimir_registro_destinatario()

celular1.cerrar_telefono()
celular2.cerrar_telefono()


