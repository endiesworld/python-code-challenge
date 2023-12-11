# from duck_class import Duck
# from cannot_fly import FlyNoWay
# from fly_with_wing import FlyWithWings
# from quack import Quack
# from quack_mute import MuteQuack
# from quack_squeak_type import Squeak

from duck_mallard import MallardDuck
from duck_real import ReallDuck
from fly_rocket_powered import FlyRocketPowered

def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()
    print()
    print("***** Real Duck ****")
    print()
    reall = ReallDuck()
    reall.display()
    reall.performFly()
    reall.performQuack()
    reall.set_fly_behavior(FlyRocketPowered() )
    
    print("Dynamically changed fly_behavior for reall duck: ")
    reall.performFly()
    
if __name__ == '__main__':
    main()