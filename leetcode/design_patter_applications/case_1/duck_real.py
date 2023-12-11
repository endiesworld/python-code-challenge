from duck_class import Duck
from fly_cannot import FlyNoWay
from quack import Quack


class ReallDuck(Duck):
    
    def __init__(self):
        super().__init__(FlyNoWay(), Quack())
        
        
    def display(self):
        print(" I'm a real duck!")