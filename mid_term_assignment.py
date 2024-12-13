class Library:
    
    # Class attribute to hold the list of books
    book_list = []

    @classmethod
    def entry_book(self, book):
        
        if isinstance(book, Book):
            self.book_list.append(book)
        else:
            raise TypeError("Only objects of the Book class can be added.")

    @classmethod
    def view_all_books(self):
        if self.book_list:
            for book in self.book_list:
                book.view_book_info()
        else:
            print("No books available in the library.")

    @classmethod
    def find_book_by_id(self, book_id):
        for book in self.book_list:
            if book.get_book_id() == book_id:
                return book
        return None

class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True

        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' has been borrowed.")
        else:
            print(f"Book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book '{self.__title}' has been returned.")
        else:
            print(f"Book '{self.__title}' was not borrowed.")

    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Not Available"
        print(f"Book ID: {self.__book_id}, Title: '{self.__title}', Author: '{self.__author}', Availability: {availability_status}")

    def get_book_id(self):
        return self.__book_id

def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Library.view_all_books()
        elif choice == "2":
            book_id = input("Enter the Book ID to borrow: ")
            book = Library.find_book_by_id(book_id)
            if book:
                book.borrow_book()
            else:
                print("Invalid Book ID.")
        elif choice == "3":
            
            book_id = input("Enter the Book ID to return: ")
            book = Library.find_book_by_id(book_id)
            
            if book:
                book.return_book()
            else:
                print("Invalid Book ID.")
                
        elif choice == "4":
            print("Exiting the library system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Example initialization of books
Book("1", "Atomic Habit", "James Clear")
Book("2", "Thinking Clearly ", "Rolf Dobelli")

# Start the menu system
menu()
