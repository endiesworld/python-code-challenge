"""
    An abstract base class is a class that is used as a blueprint for other classes.
    An abstract base class is “Abstract” because it is non-existent.
    it’s just an ideal way for some other class to exist, but it cannot exist on its own.
    Abstract methods are those methods without implementation or which are without the body. 
"""

from abc import ABC, abstractmethod

class Shapes(ABC):
    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def calc_area(self):
        ...
        

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
        
    # As as sub class of an abstract class(Shapes), we must implement the below method
    def calc_area(self):
        return 3.142 * pow(self.radius, 2)
    
    
class Square(Shapes):
    def __init__(self, length):
        self.length = length
        
    # As as sub class of an abstract class(Shapes), we must implement the below method
    def calc_area(self):
        return pow(self.length, 2)
    
    
def main():
    
    # shape = Shapes(), This isn't possible because Shapes inherits from python ABC (Absract base class)
    
    circle = Circle(radius=7)
    square = Square(length=7)
    
    print(f"The area for this circle is: {circle.calc_area()}")
    print(f"The area for this square is: {square.calc_area()}")
    

if __name__ == "__main__":
    main()