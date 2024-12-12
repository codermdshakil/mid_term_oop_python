
class Library:
    
    book_list = []
    
    def entry_book(book):
        Library.book_list.append(book)
        
        
class Book:
    
    def __init__(self, book_id, title, author, avaiablability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.avaiablability = avaiablability
        