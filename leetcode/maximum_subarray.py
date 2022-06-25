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


item = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# item = [-2, 1, -3, 4]
# # # item = [1]
# item = [5, 4, -1, 7, 8]

x = [5, 4, 3, 7, 9]
y = [-1, 7, 8]
# print(maxSubArray(item))


def texter(nums):
    accum = nums[0]
    start = 0
    stop = 0
    maxi = accum
    skip = True

    for index, data in enumerate(nums[1:]):

        if (data > (accum + data)) & (data > maxi):
            print(f'data: {data}')
            start = index + 1
            accum = data
            maxi = data
            skip = True
            print(f'Accumulator is: {accum}')
        elif (maxi <= (maxi + data)) & (skip):
            print(f'Changed stop @ index {int(index) +1 }')
            print(f'Data is: {data}')
            # print(f'Accumulator is: {accum + data}')
            stop = index + 2
            # skip = True
        else:
            accum += data
            skip = False
    return (nums[start:stop], sum(nums[start:stop]))


print(texter(item))
