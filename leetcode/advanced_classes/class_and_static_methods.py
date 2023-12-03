from enum import Enum, unique

# class attributes
'''
Class attributes belong to the class itself they will be shared by all the instances. 
Such attributes are defined in the class body parts usually at the top, for legibility.
'''

# Class method
"""
method marked with '@classmethod' decorator is a class method.

Instead of accepting a self parameter, 
class methods take a cls parameter that points to the class—and not the object instance—when the method is called.

Because the class method only has access to this cls argument, 
it can’t modify object instance state. That would require access to self. 
However, class methods can still modify class state that applies across all instances of the class.
    
"""

#  You can prevent dublicate value by using the "@unique" 
class BookType(Enum):
    HARDCOVER = "Hard Cover"
    PAPERBACK = "Paper Back"
    EBOOK = "E_book"
    

class Book:
    
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    
    # Double underscore properties are hidden from other classes, but not completely
    __book_list = None
    
    def __init__(self, title: str, author: str, pages: int, price:float, book_type:str):
        
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        if (book_type not in Book.BOOK_TYPES):
            raise ValueError(f"{book_type} is not a valid book type")
        self.book_type = book_type
        
    
    # Create a class method to return a book type
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    
    # Creae a static method to return a book list
    @staticmethod
    def get_book_list():
        if Book.__book_list == None:
            Book.__book_list = []
        return Book.__book_list
        
    def get_price(self)-> float:
        # Use the hasattr method to chect if an instance has the attribute _discount
        if hasattr(self, '_discount'):
            return self.price - (self.price * (self._discount / 100))
        return self.price
    
    def set_discount(self, discount: int):
        self._discount = discount
        
    def __str__(self) -> str:
        return f"Book (title: {self.title}, author: {self.author}, pages: {self.pages}, price: {self.get_price()})"
        
    def __repr__(self) -> str:
        return f"Book (title: {self.title}, author: {self.author}, pages: {self.pages}, price: {self.get_price()})"
       
        
def main():
    # Access the book types with the help of a class method
    print('The valid book types are:', Book.get_book_types())
    
    book1 = Book("Things fall apart", "Chinua Achebe", 256, 15000.87, 'HARDCOVER')
    book2 = Book("Half of a Yellow Sun", "Chimamanda Adichie", 356, 25000.87, 'EBOOK')
    # book3 = Book("Half of a Yellow Sun", "Chimamanda Adichie", 356, 25000.87, 'BOOK')
    
    # Access book list with the help of a singleton method
    book_list = Book.get_book_list()
    book_list.append(book1)
    book_list.append(book2)
    
    print(book_list)
    
    
if __name__ == '__main__':
    main()