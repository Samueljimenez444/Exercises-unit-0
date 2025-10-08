class Animal:
    
    def __init__(self, name, legNumber):
        
        self.name = name

        self.legNumber = legNumber

    def talk (self):
        
        return ""
    
    def __str__(self):
        
        return "My name is " + self.name + " i have " + str(self.legNumber) + " legs " + "this is my sound:" + self.talk()

class Dog(Animal):
    
    def __init__(self, name,legNumber):
        
        super().__init__(name, legNumber)
    
    def talk(self):
        return super().talk() + "Wof woff"
    
    def __str__(self):
        return "Im a dog " + super().__str__()

class Cat(Animal):
    
    def __init__(self, name, legNumber):
        
        super().__init__(name, legNumber)
    
    def talk(self):
        return super().talk() + "Miauuu"
    
    def __str__(self):
        return "Im a cat " + super().__str__()

class Main:
    
    dog1 = Dog("Nube" , 4)
    
    cat1 = Cat("Phosqui", 4)
    
    print(dog1.talk())
    
    print(dog1)

    print(cat1)

    print(cat1.talk())    
    
        
        