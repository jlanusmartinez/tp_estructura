class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, item):
        """Agrega un elemento a la cima de la pila."""
        self.elementos.append(item)

    def desapilar(self):
        """Elimina y devuelve el elemento en la cima de la pila."""
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            print("La pila está vacía.")
            return None

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.elementos) == 0

    def tamano(self):
        """Devuelve el tamaño de la pila."""
        return len(self.elementos)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None 

    def __repr__(self):
        return f"Nodo({self.dato})"  


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza: 
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:  
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  

    def mostrar(self):
        actual = self.cabeza
        while actual:  
            print(actual.dato)
            actual = actual.siguiente

    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        while actual:  
            if actual.dato == dato:
                if previo:  
                    previo.siguiente = actual.siguiente
                else:  
                    self.cabeza = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
        return False  