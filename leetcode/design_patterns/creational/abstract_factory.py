class Dog:
    """One of the objects to be returned
    """
    def __init__(self, name):
        self.name = name
        self.speaks = "Woof"
        
    def speak(self):
        return self.speaks
        
    def __repr__(self) -> str:
        return f"<Class Dog, name: {self.name}, speaks: {self.speak()}"
    
    def __str__(self) -> str:
        return f"Dog, name: {self.name}."
    
    
class PetFactory:
    """ Concrete Factory"""
    
    def get_pet(self):
        """Returns a Pet object"""
        return Dog("bingo")
        
    def get_food(self):
        """Returns a Pet food object"""
        return "Dog food"


class PetStore:
    """ PetStore houses the Abstract Factory """
    
    def __init__(self, pet_factory=None):
        """ pet_factory is the Abstract Factory"""
        self._pet_factory = pet_factory    
    
    def show_pet(self):
        """ Utility method to display the details of the object returned""" 
        
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print("Pet is '{}!".format(pet))
        print("Pet says  '{}!".format(pet.speak()))
        print("Pet's food is '{}!".format(pet_food))
        
        
# Create a concrete factory
factory = PetFactory()

# Create a pet store housing the Abstract Factory
shop = PetStore(factory)

# Invoke the utility method to show the details of the pet
shop.show_pet()