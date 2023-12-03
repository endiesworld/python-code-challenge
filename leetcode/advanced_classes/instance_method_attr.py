from enum import Enum
# from typing import str, int, float

#  You can prevent dublicate value by using the "@unique" 
class BookType(Enum):
    HARDCOVER = "Hard Cover"
    PAPERBACK = "Paper Back"
    EBOOK = "E_book"

# All python classes inherit from the 'object' class
class Book:
    def __init__(self, title: str, author: str, pages: int, price:float, book_type:BookType):
        
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        try:
            self.book_type = BookType[book_type].value
        except KeyError:
            raise Exception(f"{book_type} not a valid book type")
        
    def get_price(self)-> float:
        # Use the hasattr method to chect if an instance has the attribute _discount
        if hasattr(self, '_discount'):
            return self.price - (self.price * (self._discount / 100))
        return self.price
    
    def set_discount(self, discount: int):
        self._discount = discount
        
    def __str__(self) -> str:
        return f"Book (title: {self.title}, author: {self.author}, pages: {self.pages}, price: {self.get_price()}, book type: {self.book_type})"
        
        
def main():
    book1 = Book("Things fall apart", "Chinua Achebe", 256, 15000.87, 'HARDCOVER')
    book2 = Book("Half of a Yellow Sun", "Chimamanda Adichie", 356, 25000.87, 'EBOOK')
    # book3 = Book("Half of a Yellow Sun", "Chimamanda Adichie", 356, 25000.87, 'BOOK')
    
    book2.set_discount(5)
    
    print(book1)
    print(book2)
    
    # To check the type of an object, we use the type function
    print(f"book1 belongs to the class {type(book1)}")
    print(f"Does book1 and books2 belongs to the same class? {type(book1) == type(book2)}") 
    
    # Use 'isinstance' to comapre if a specific object is an instance of a known class(type)
    print(f"book1 belongs to the class {isinstance(book1, Book)}")
    print(f"Does book1 and books2 belongs to the same class? {isinstance(book1, Book) == isinstance(book2, Book)}") 

if __name__ == '__main__':
    main()