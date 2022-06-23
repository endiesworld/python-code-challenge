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
item = [1]
item = [5, 4, -1, 7, 8]
print(maxSubArray(item))
