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
item = [-2, 1, -3, 4]
item = [3, -5, 1, 9, -2, 4]
item = [8, -19, 5, -4, 20]
# item = [-1, -2]
# item = [5, 4, -1, 7, 8]
item = [5, 4, -1]


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

print(texter(item))


# print(texter_recursive(item))
