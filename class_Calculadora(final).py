from class_App import *

class Calculadora(Aplicacion):
    def __init__(self):
        super().__init__(8, "Calculadora")
    
    def sumar(self, a, b):
        if self.estado:
            resultado = a + b
            print(f"Resultado de {a} + {b} = {resultado}")
            return resultado
        else:
            print("La aplicación Calculadora no está abierta.")
    
    def restar(self, a, b):
        if self.estado:
            resultado = a - b
            print(f"Resultado de {a} - {b} = {resultado}")
            return resultado
        else:
            print("La aplicación Calculadora no está abierta.")
    
    def multiplicar(self, a, b):
        if self.estado:
            resultado = a * b
            print(f"Resultado de {a} * {b} = {resultado}")
            return resultado
        else:
            print("La aplicación Calculadora no está abierta.")
    
    def dividir(self, a, b):
        if self.estado:
            if b == 0:
                print("Error: No se puede dividir entre cero.")
                return None
            resultado = a / b
            print(f"Resultado de {a} / {b} = {resultado}")
            return resultado
        else:
            print("La aplicación Calculadora no está abierta.")
            
            
            
            
# Agregado para el Final 
    
    def evaluar_expresion(self, expresion):
        """Evalúa una expresión simbólica (con números, operadores y paréntesis)."""
        if not self.estado:
            print("La aplicación Calculadora no está abierta.")
            return None

        try:
            resultado = self._evaluar(expresion)
            print(f"El resultado de la expresión '{expresion}' es: {resultado}")
            return resultado
        except Exception as e:
            print(f"SyntaxError: {e}")
            return None

    def _evaluar(self, expresion):
        """Algoritmo para evaluar una expresión simbólica usando pilas."""
        def precedencia(op):
            """Devuelve la precedencia de un operador."""
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        def aplicar_operador(operadores, valores):
            """Aplica un operador a los dos últimos valores en la pila."""
            operador = operadores.pop()
            b = valores.pop()
            a = valores.pop()
            if operador == '+':
                valores.append(a + b)
            elif operador == '-':
                valores.append(a - b)
            elif operador == '*':
                valores.append(a * b)
            elif operador == '/':
                if b == 0:
                    raise ValueError("División por cero")
                valores.append(a / b)

        # **Elimina espacios en blanco de la expresión**
        expresion = expresion.replace(" ", "")


        operadores = []
        valores = []
        i = 0
        while i < len(expresion):
            c = expresion[i]
            if c.isdigit() or (c == '.' and i + 1 < len(expresion) and expresion[i + 1].isdigit()):
                # Extraer el número completo
                num = []
                while i < len(expresion) and (expresion[i].isdigit() or expresion[i] == '.'):
                    num.append(expresion[i])
                    i += 1
                valores.append(float(''.join(num)))
                continue
            elif c == '(':
                operadores.append(c)
            elif c == ')':
                while operadores and operadores[-1] != '(':
                    aplicar_operador(operadores, valores)
                operadores.pop()  # Remover '('
            elif c in '+-*/':
                while (operadores and operadores[-1] != '(' and
                       precedencia(operadores[-1]) >= precedencia(c)):
                    aplicar_operador(operadores, valores)
                operadores.append(c)
            else:
                raise ValueError(f"Carácter inválido: {c}")
            i += 1

        while operadores:
            aplicar_operador(operadores, valores)

        return valores[0]
