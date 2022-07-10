"""
    Write a function sum_possible that takes in an amount and a list of positive numbers. 
    The function should return a boolean indicating whether or not it is possible to create the 
    amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.
sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
sum_possible(15, [6, 2, 10, 19]) # -> False
sum_possible(13, [6, 2, 1]) # -> True
sum_possible(103, [6, 20, 1]) # -> True
test_07:
sum_possible(271, [10, 8, 265, 24]) # -> False
test_08:
sum_possible(2017, [4, 2, 10]) # -> False
test_09:
sum_possible(13, [3, 5]) # -> true
"""


def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})


def _sum_possible(amount, numbers, store={}):
    if amount == 0:
        return True
    if amount < 0:
        return False
    if amount in store:
        return store[amount]
    for data in numbers:
        result = _sum_possible(amount - data, numbers, store)
        if result:
            store[amount] = result
            return True
    store[amount] = False
    return store[amount]


print(sum_possible(271, [10, 8, 265, 24]))
