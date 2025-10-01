class Product:

    def __init__(self,name,price,quantity):
        
        iva = 0.21

        self.name = name

        self.price = price

        self.quantity = quantity

    def getPvP(self):

        return self.price + self.price * self.iva
    

class main:

    product1 = Product("Cereals" , 10 , 100)

    print(product1.getPvP)