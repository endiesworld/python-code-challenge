from collections import defaultdict

def main():
    
    fruits = ['apple', 'orange', 'mango', 'banana', 'banana', 'orange', 'orange', 'apple'] 
    
    fruitCounter = {}
    
    # Adds a default value of zero to any valid key value
    fruitCounter_2 = defaultdict(int)
    
    # Adds a default value of 100 using a lambda expression to any valid key value
    fruitCounter_3 = defaultdict(lambda : 100)
    
    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1
            
    for (key, value) in fruitCounter.items():
        print(f" {key} = {value}")
    
    # Using defaultdict
    for fruit in fruits:
        fruitCounter_2[fruit] += 1

    for (key, value) in fruitCounter.items():
        print(f" {key} = {value}")
        
    print("--------------------------------")
    print("           fruitCounter_2       ")
    print("--------------------------------")
    for (key, value) in fruitCounter_2.items():
        print(f" {key} = {value}")
        
    
    print("--------------------------------")
    print(" Checking any random value")
    print("--------------------------------")
    print(f"pear = {fruitCounter_2['pear']}")
    print(f"Emmanuel = {fruitCounter_2['Emmanuel']}")
    
    print("--------------------------------")
    print("     fruitCounter_3 with no key insered       ")
    print("--------------------------------")
    for (key, value) in fruitCounter_3.items():
        print(f" {key} = {value}")
    
if __name__ == "__main__":
    main()