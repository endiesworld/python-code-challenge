from enum import Enum

#  You can prevent dublicate value by using the "@unique" 
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    
    

def main():
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.BANANA))
    
    # Enums have both name and value
    print(f"The name of this enum: {Fruit.APPLE.name}, and value is : {Fruit.APPLE.value}")
    

if __name__ == '__main__':
    main()