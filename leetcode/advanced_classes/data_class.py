"""
    Because classes exist to store and manipulate data via an object, python has in-built 'dataclass'
    to make it easy for users to create and manipulate data.
    
    dataclass also authomatically implements the '__str__' and '__repr__' methods, however, this can also be overrided.
    
    The __post_init__ function lets us customize additional properties
    after the object has been initialized via built-in __init__ method
    
    It also gives room to define args with default values, however arguments without defaults has to come earlier than the none dafult ones.

    You can also creat a class whose value is immutable by using the 'frozen=True' property of the dataclass
"""

from dataclasses import dataclass, field
import random

def random_price_generator():
    return float(random.randrange(10, 40))

@dataclass
class Author:
    first_name: str
    last_name: str
    email:str
    date_of_birth:str
        
    def __str__(self):
        return f"(Author: first_name: {self.first_name}, last_name: {self.last_name} )"
    

@dataclass
class Chapter:
    title: str
    pages: str


@dataclass
class Book:
    title: str = None
    author: Author = ''
    price: float = field(default_factory=random_price_generator)
    
    def __post_init__(self):
        self.chapters = []
    
    
    def add_chapter(self, chapter):
        self.chapters.append(chapter)
        
    def get_pages(self)->int:
        pages = 0 
        for chapter in self.chapters:
            pages += chapter.pages
        return pages

    def __str__(self) -> str:
        return f"Book (title: {self.title}, author: {self.author}, pages: {self.get_pages()}, price: {self.price})"
        

def main():
    first_author = Author('Emmanuel', 'Okoro', 'endiesworld@gmail.com', 'Dec-17-1986')
    book = Book("Things fall apart", first_author)
  
    chapter_1 = Chapter('Naked Truth', 35)
    book.add_chapter(chapter_1)
    
    print(book)
 
    
if __name__ == '__main__':
    main()