# Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de cada palabra en el texto.

userString = input("Introduce a phrase")

dictionary = {}

wordList = userString.split(" ")

for word in wordList:
    
    timesWordAppears = wordList.count(word)
    dictionary[word] = timesWordAppears

print(dictionary)