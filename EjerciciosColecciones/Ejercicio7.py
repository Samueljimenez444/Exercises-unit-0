# Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario. La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. Crea un menú para las distintas opciones e implementa una función para cada opción.

userSelecction = int(input("Introduce the option you want"))

print("Introduce 1 to add a contact, 2 to erase a contact and 3 to look for a contact ")

contactList = {}

if userSelecction == 1:
    print("Hi, introduce the name and number of the new contact")
    name = input("Introduce the name")

    number = int(input("Introduce the number"))

    contactList[name] = number

elif userSelecction == 2:
    print("Hi, introduce the number of the contact you want to erase")
    contactList

elif userSelecction == 3:
    print("Hello")
    
