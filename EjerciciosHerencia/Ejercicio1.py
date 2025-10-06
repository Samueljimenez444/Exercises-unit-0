class Animal:
    
    def __init__(self, name):
        
        self.name = name

    def talk (self):
        
        return " "
    
    def __str__(self):
        
        return "my name is " + self.name + " i have x legs and my sound is this: "

class Dog(Animal):
    
    def __init__(self, name):
        
        super().__init__(name)
    
    def talk(self):
        return super().talk() + "Wof woff"
    
    def __str__(self):
        return "Im a dog " + super().__str__()

class Cat(Animal):
    
    def __init__(self, name):
        
        super().__init__(name)
    
    def talk(self):
        return super().talk() + "Miauuu"
    
    def __str__(self):
        return "Im a cat " + super().__str__()

class Main:
    
    dog1 = Dog("Nube")
    
    cat1 = Cat("Phosqui")
    
    print(dog1.talk())
    
    print(dog1)
    
    
        
        