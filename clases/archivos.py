#Importamos pandas para trabajar con el archivo csv
import pandas as pd

#Creamos la clase
class Notas():
    #Definimos el constructor
    def __init__(self, archivo):
        self.archivo = archivo
    
    def ejercicio1(self):
        data = pd.read_csv(self.archivo) #Leemos el archivo csv

        lista_diccionarios = []
        #Creamos una columna que contenga el nombre y apellidos
        data["Nombre completo"] = data["Apellidos"] + ", " + data["Nombre"]
        data.drop('Apellidos', inplace=True, axis=1) 
        data.drop('Nombre', inplace=True, axis=1) 

        #Ordenamos las filas por apellidos
        data = data.sort_values("Nombre completo")

        #Hacemos una lista con cada columna del csv
        parcial1 = list(data["Parcial1"])
        parcial2 = list(data["Parcial2"])

