class Subject(object):
    
    def __init__(self):
        self._observers = []
        
    def attach(self, observer):
        # If the observer is not already in the observers list, append to the list
        if observer not in self._observers:
            self._observers.append(observer)
        
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except KeyError:
            pass
        
    def notify(self, modifer=None):
        # Sends notification to all observers in the list
        for observer in self._observers:
            if modifer != observer:
                observer.update(self)
                

class Core(Subject):
    
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0
        
    @property #Getter that gets the core temperature
    def temp(self):
        return self._temp
    
    @temp.setter #Setter that gets the core temperature
    def temp(self, temp):
        self._temp = temp
        self.notify()
        

class TempViewer:
    
    def update(self, subject): #Alert method that is invoked when the temperature value changes.
        print("Temperature Viewer updated: {} has Temperature {}".format(subject._name, subject.temp))
        

# Creat subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

#Create Observer
v1 = TempViewer()
v2 = TempViewer()

#Attach observers to the first Core
c1.attach(v1)
c1.attach(v2)

#Change the temperature of the first core
c1.temp = 80
c1.temp = 90