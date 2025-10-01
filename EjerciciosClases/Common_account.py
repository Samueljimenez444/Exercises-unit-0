class Common_account:
    def __init__(self,dni,name,credit):

        self.dni = dni

        self.name = name

        self.credit = credit
    def __init2__(self,dni,credit):

        self.dni = dni

        self.credit = credit
    
    def extract_money(self,credit):

        is_able = True

        if(self.credit>=credit):
            self.credit-=credit
        else:
            is_able = False
        return is_able
    
    def add_money(self,credit):

        self.credit += credit


    def __str__(self):

        cadena = "Name: " + self.name + ", DNI: " + self.dni + ", Credit: " + str(self.credit)       

        return cadena
    
    def __eq__(self, object):
        
        equals = False

        if(self.name==object.name):
            equals = True
        return equals
    
    def __lt__(self,object):
        minor = False

        if(self.credit < object.credit):
            menor = True
        
        return minor

class main:
    account1 = Common_account("77873441H","Samuel",100)

    print(account1)

    account1.extract_money(50)

    print(account1)

    account1.add_money(100)

    print(account1)




