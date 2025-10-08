import os


ruta_fichero = 'C:/Users/samuel.jimenez/Desktop/Programacion/Ejercicios Tema 0/EjerciciosFicheros/ficheroEj1.txt'

f = open(ruta_fichero, 'rt')

counter = 0

age = 0

height = 0.0

for line in f.readlines():

    counter += 1

    print(line, end="")

    data = line.split()

    age += int(data[1])
    
    height += float(data[2])
    
f.close()

print()

print("The age media is ")
print(age/counter)

print("The height media is")
print(height/counter)

    