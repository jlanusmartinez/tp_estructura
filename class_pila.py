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