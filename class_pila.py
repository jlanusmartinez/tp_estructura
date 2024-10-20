class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        """Agrega un elemento al final de la cola."""
        self.elementos.append(item)

    def desencolar(self):
        """Elimina y devuelve el primer elemento de la cola."""
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            print("La cola está vacía.")
            return None

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.elementos) == 0

    def tamano(self):
        """Devuelve el tamaño de la cola."""
        return len(self.elementos)
    