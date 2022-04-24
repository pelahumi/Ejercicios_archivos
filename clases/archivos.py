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
        asistencia = list(data["Asistencia"])
        parcial1 = list(data["Parcial1"])
        parcial2 = list(data["Parcial2"])
        nombre_completo = list(data["Nombre completo"])

        #Creamos un bucle que vaya recorriendo todas las filas y meta los datos en un diccionario
        for i in range(len(nombre_completo)):
            dicccionario = {"Nombre" : "{}".format(nombre_completo[i]), "Asistencia" : asistencia[i], "Primer parcial" : parcial1[i], "Segundo parcial" : parcial2[i]}
            #Añadimos a la lista que creamos al principio cada diccionario
            lista_diccionarios.append(dicccionario)
        return "Lista con las notas de los parciales y asistencia a clase: {}".format(lista_diccionarios)
    
    def ejercicio2(self):
        #Reutilizando el codigo del metodo anterior añadimos el nuevo par de elementos a cada diccionario
        data = pd.read_csv(self.archivo) 

        lista_diccionarios = []
    
        data["Nombre completo"] = data["Apellidos"] + ", " + data["Nombre"]
        data.drop('Apellidos', inplace=True, axis=1) 
        data.drop('Nombre', inplace=True, axis=1) 

        data = data.sort_values("Nombre completo")

        #Cambiamos los valores nulos del examen de prácticas por un 0
        data["OrdinarioPracticas"].fillna(0, inplace= True)

        asistencia = list(data["Asistencia"])
        parcial1 = list(data["Parcial1"])
        parcial2 = list(data["Parcial2"])
        nombre_completo = list(data["Nombre completo"])
        ordinario_practicas = list(data["OrdinarioPracticas"])

        for i in range(len(nombre_completo)):
            dicccionario = {"Nombre" : "{}".format(nombre_completo[i]), "Asistencia" : asistencia[i], "Primer parcial" : parcial1[i], "Segundo parcial" : parcial2[i], "Nota final" : (parcial1[i] * 0.3 + parcial2[i] * 0.3 + ordinario_practicas * 0.4)}
            #Añadimos a la lista que creamos al principio cada diccionario
            lista_diccionarios.append(dicccionario)
        return "Lista con las notas de los parciales, asistencia a clase y nota final: {}".format(lista_diccionarios)
    
    def ejercicio3(self):
        data = pd.read_csv(self.archivo)

        #Creamos las listas de alumnoz aprobados y suspensos
        aprobados = []
        suspensos = []

        asistencia = list(data["Asistencia"])
        parcial1 = list(data["Parcial1"])
        parcial2 = list(data["Parcial2"])
        nombre_completo = list(data["Nombre completo"])
        ordinario_practicas = list(data["OrdinarioPracticas"])

        for i in range(len(nombre_completo)):
            nota_final = parcial1[i] * 0.3 + parcial2[i] * 0.3 + ordinario_practicas * 0.4
            if asistencia >= 0.75 and parcial1 >= 4 and parcial2 >= 4 and ordinario_practicas >= 4 and nota_final >= 5:
                aprobados.append(nombre_completo[i])
            else:
                suspensos.append(nombre_completo[i])
        return "Lista con los alumnos aprbados: {}, y otra con los suspensos: {}".format(aprobados, suspensos)


