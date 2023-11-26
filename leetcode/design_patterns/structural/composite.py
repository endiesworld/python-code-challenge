class Component(object):
    """Abstract class"""
    
    def __init__(self, *args, **kwards):
        pass
    
    def component_function(self):
        pass
    
class Child(Component):
    """ Concrete class, Inherit from abstract class 'Component' """
    
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        
        
    def component_function(self):
        # Prints the name of the child item here
        print("{}".format(self.name))
        
class Composite(Component):
    """Concrete class, and maintains the tree recursive structure"""
    
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        
        self.children = []
        
    def append_child(self, child):
        """Method for adding a child item to the tree"""
        self.children.append(child)
        
    def remove_child(self, child):
        """Method for removing a child item to the tree"""
        self.children.remove(child)
        
    def component_function(self):
        print("{}".format(self.name))
        
        for i in self.children:
            i.component_function()

# Build a composite submenu 1
sub1 = Composite("submenu1")

# Create a new child sub_submenu 11
sub11 = Child("sub_submenu 11")

sub12 = Child("sub_submenu 12")

# Add the sub-submenu 11 to submenu 1
sub1.append_child(sub11)

# Add the sub-submenu 12 to submenu 1
sub1.append_child(sub12)

sub1.component_function()