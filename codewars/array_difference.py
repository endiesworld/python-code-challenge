def array_diff(arr1, arr2):
    if len(arr2) == 0 or len(arr1) == 0:
        return arr1
    arr_2_dict = {key: key for key in arr2}
    result = [x for x in arr1 if x not in arr_2_dict]
    return result


if __name__ == '__main__':
    print(array_diff([1,2], [1]))
    print(array_diff([1,2,2], [1]))
    print(array_diff([1,2,2], [2]))
    print(array_diff([1,2,2], []))
    print(array_diff([], [1,2]))
    print(array_diff([1,2,3], [1, 2]))