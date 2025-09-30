# Crea un programa que pida diez números reales por teclado, los almacene en una lista, y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.
numbers = []
for i in range (1, 11):
    userNumber= int(input("Introduce a number"))
    numbers.append(userNumber)

numbers.sort()    
print(numbers[0], numbers[-1])