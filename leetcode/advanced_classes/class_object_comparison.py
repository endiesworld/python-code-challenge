class Employee:
    def __init__(self, first_name: str="", last_name: str="", level: int=1, yrsService:int =0):
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.yrsService = yrsService
        
    def __ge__(self, other):
        if(self.level == other.level):
            return self.yrsService >= other.yrsService
        return self.level >= other.level
        
    def __lt__(self, other):
        if(self.level == other.level):
            return self.yrsService < other.yrsService
        return self.level < other.level
        
    def __le__(self, other):
        if(self.level == other.level):
            return self.yrsService <= other.yrsService
        return self.level <= other.level
        
    def __gt__(self, other):
        if(self.level == other.level):
            return self.yrsService > other.yrsService
        return self.level > other.level
        
    def __eq__(self, other):
        return self.level == other.level
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    
    def __repr__(self):
        return f"{self.first_name}, {self.last_name}"
        
def main():
    dept = []
    dept.append(Employee("Emmanuel", "Kamuma", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Dubem", "Emmanuel", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 12))
    dept.append(Employee("Ugo", "Alozie", 5, 11))
    
    
    print(dept[0] > dept[1])
    print(dept[2] > dept[1])
    print(dept[3] > dept[2])
    
    # Uses the __gt__ method to sort the array
    dept.sort()
    print(dept)


if __name__ == '__main__':
    main() 
    
    