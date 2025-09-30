# Realiza un programa que pida 8 números enteros y los almacene en una lista. A continuación, recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.

numbers = []
for i in range (1, 9):
    
    userNumber= int(input("Introduce a number"))

    numbers.append(userNumber)

for number in numbers:

    if(number%2==0):
        print("pair")

    else:
        print("odd")