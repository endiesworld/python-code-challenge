class Borg:
    _shared_data = {} # Class variable _shared_data is an empty dictionary that will be shared among all instances of the class.
    def __init__(self):
        self.__dict__ = self._shared_data
        #The __dict__ attribute is used to store the instance's attributes. By setting it to _shared_data, every instance of Pet will share the same dictionary, effectively making them share the same set of attributes.
        
class Singleton(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self) #This is used to initialize instances of the Borg class, and it's often seen when a derived class wants to invoke the constructor of its parent class explicitly.
        self._shared_data.update(kwargs)
        
    def __str__(self) -> str:
        return str(self._shared_data)
    
    
x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(f" Creating an x Singleton instance gives x as  {x}")

y = Singleton(SNMP="Simple Network Management Protocol")
print(f" Creating a y Singleton instance gives y as  {y}")
print(f" Creating a y Singleton instance gives x as  {x}")