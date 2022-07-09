
nums = [1, -1, -2, 4, -7, 3]
k = 2
nums = [10, -5, -2, 4, 0, 3]
k = 3
# nums = [1, -5, -20, 4, -1, 3, -6, -3]
# k = 2
# nums = [100, -1, -100, -1, 100]
# k = 2


def max_result(arr, k):
    arr_len = len(arr)
    max_sum = arr[0]
    jumper = k
    index = 1

    while index < arr_len:
        start = jumper
        print(f'index is: {index}')
        print(f'start is: {start}')
        if start < arr_len:
            print(f'slice array is: {arr[index: start]}')
            _max = arr[index: start]
        else:
            _max = arr[index:]
            print(f'slice array is: {arr[index: ]}')
        max_val = max(_max)
        max_sum += max_val
        index = index + _max.index(max_val) + 1
        jumper = k + index
    return max_sum


print(max_result(nums, k))
