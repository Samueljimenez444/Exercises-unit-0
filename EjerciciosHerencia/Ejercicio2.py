class Employee:

   def __init__(self,name):
      
      self.name = name

   def setName(self,name):
      
        self.name = name

   def getName(self):
       
       return self.name
   
   def __str__(self):
       
       return "Employee " + self.name
   
class Operator(Employee):

    def __init__(self, name):

        super().__init__(name)

    def __str__(self):

       return super().__str__() + " Operator"

class Executive(Employee):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__() + " Executive"    
    
class Oficcer(Operator):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__() + " Oficcer" 
    
class Technician(Operator):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__() + " Technician"        

class Main:

    employee1 = Operator("Samuel")

    print(employee1)



        
        
   