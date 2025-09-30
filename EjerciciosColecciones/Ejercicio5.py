# Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10 (utiliza 1 + Math.random()*10). Luego pedirá un valor N y mostrará cuántas veces aparece N. 
import random

count = 0

numbers = []

for i in range (1, 101):

    randomNumber = random.randint(1,10)
    
    numbers.append(randomNumber)


userNumber = int(input("Introduce the number you want to research about"))

for number in numbers:

    if(userNumber==number):

        count+=1  

print(count)

print(numbers)