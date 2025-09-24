userNumber = int(input("Introduce your number"))

factorial = 1

for contador in range (userNumber, 0 , -1):
    factorial *= contador


print(factorial)