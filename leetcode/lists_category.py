import sys


def test_equality(list_a, list_b, lenght):
    count = 0
    for data in list_a:
        if data in list_b:
            count += 1
    return True if count == lenght else False


def test_a_sublist_b(list_a, list_b, lenght):
    count = 0
    for data in list_a:
        if data in list_b:
            count += 1
    return True if count == lenght else False


def test_a_superlist_b(list_a, list_b, lenght):
    count = 0
    for data in list_b:
        if data in list_a:
            count += 1
    return True if count == lenght else False
    
    
def test_categories(list_a: list, list_b: list):
    len_a = len(list_a)
    len_b = len(list_b)
    
    if len_a == len_b:
        return "Two lists are equal" if  test_equality(list_a, list_b, len_a) else "Two lists are unequal"
    elif len_b > len_a:
        return "List 1 is sublist of list 2" if test_a_sublist_b(list_a, list_b, len_a) else "Two lists are unequal"
    else:
        return "List 1 is superlist of list 2" if test_a_superlist_b(list_a, list_b, len_b) else "Two lists are unequal"
    
def main():
    if len(sys.argv) != 3:
        print("Usage: enter two arguments after the file name")
        sys.exit(1)
        
    arg_1 = sys.argv[1]
    arg_1 = [int(data) for data in arg_1 if data.isdigit()]
    arg_2 = sys.argv[2]
    arg_2 = [int(data) for data in arg_2 if data.isdigit()]
    
    print(f"The value entered of arg_1 is {arg_1}: and the data type is {type(arg_1)}")
    print(f"The value entered of arg_1 is {arg_2}: and the data type is {type(arg_2)}")
    
    print(test_categories(arg_1, arg_2))
    
    

if __name__ == "__main__":
    main()