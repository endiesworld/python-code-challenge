class A:
    def __init__(self):
        self.props_a = "props from class A"
        self.name = "Class A"
        

class B:
    def __init__(self):
        self.props_b = "props from class B"
        self.name = "Class B"
        
        
class C(A, B):
    def __init__(self):
        super().__init__()

    def show_props(self):
        print(self.props_a)
        print(self.props_a)
        print(self.name) # prints the name props in class A beacise A is inherited first
        
        

def main():
    print(f"The class other for C is {C.__mro__}")
    
    c = C()
    c.show_props()
    
    
if __name__ == '__main__':
    main()