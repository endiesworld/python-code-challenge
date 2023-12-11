from abc import ABC, abstractmethod
from interface_fly import FlyBehaviour
from interface_quack import QuackBehaviour

class Duck(ABC):
    def __init__(self, fly_bahavior:FlyBehaviour, quack_behavior:QuackBehaviour):
        super().__init__()
        self.fly_behavior = fly_bahavior
        self.quack_behavior = quack_behavior
        
    @abstractmethod
    def display(self):
        ...
        
    def set_fly_behavior(self, fly_behavior:FlyBehaviour):
        self.fly_behavior = fly_behavior
        
    def set_quack_behavior(self, quack_behavior:QuackBehaviour):
        self.quack_behavior = quack_behavior
        
    def performFly(self):
        self.fly_behavior.fly()
        
    def performQuack(self):
        self.quack_behavior.quack()
        
    def swim(self):
        print("All ducks flaot, even decoys!")