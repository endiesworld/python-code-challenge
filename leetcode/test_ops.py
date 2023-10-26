
def main(*args, **kwargs):
    my_list_1 = [3,6, "hello", "world"]
    my_tuple_1 = (1,3,5, "hello", "world")
    
    print(my_list_1[3][::-1])
    
    print("my_list_1 contains: ", end=" ")
    for data in my_list_1:
        print(f"{data},", end=" ")
        
    print("\nmy_tuple_1 contains: ", end=" ")
    for data in my_tuple_1:
        print(f"{data},", end=" ")
        

if __name__ == '__main__':
    main()