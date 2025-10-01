# Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario. La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. Crea un menú para las distintas opciones e implementa una función para cada opción.

print("Introduce 1 to add a contact, 2 to erase a contact and 3 to look for a contact ")

userSelecction = int(input("Introduce the option you want"))

contactList = {}

while(userSelecction != 0):
    
    if userSelecction == 1:

        name = input("Introduce the name")

        number = int(input("Introduce the number"))

        contactList[name] = number

    elif userSelecction == 2:
        print("Hi, introduce the number of the contact you want to erase")

        name = input("Introduce your name")

        del contactList[name]

    elif userSelecction == 3:
        print("Introduce the name of the contacto you want to search")
        
        name = input("Introduce your name")

        print(contactList[name])
        
    elif userSelecction == 4:
        print(contactList)

    userSelecction = int(input("Introduce the option you want"))