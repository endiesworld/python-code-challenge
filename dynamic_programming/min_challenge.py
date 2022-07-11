"""
    Write a function min_change that takes in an amount and a list of coins. 
    The function should return the minimum number of coins required to create the amount. 
    You may use each coin as many times as necessary.

    If it is not possible to create the amount, then return -1.

    test_00:
    min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
    test_01:
    min_change(13, [1, 9, 5, 14, 30]) # -> 5
    test_02:
    min_change(23, [2, 5, 7]) # -> 4
    test_03:
    min_change(102, [1, 5, 10, 25]) # -> 6
    test_04:
    min_change(200, [1, 5, 10, 25]) # -> 8
    test_05:
    min_change(2017, [4, 2, 10]) # -> -1
    test_06:
    min_change(271, [10, 8, 265, 24]) # -> -1
    test_07:
    min_change(0, [4, 2, 10]) # -> 0
    test_08:
    min_change(0, []) # -> 0
"""


def min_change(amount, nums):
    ans = _min_change(amount, nums, {})
    if ans == float('inf'):
        return -1
    return ans


def _min_change(amount, nums, memo):
    if amount == 0:
        return 0

    if amount < 0:
        return float('inf')

    if amount in memo:
        return memo[amount]

    max_coin = float('inf')
    for data in nums:
        result = 1 + _min_change(amount - data, nums, memo)
        if result < max_coin:
            max_coin = result

    memo[amount] = max_coin

    return max_coin


print(min_change(8, [1, 5, 4, 12]))
print(min_change(13, [1, 9, 5, 14, 30]))
print(min_change(271, [10, 8, 265, 24]))
print(min_change(2017, [4, 2, 10]))
print(min_change(0, []))
