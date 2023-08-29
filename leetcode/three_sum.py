import sys

def main(arr, *args, **kwargs):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    store = {}
    for index, data in enumerate(arr):
        for index_2, data_2 in enumerate(arr[index+1:]):
            for data_3 in arr[index+index_2+2:]:
                key = "value_{}_{}_{}".format(data, data_2, data_3)
                store[key] = [data, data_2, data_3]

    list_of_repeated_lists = store.values()

    # Create a list to store unique lists
    unique_list = []
    seen = set()  # Set to keep track of seen sublists as tuples

    for sublist in list_of_repeated_lists:
        sublist_sorted = sorted(sublist)  # Sort the sublist elements
        sublist_tuple = tuple(sublist_sorted)
        if (sublist_tuple not in seen) and (sum(sublist_tuple) == 0):
            seen.add(sublist_tuple)
            unique_list.append(sublist_sorted)

    return unique_list
    

if __name__ == '__main__':
    arr = sys.argv[1]
    
    arr = [int(data) for data in arr if data.isdigit()]
    
    print(f"Array entered is given as {arr}")
    
    main(arr)