# Crea un diccionario donde las claves son las letras del abecedario y los valores, la puntuación para cada letra, como en el Scrabble. El programa le pedirá una palabra al usuario y se mostrará por pantalla la puntuación que tiene la palabra en total.
import random
letter_points = {}

points = random.randint(1,27)

character = "a"

for i in range (1, 27):   

    letter_points[character] = points

    points = random.randint(1,27)
    character = chr(ord(character) + 1)


user_phrase = input("Introduce a phrase")

points = 0

user_phrase = user_phrase.lower()

for letter in user_phrase:

    points += letter_points.get(letter, 0)

print("You have won" ,points , "Points")