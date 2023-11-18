class Point():
    def __init__(self, x:int = 0, y: int = 0):
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return f"< Class Point -x: {self.x}, y: {self.y}"
    
    def __add__(self, other):
        x = pow((self.x + other.x), 0.5)
        y = pow((self.y + other.y), 0.5)
        return Point(x, y)
    
    def __sub__(self, other):
        x = pow((self.x - other.x), 0.5)
        y = pow((self.y - other.y), 0.5)
        return Point(x, y)
        
    #This is for in-place addition 
    def __iadd__(self, other):
        print("In-place addition taking place")
        self.x = pow((self.x + other.x), 0.5)
        self.y = pow((self.y + other.y), 0.5)
        return self
        
        
def main():
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)
    
    p3 = p1 + p2
    p4 = p2 - p1
    print(p3)
    print(p4)
    
    p1 += p2
    print(p1)
    
if __name__ == '__main__':
    main()