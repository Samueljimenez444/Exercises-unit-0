import math

class Dot:

    def __init__(self,x,y):
        self.x = x

        self.y = y
    
    def setXY(self, x , y):
        self.x = x

        self.y = y
    
    def desplaza(self,dx, dy):
        self.x += dx

        self.y += dy
    
    def  distance(self,dot2):
        
        distance = math.sqrt((dot2.x-self.x)**2 + (dot2.y-self.y)**2)

        return distance
    
    def __str__(self):
        cadena = str(self.x) + " " + str(self.y)

        return cadena
    
class main:

    dot1 = Dot(5,5)

    dot2 = Dot(10,10)
    
    dot1.desplaza(3,3)

    print(dot1)

    dot1.setXY(5,5)

    print(dot1)

    print(dot1.distance(dot2))  

