#Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.

numbers = []

for i in range (1 , 11):

    userNumber = int(input("Introduce ten numbers"))

    numbers.append(userNumber)

numbers.sort()

print(numbers)