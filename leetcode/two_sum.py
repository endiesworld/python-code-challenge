"""
    Given an array of integers nums and an integer target, return indices of the two numbers such 
    that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    
    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
"""


from tkinter import N


nums = [2, 7, 11, 15]
target = 9
# nums = [3, 2, 4]
# target = 6


def two_sum(nums, target):
    for index_1, num in enumerate(nums):
        for index_2, data in enumerate(nums[(index_1+1):]):
            if (num + data) == target:
                return [index_1, (index_1 + index_2 + 1)]
    return None


# def two_sum(list, target, index_store):
#     if (list[index_store[0]] + list[index_store[1]] ) == target:
#         return index_store
#     if index_store[1] >= len(list):
#         return False
#     first = 0
#     for index, data in enumerate()


# def two_sum(nums, target):
#     if (len(nums) == 0):
#         return target == 0
#     else:
#         element = nums[0]
#         rest = nums[1:]
#         return two_sum(rest, target) | two_sum(rest, target - element)


# def two_sum(nums, target):
#     return _two_sum(nums, target, [], len(nums)-1)


# def _two_sum(nums, target, index_store, caller_number):
#     if (len(nums) == 0):
#         return 0
#     element_index = caller_number
#     element = nums.pop()
#     _two_sum(nums, target, index_store, caller_number - 1)
#     print(f'Element is : {element}, index is: {element_index}')

# return None


def recus_mestry(n):
    if n < 10:
        return n
    a = n // 10
    b = n % 10
    return recus_mestry(a+b)


# print(recus_mestry(648))

# print(two_sum(nums, target))
# print((648 % 10))
# print((1 // 2))


def permutation(string):
    str_len = len(string)
    return _permutation(string, 0, str_len-1)


def _permutation(string, pointer, str_len):
    if pointer == str_len:
        return [string[pointer]]

    result = [string[pointer], _permutation(string, pointer + 1, str_len)]
    return result


print(permutation('hello'))
