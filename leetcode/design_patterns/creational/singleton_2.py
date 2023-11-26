from typing import Any


class Singleton(type):
    _instance = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
    
    
class Logger(metaclass=Singleton):
    def log(self, message):
        print(message)
        
        
logger = Logger()
logger2 = Logger()
logger.log("Hello, world!")
logger2.log("Hello, Emmanuel!")

print(id(logger))
print(id(logger2))