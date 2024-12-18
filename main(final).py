from class_Celular import Celular
from class_central import Central
from class_Calculadora import Calculadora

try:
      if __name__ == '__main__':
            print('\nSe crean las centrales \n')
            central1 = Central()
            central2 = Central()
            central3 = Central()    

            print('\nSe crean los celulares\n')
            celular1 = Celular(1, 'pedro', '1234', 'phone 8', 'IOs', 'version 8', '10', '123', '1129999999')
            celular2 = Celular(2, 'franco', '2020', 'phone 8', 'IOs', 'version 8', '10', '123', '1111111122')
            celular3 = Celular(3, 'joaco', '3245', 'Galaxy S21', 'Android', '11', '8', '128', '1134567890')
            print(celular1)

            print('\nSe agregan a la central los dispositivos\n')

            central1.agregar_celular(celular1)
            central2.agregar_celular(celular2)
            central3.agregar_celular(celular3)
            
            
            print('\nConecto las centrales 1 y 2\n')
            
            central1.conectar_central(central2)
            
            print('\nSe encienden y desbloquean los celulares\n')
            
            celular1.encender_celular()
            celular1.desbloquear_celular('1234')
            celular2.encender_celular()
            celular2.desbloquear_celular('2020')
            celular3.encender_celular()
            celular3.desbloquear_celular('3245')
            
            print('\nDescargo las apps \n') 
            celular1.abrir_tienda()
            celular2.abrir_tienda()
            celular3.abrir_tienda()
               
            celular1.descargar_app(4, 'Telefono')
            celular2.descargar_app(4, 'Telefono')
            celular3.descargar_app(4, 'Telefono')
            
            celular1.descargar_app(8, 'Calculadora')
            
            celular1.cerrar_tienda()
            celular2.cerrar_tienda()
            celular3.cerrar_tienda()
            
          
            print('\n-----------------------------------------\n')
            
            
          # Menú interactivo
            print("\n¿Qué deseas ver?")
            print("1. Funcionalidades de Telefono")
            print("2. Funcionalidades de Calculadora")

            opcion = input("Selecciona una opción (1-2): ")
            while opcion not in ["1", "2"]:
                  print("Opción no válida. Por favor, seleccione una opción correcta.")
                  opcion = input("Selecciona una opción (1-2): ")
            
            if opcion == '1':
                

                celular1.abrir_telefono()
                celular2.abrir_telefono()
                celular3.abrir_telefono()
                
                # LLamada entre dos celulares en distintas centrales conectadas 
                central1.llamada('1129999999', '1111111122', 5)
                
                # LLamada entre dos celulares en distintas centrales no conectadas
                central3.llamada('1134567890', '1129999999', 7)

                celular1.imprimir_registro_emisor()
                celular2.imprimir_registro_destinatario()

                celular1.cerrar_telefono()
                celular2.cerrar_telefono()
            elif opcion == '2':
                
                celular1.abrir_calculadora()
                celular1.usar_calculadora('sumar', 3, 5)
                celular1.usar_calculadora('multiplicar', 3, 5)
                celular1.evaluar_expresion("3 + 5 * (2 - 8)")
                celular1.evaluar_expresion("((300-50) + 30) + 2 * (300 * 2) /2")
                
                # Errores al dividir por cero
                celular1.evaluar_expresion("((300-50) + 30) + 2 * (300 * 2) /0")
                celular1.usar_calculadora('dividir', 3, 0)
                
                # Error de sintaxis
                celular1.evaluar_expresion("((300-50) + 30)) + 2 * (300 * 2)")
                
                celular1.cerrar_calculadora()
except: 
      print("Error generico") 
      

