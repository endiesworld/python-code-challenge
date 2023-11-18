class Person:
    def __init__(self, first_name: str='', last_name: str='', age: int=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # By overloading these methods you have full control over how your object is represented
    
    # Basically used for debugging purposes
    # __repr__ will be called for str if __str__ is not overridden
    def __repr__(self) -> str:
        return f"<Person Class -first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age}"
        
    def __str__(self) -> str:
        return f"Person (first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age})"
        
    # You coulsalso override the byte methos as well
    
def main():
    
    person_1 = Person('Emmanuel', 'Okoro', 37)
    
    print(repr(person_1))
    print(str(person_1))
    print("Formated: {0}".format(person_1))
    
    
if __name__ == "__main__":
    main()