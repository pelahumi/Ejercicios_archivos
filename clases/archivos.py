#Importamos pandas para trabajar con el archivo csv
import pandas as pd

#Creamos la clase
class Notas():
    #Definimos el constructor
    def __init__(self, archivo):
        self.archivo = archivo
