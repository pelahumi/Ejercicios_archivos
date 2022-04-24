from clases.archivos import * 

if __name__ == "__main__":

    calificaciones = Notas("calificaciones.csv")

    print("EJERCICIO 1:", "\n")
    print(calificaciones.ejercicio1())

    print("EJERCICIO 2:", "\n")
    print(calificaciones.ejercicio2())

    print("EJERCICIO 3:", "\n")
    print(calificaciones.ejercicio3)
    
