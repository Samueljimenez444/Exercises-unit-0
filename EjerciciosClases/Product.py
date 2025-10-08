class Product:

    IVA = 21

    def __init__(self,name,price,quantity):
    
        self.name = name

        self.price = price

        self.quantity = quantity

    def getPvP(self):

        return self.price + self.price * self.IVA
    
    def getPvPDescuento(self, discount):
        
        totalPrice = self.price + self.price * self.IVA
        
        return totalPrice - (totalPrice *discount/100)
    
    def sellProduct(self, units):
        
        sold = False
        
        if(self.quantity - units >= 0):
            self.quantity -= units
            sold = True

        return sold
    
    def addUnits (self, units):
        
        self.quantity += units
        

        
    def __str__(self):
        
        return "Name: " + self.name + " Units: " + str(self.quantity) + " Price: " + str(self.price)
        
    def __eq__(self, object):
        
        equals = False
        
        if(self.name == object.name):
            
            equals = True
            
        return equals

    def __lt__(self , otherObject):
        
        minor = False
        
        if (self.name < otherObject.name):
            
            minor = True
            
        return minor    
        
        
class main:

    product1 = Product("Cereals" , 10 , 100)

    print(product1.getPvP())
    
    print(product1)