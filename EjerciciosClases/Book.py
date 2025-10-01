class Book:
    def __init__(self,title,author,quantity,borrowed_books):

        self.title = title

        self.author = author

        self.quantity = quantity

        self.borrowed_books = borrowed_books


    def borrow_a_book(self,quantity):

        borrowed = False

        if(self.quantity >= quantity):

            self.quantity -= quantity

            self.borrowed_books += quantity

            borrowed = True
    def return_a_book(self , quantity):

        self.quantity += quantity

        self.borrowed_books -= quantity
        
    def __str__(self):

        cadena = "Title " + self.title + ", Author: " + self.author + ", Quantity Avaliable: " + str(self.quantity) + " Borrowed Books: " + str(self.borrowed_books)      

        return cadena
    
    def __eq__(self, object):
        
        equals = False

        if(self.title==object.title):
            equals = True

        return equals
    
    def __lt__(self,object):
        minor = False

        if(self.author < object.author):
            menor = True
        
        return minor

class main:

    book1 = Book("Rebelion en la granja" , "George Orwell" , 10 , 5)

    print(book1)

    book1.borrow_a_book(5)

    print(book1)

    book1.return_a_book

              


        