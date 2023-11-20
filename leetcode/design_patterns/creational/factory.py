import sys
from typing import Union

class Dog:
    def __init__(self, name):
        self.name = name
        self.speaks = "Woof"
        
    def speak(self):
        return self.speaks
        
    def __repr__(self) -> str:
        return f"<Class Dog, name: {self.name}, speaks: {self.speak()}"
    

class Cat:
    def __init__(self, name):
        self.name = name
        self.speaks = "Meoow"
        
    def speak(self):
        return self.speaks
        
    def __repr__(self) -> str:
        return f"<Class Cat, name: {self.name}, speaks: {self.speak()}"
    
# Factory method
def get_pet(pet: str="dog")-> Union[Dog, Cat]:
    """_summary_
        The factory method used to create a new instance of a pet type

    Args:
        pet (str, optional): type of pet("dog" or "cat" for now). Defaults to "dog".

    Returns:
        Union[Dog, Cat]: A dog object or a cat object
    """
    pets = {
        'dog': Dog('Sebia'),
        'cat': Cat('busu'),
    }
    
    return pets[pet]
    
def main(pet: str=None):
    my_pet = get_pet(pet) if pet is not None else get_pet()
    print(f"This is how the pet you have chosen speaks: {my_pet.speak()}")
    

if __name__ == '__main__':
    # Access the command line arguments
    pet = None
    
    if len(sys.argv) > 1:
        pet = sys.argv[1]
    
    if (pet == 'dog' or pet == 'cat'):
        main(pet)
    elif(pet == None):
        print("You have not specified your choice of pet, we would recommend a dog.")
        main()
    else:
        print("We do not sell such pets here, please")