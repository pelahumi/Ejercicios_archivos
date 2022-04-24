#Importamos pandas para trabajar con el archivo csv
import pandas as pd

#Creamos la clase
class Notas():
    #Definimos el constructor
    def __init__(self, archivo):
        self.archivo = archivo
    
    def ejercicio1(self):
        data = pd.read_csv(self.archivo) #Leemos el archivo csv
