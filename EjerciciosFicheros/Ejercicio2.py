import os

rutaFichero = 'C:/Users/samuel.jimenez/Desktop/Programacion/Ejercicios Tema 0/EjerciciosFicheros/ficheroEjercicio2.txt'

f = open(rutaFichero, 'w')

userInput = input("Introduce what you want to write in the file")

while(userInput != "end"):

    f.write(userInput+ "\n")

    userInput = input("Introduce what you want to write in the file")

f.close()
