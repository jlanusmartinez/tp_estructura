class Pila:
    def __init__(self):
        self.elementos = []  # Inicializa la lista vacía para almacenar los elementos de la pila

    def apilar(self, item):
        """Agrega un elemento a la cima de la pila."""
        self.elementos.append(item)  # Añade el item al final de la lista (la cima de la pila)

    def desapilar(self):
        """Elimina y devuelve el elemento en la cima de la pila."""
        if not self.esta_vacia():  # Si la pila no está vacía
            return self.elementos.pop()  # Elimina y devuelve el último elemento de la lista
        else:
            print("La pila está vacía.")  # Si la pila está vacía, muestra un mensaje de error
            return None  # Retorna None si no hay elementos en la pila

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.elementos) == 0  # Retorna True si la pila está vacía, False en caso contrario

    def tamano(self):
        """Devuelve el tamaño de la pila."""
        return len(self.elementos)  # Retorna la cantidad de elementos en la pila


class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato en el nodo
        self.siguiente = None  # Inicializa el puntero 'siguiente' como None (no apunta a ningún nodo)

    def __repr__(self):
        return f"Nodo({self.dato})"  # Representación en cadena del nodo para facilitar la depuración


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicializa la cabeza de la lista como None (lista vacía)

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        if not self.cabeza:  # Si la lista está vacía (no hay cabeza)
            self.cabeza = nuevo_nodo  # El nuevo nodo se convierte en la cabeza de la lista
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorre la lista hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # El último nodo apunta al nuevo nodo

    def mostrar(self):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        while actual:  # Mientras haya nodos en la lista
            print(actual.dato)  # Muestra el dato del nodo actual
            actual = actual.siguiente  # Avanza al siguiente nodo

    def eliminar(self, dato):
        actual = self.cabeza  # Comienza desde la cabeza de la lista
        previo = None  # No hay nodo previo al principio
        while actual:  # Recorre toda la lista
            if actual.dato == dato:  # Si encuentra el dato que coincide
                if previo:  # Si el nodo a eliminar no es la cabeza
                    previo.siguiente = actual.siguiente  # El nodo anterior apunta al siguiente nodo
                else:  # Si el nodo a eliminar es la cabeza
                    self.cabeza = actual.siguiente  # La cabeza apunta al siguiente nodo
                return True  # Retorna True si se eliminó el nodo
            previo = actual  # Actualiza el nodo previo
            actual = actual.siguiente  # Avanza al siguiente nodo
        return False  # Retorna False si no se encuentra el dato en la lista
