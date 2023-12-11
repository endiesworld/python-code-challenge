# from duck_class import Duck
# from cannot_fly import FlyNoWay
# from fly_with_wing import FlyWithWings
# from quack import Quack
# from quack_mute import MuteQuack
# from quack_squeak_type import Squeak

from mallard_duck import MallardDuck


def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()
    
if __name__ == '__main__':
    main()