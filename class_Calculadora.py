from class_App import *

class Calculadora(Aplicacion):
    def __init__(self):
        super().__init__(8,"Calculadora")
    
    def sumar(self, a, b):
        if self.abierta:
            resultado = a + b
            print(f"Resultado de {a} + {b} = {resultado}")
            return resultado
        else:
            print("La aplicación Calculadora no está abierta.")
    
    def restar(self, a, b):
        if self.abierta:
            resultado = a - b
            print(f"Resultado de {a} - {b} = {resultado}")
            return resultado
        else:
            print("La aplicación Calculadora no está abierta.")
    
    def multiplicar(self, a, b):
        if self.abierta:
            resultado = a * b
            print(f"Resultado de {a} * {b} = {resultado}")
            return resultado
        else:
            print("La aplicación Calculadora no está abierta.")
    
    def dividir(self, a, b):
        if self.abierta:
            if b == 0:
                print("Error: No se puede dividir entre cero.")
                return None
            resultado = a / b
            print(f"Resultado de {a} / {b} = {resultado}")
            return resultado
        else:
            print("La aplicación Calculadora no está abierta.")