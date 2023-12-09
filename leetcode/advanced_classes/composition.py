class Publication:
    def __init__(self, title:str, price:float):
        self.title = title
        self.price = price
        
        
class Author:
    def __init__(self, first_name:str, last_name:str, email:str, date_of_birth:str):
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f"(Author: first_name: {self.first_name}, last_name: {self.last_name} )"
    

class Chapter:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


class Book(Publication):
    def __init__(self, title: str, price: float, author:Author = None, pages:int = 0):
        super().__init__(title,  price)
        self.author = author
        self.pages = pages
        self.author = author
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
    book = Book("Things fall apart", 256, first_author)
  
    chapter_1 = Chapter('Naked Truth', 35)
    book.add_chapter(chapter_1)
    
    print(book)
 
    
if __name__ == '__main__':
    main()