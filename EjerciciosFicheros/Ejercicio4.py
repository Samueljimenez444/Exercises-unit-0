# Archivo de entrada
ruta_fichero = 'C:/Users/samuel.jimenez/Desktop/Programacion/Ejercicios Tema 0/EjerciciosFicheros/ficheroEj4.txt'

data = []

with open(ruta_fichero, 'rt') as f:

    for number in f:

        data.append(number.strip())


data.sort()

ruta_fichero_salida = 'C:/Users/samuel.jimenez/Desktop/Programacion/Ejercicios Tema 0/EjerciciosFicheros/datosEj4.txt'

with open(ruta_fichero_salida, 'w') as f2:
    
    f2.write("\n".join(data) + "\n")

print(data)
