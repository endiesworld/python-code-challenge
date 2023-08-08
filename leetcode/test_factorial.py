
def normal_fact(x):
    fact = 1
    if x < 0:
        print(f"The factorial for {x} is: 0")
    else:
        for data in range(2, (x+1)):
            fact *= data
        print(f"The factorial for {x} is: {fact}")
        

normal_fact(24)