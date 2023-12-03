class Publication:
    def __init__(self, title:str, price:float):
        self.title = title
        self.price = price
        
        
class PeriodicalPublication(Publication):
    def __init__(self, title:str, price:float, period:str, publisher:str):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher
        
        
class Book(Publication):
    def __init__(self, title: str, author:str, page:int, price: float):
        super().__init__(title,  price)
        self.author = author
        self.page = page
        
    def __str__(self) -> str:
        return f"Book (title: {self.title}, author: {self.author}, pages: {self.page}, price: {self.price})"
        
        
class Magazine(PeriodicalPublication):
    def __init__(self, title:str, price:float, period:str, publisher:str):
        super().__init__(title, price, period, publisher)
        
    def __str__(self) -> str:
        return f"Magazine (title: {self.title}, author: {self.period}, publisher: {self.publisher})"
        

class Newspaper(PeriodicalPublication):
    def __init__(self, title:str, price:float, period:str, publisher:str):
        super().__init__(title, price, period, publisher)
        
    def __str__(self) -> str:
        return f"Newspaper (title: {self.title}, author: {self.period}, publisher: {self.publisher})"
        
        
def main():
    book = Book("Things fall apart", "Chinua Achebe", 256, 15000.87)
    magazine = Magazine("Sun set in the city", 6000, "Dec 2023", 'Money bag Inc.')
    news_paper = Newspaper("Daily Punch", 1500, "03-Dec-2023", 'Punch.')
    
    print(book)
    print(magazine)
    print(news_paper)
    
if __name__ == '__main__':
    main()