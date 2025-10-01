encrypted = {"e" : "p" , "i" : "v" , "k" : "i" , "m" : "u" , "p" : "m" , "q" : "t" , "r" : "e" , "s" : "r" , "t" : "k" , "u" : "q" , "v" : "s"}

user_phrase = input("Introduce the phrase you want to cypher")

cypher_phrase = ""

for letter in user_phrase:
    
    cypher_phrase += str(encrypted.get(letter, letter))
    

print(cypher_phrase)