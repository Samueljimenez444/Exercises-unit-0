
class Product:

    def __init__(self, name , price):

        self.name = name

        self.price = price

    def calculate(self, quantity):

        return self.price * quantity

    def __str__(self):
        
        return self.name + str(self.price)
    
    def __lt__(self,object):

        minor = False

        if(self.price < object.price):
            
            minor = True

        return minor


class PerishableProduct(Product):

    def __init__(self, name, price, daysToPerish):

        super().__init__(name, price)

        self.daysToPerish = daysToPerish

    def calculate(self, quantity):

        total = super().calculate(quantity)

        if(self.daysToPerish == 1):

            total = total/4

        elif(self.daysToPerish == 2):

            total = total/3

        elif(self.daysToPerish == 3):
            
            total = total/2

        return total

    def __str__(self):

        return super().__str__() + str(self.daysToPerish)
    
class NoPerishableProduct(Product):

    def __init__(self, name, price, type):

        super().__init__(name, price)

        self.type = type
    
    def calculate(self, quantity):

        return super().calculate(quantity)

    def __str__(self):
        
        return super().__str__() + type

class Main:
    
    product1 = PerishableProduct("Salmon" , 10 , 1)

    print(product1.calculate(10))




       
        