"""
Implementing an interface allows a class to become more formal about the behavior it promises to provide. 
Interfaces form a contract between the class and the outside world.
If your class claims to implement an interface, all methods defined by that interface must appear in its source code
"""

from abc import ABC, abstractmethod

class Shapes(ABC):
    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def calc_area(self):
        ...
        

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class Circle(Shapes, JSONify):
    def __init__(self, radius):
        self.radius = radius
        
    # As as sub class of an abstract class(Shapes), we must implement the below method
    def calc_area(self):
        return 3.142 * pow(self.radius, 2)
    
    def toJSON(self):
        return f"{{'circles': {str(self.calc_area())}}}"
    
    
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
    print(circle.toJSON())

if __name__ == "__main__":
    main()
        
        