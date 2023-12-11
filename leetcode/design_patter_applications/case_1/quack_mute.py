from interface_quack import QuackBehaviour

class MuteQuack(QuackBehaviour):
    def quack(self):
        print("Mute Quack: <<--silence-->>")