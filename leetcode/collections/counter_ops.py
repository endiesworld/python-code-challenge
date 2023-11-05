from collections import Counter


def main():
    
    class_1 = ['a', 'b', 'c', 'd', 'e','a', 'b', 'c', 'd', 'e','b', 'c', 'd', 'c', 'd',]
    
    class_2 = ['f', 'g', 'h', 'i', 'j', 'k', 'g', 'h', 'i', 'j','f', 'g', 'h',]
    
    c1 = Counter(class_1)
    c2 = Counter(class_2)
    
    print(f" class_1 count: {c1}")
    print(f" class_1 count: {c2}")
    
    # Prints all key and value pairs as a list of tuples
    print(f"Most common key in c1: {c1.most_common()}")
    
    # Prints the key with the highest frequency
    print(f"Most common key in c1: {c1.most_common(1)}")

if __name__ == '__main__':
    main()