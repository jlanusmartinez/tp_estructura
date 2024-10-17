class Contacto :
    
    def __init__(self,nombre , numero_telefono):
        self.nombre=nombre
        self.numero_telefono=numero_telefono
    
    def set_nombre(self,nuevo_nom):
        self.nombre=nuevo_nom
        
        
    def set_numero(self,nuevo_num):
        self.numero_telefono=nuevo_num  
    
    def __str__(self):
        return f"Contacto({self.nombre}, {self.numero_telefono})"
          
   
