from functools import wraps

def make_blink(function):
    """Defines the decorator"""
    
    # This makes the decorator transparent in terms of its name and description
    @wraps(function)
    
    # Define the inner function
    def decorator():
        # Grab the return value of the function
        return_val = function()
        
        return '<blink> {} </blink>'.format(return_val)
    
    return decorator

def hello_world():
    """Original function"""
    return "Hello World!"

# Define a decorated function
@make_blink
def decorated_hello_world():
    """Original function"""
    return "Hello World!"

# Check result of hello_world function without decorator
print(hello_world())

# Check result of hello_world function with decorator
print(decorated_hello_world())