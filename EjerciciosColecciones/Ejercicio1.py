#Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 
import random
intList = []

for i in range (1,11):
    randomNumber = random.randint(1,100)
    intList.append(randomNumber)


print(intList)