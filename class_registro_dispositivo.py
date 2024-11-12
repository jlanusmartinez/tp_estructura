import pickle
from class_Celular import Celular


class Registro_dispositivos (dict):

    def __init__(self):
       super().__init__()
       try :
        self.leer()
       except Exception as e:
        print('No hay archivo para leer')
        print(e)
        
    # recupera los datos del archivo y los guarda en el diccionario

    def inicializar (self,diccionario:dict):
            for key , values in diccionario.items():
                self[key]=values
            Celular.inicializar_ids(diccionario.values())
    
    # lee los datos del archivo y los guarda en el diccionario con inicializar
    def leer(self):
         with open('dispositivos_registrados.pkl','rb') as f:
              registro=pickle.load(f)
              self.inicializar(registro)

    # almacena los datos en el archivo pickle
    def guardar(self): 
        if self.values(): 
            with open('dispositivos_registrados.pkl','wb') as f:
                pickle.dump(self,f)

