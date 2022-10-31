# item = [1, 2, 3, 3, 3, 3, 4, 5, 9]
# print(item[0:-1])
# print(item[0:-2])


def maxSubArray(nums):
    store = nums
    max_val = nums[0]
    for index in range(len(nums)):

        adjuster = index + 1
        while adjuster <= len(nums):
            summation = sum(nums[index: adjuster])
            if max_val < summation:
                store = nums[index: adjuster]
                max_val = summation
            adjuster += 1

    return (store, max_val)


def texter(nums):
    accum = nums[0]
    maxi = accum
# skip = True
    datas = nums[1:]
    for data in datas:
        if((data + accum < data) & (data > maxi)):
            accum = data
            maxi = accum
        elif (accum + data > maxi):
            accum = accum + data
            maxi = accum
        elif (data > accum + data):
            accum = data
        else:
            accum += data

    return (maxi)


# def texter_recursive(nums):
#     if len(nums) == 0:
#         return 0
#     maxi = float('-inf')

#     result = nums[0] + texter_recursive(nums[1:])
#     return result

# print(texter(item))


# print(texter_recursive(item))
# item = [-1, -1, -2, -2]


# def slidingWindow(items):
#     maximum = items[0]
#     start = 0
#     stop = 0
#     operation_max = maximum
#     for index, data in enumerate(items):
#         if((index - 1) >= 0):
#             if ((data > (operation_max + data)) and data > operation_max):
#                 start = index
#                 stop = index
#                 maximum = data
#                 operation_max = data
#                 print('data is greater, ', data)
#             elif (maximum + data > operation_max):
#                 stop = index
#                 maximum += data
#                 operation_max = maximum
#             else:
#                 maximum += data
#     print(f'start: {start},  stop: {stop}')
#     return sum(items[start: stop+1])

item = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# item = [-2, 1, -3, 4]
# item = [3, -5, 1, 9, -2, 4]
# item = [8, -19, 5, -4, 20]
# item = [-1, -2]
# item = [5, 4, -1, 7, 8]
# item = [5, 4, -1]
# item = [-1, -1, -2, -2]
item = [5, 4, -1]
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
    return maximum


print(slidingWindow(item))
