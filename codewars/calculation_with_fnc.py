"""
Deascription:
    This time we want to write calculations using functions and get the results. Let's have a look at some examples:
    seven(times(five())) # must return 35
    four(plus(nine())) # must return 13
    eight(minus(three())) # must return 5
    six(divided_by(two())) # must return 3
    
Requirements:
    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...: eight(divided_by(three()))
    
"""

def zero(arg=None): 
    if arg : 
        result = arg
        return eval(f"0{result}")
    return 0 #your code here

def one(arg=None):
    if arg : 
        result = arg
        return eval(f"1{result}")
    return 1 #your code here

def two(arg=None):
    if arg : 
        result = arg
        return eval(f"2{result}")
    return 2 #your code here

def three(arg=None):
    if arg : 
        result = arg
        return eval(f"3{result}")
    return 3 #your code here

def four(arg=None): 
    if arg : 
        result = arg 
        return eval(f"4{result}")
    return 4 #your code here

def five(arg=None):
    if arg : 
        result = arg 
        return eval(f"5{result}")
    return 5 #your code here

def six(arg=None): 
    if arg : 
        result = arg
        return eval(f"6{result}")
    return 6 #your code here

def seven(arg=None): 
    if arg : 
        result = arg
        return eval(f"7{result}")
    return 7 #your code here

def eight(arg=None): 
    if arg : 
        result = arg
        return eval(f"8{result}")
    return 8 #your code here

def nine(arg=None):
    if arg : 
        result = arg
        return eval(f"9{result}")
    return 9 #your code here

def plus(arg): 
    return " + {}".format(str(arg))

def minus(arg=None): 
    return " - {}".format(str(arg))

def times(arg=None):  
    return " * {}".format(str(arg))

def divided_by(arg=None):  
    return " // {}".format(str(arg))

def fixed_tests():
    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) == 5
    assert six(divided_by(two())) == 3

if __name__ == '__main__':    
    fixed_tests()