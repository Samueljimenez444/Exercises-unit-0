def numbersInBetween(number1, number2):

    maxNumber=max(number1,number2)
    
    minNumber=min(number1,number2)

    for counter in range (minNumber-1,maxNumber):
        print(counter)

number1User = int(input("Introduce a number"))
number2User = int(input("Introduce a number"))

numbersInBetween(number1User,number2User)
