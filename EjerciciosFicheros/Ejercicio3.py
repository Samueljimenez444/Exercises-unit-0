import os

rutaFichero = 'C:/Users/samuel.jimenez/Desktop/Programacion/Ejercicios Tema 0/EjerciciosFicheros/datosEj3.txt'

fin = False

with open(rutaFichero, 'w') as f:  

    while (not fin):

        nombre = input("Introduce your name (or 'end' to finish): ")

        if nombre.lower() == "end":

            fin = True
            
        else:

            f.write(nombre + " ")
        
            edad = input("Introduce your age: ")

            f.write(edad + "\n")
