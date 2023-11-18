class Employee:
    def __init__(self, first_name: str="", last_name: str="", level: int=1, yrsService:int =0):
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.yrsService = yrsService
        
    def __ge__(self, other):
        ...
        
    def __lt__(self, other):
        ...
        
    def __le__(self, other):
        ...
        
    def __gt__(self, other):
        ...
        
    def __eq__(self, other):
        ...
        
def main():
    ...
    


if __name__ == '__main__':
    main() 
    
    