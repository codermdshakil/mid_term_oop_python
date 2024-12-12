
class Library:
    
    book_list = []
    
    
        
        
class Book:
    
    def __init__(self, book_id, title, author, avaiablability):
        self.__book_id = book_id
        self._title = title
        self._author = author
        self._avaiablability = avaiablability
    
    def entry_book(self):
        Library.book_list.append(self)
        
    def borrow_book(self):
        if self._avaiablability == True:
            self._avaiablability = False
        else:
            self._avaiablability == True
            
    def return_book(self):
        if self._avaiablability == False:
            self._avaiablability = True
    
    def view_book_info(self):
        return f"Book id is : {self.__book_id}, Book name is : {self._title}, Book Author: {self._author} and Avaiablability is {self._avaiablability}"
    


python_book = Book(1,'Head first Python', 'Shakil', True)


print(python_book.view_book_info())




        
        