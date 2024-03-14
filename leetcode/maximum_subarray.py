# item = [1, 2, 3, 3, 3, 3, 4, 5, 9]
# print(item[0:-1])
# print(item[0:-2])


def max_subarray_sum(arr):

    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum



item = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# item = [-2, 1, -3, 4]
# item = [3, -5, 1, 9, -2, 4]
# item = [8, -19, 5, -4, 20]
# item = [-1, -2]
# item = [5, 4, -1, 7, 8]
# item = [5, 4, -1]
# item = [-1, -1, -2, -2]
# item = [5, 4, -1]
# item = [-1, -1, -2, -2]
# item = [8, -19, 5, -4, 20]
# item = [-2, 1]
# item = [-2, -1]


def slidingWindow(nums):
    maximum = nums[0]
    start = 0
    stop = 0
    running_sum = maximum
    for index, data in enumerate(nums):
        if((index - 1) >= 0):
            if((data > (running_sum + data)) and (data > running_sum)):
                maximum = data
                running_sum = maximum
                start = index
                stop = index
            elif(running_sum + data > maximum):
                stop = index
                maximum = running_sum + data
                running_sum = maximum
            elif(running_sum + data < 0):
                running_sum = 0
                start = index + 1
            else:
                running_sum += data
    start = min(stop, start)
    print('Array sum: ', sum(nums[start: stop + 1]))
    print(f'start: {start},  stop: {stop}')
    print("sub array is: ", nums[start: stop + 1])
    return maximum


print(slidingWindow(item))
