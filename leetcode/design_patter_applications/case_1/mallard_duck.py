from duck_class import Duck
from fly_with_wing import FlyWithWings
from quack import Quack


class MallardDuck(Duck):
    
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())
        
        
    def display(self):
        print(" I'm a pretty Mallard duck!")