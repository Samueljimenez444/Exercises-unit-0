#1. Diseñar una aplicacion que solicite al usuario un numero e indique si es par o impar

numero = int(input("Introduce un numero"))

def parimpar(numero):

    par = False
    
    if(numero % 2== 0):
        par = True
    
    return par

if(parimpar(numero) == True):
    print("Es par")

else:
    print("Es impar")



