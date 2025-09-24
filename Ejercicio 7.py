userNumber = int(input("Introduce a number"))

isOdd = True

while userNumber <= 0:
    userNumber = int(input("Introduce a number"))


for contador in range (2, userNumber+1):
    if(userNumber % contador == 0 and contador != userNumber):
       isOdd=False

print(isOdd)  


