import sys


class Solution(object):
    def threeSum(self, arr):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr_len = len(arr)
        arr.sort()
        # Create a list to store unique lists
        unique_list = []
        seen = set()  # Set to keep track of seen sublists as tuples
        for index in range(arr_len):
            next_index = index + 1
            last_index = arr_len - 1
            if arr[index] > 0:
                break
            while next_index < last_index:
                sublist = [arr[index], arr[next_index], arr[last_index]]
                sublist_tuple = tuple(sublist)
                if (sublist_tuple not in seen) and (sum(sublist_tuple) == 0):
                    seen.add(sublist_tuple)
                    unique_list.append(sublist)
                    next_index += 1
                    last_index -= 1

                elif (sum(sublist_tuple) > 0):
                    if (arr[index] + arr[next_index]) > 0:
                        break
                    last_index -= 1
                else:
                    next_index += 1

        return unique_list

def main(arr, *args, **kwargs):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # Create a list to store unique lists
    unique_list = []
    seen = set()  # Set to keep track of seen sublists as tuples
    for index, data in enumerate(arr):
        for index_2, data_2 in enumerate(arr[index+1:]):
            for data_3 in arr[index+index_2+2:]:
                sublist = [data, data_2, data_3]

                # Sort the sublist elements
                sublist_sorted = sorted(sublist)
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