import random

randomNumber = random.randint(1,101)

print(randomNumber)

userNumber = int(input("Introduce your guess"))

while userNumber>100:
    userNumber = int(input("Introduce your guess (HIGHER THAN 100!)"))

while userNumber != randomNumber and userNumber >= 0:

    if(userNumber > randomNumber):
        print("The number you introduced is higher than the number you are guessing")

    elif(userNumber < randomNumber):
        print("The number you introduced is lower than the number you are guessing")

    userNumber = int(input("Introduce your guess"))

    if(userNumber>100):
        while userNumber>100:
            userNumber = int(input("Introduce your guess (HIGHER THAN 100!)"))


if(userNumber>=0):
    print("You won, the number was " , randomNumber)
else:
    print("Sorry, the number was " , randomNumber)