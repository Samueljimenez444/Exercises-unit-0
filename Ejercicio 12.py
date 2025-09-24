def calculator (number1,number2,operator):
    
    calculator = 0

    match operator:
        case 1:
            calculator = number1+number2

        case 2:
            calculator = number1-number2

        case 3:
            calculator = number1*number2

        case 4:
            calculator = number1/number2

    return calculator

number1User = int(input("Introduce a number"))

number2User = int(input("Introduce a number"))

operator = int(input("Introduce 1 to summ 2 to sustract 3 to multiply and 4 to divide"))

print(calculator(number1User,number2User,operator))
