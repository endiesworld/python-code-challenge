
def binary_search(nums, target):
    stop = len(nums) - 1
    return _binary_search(nums, target, 0, stop)


def _binary_search(nums, target, start, stop):
    if (start > stop):
        return None

    mid = (start + stop) // 2

    if (nums[mid] == target):
        return mid
    elif (nums[mid] > target):
        stop = mid - 1
        return _binary_search(nums, target, start, stop)

    start = mid + 1
    return _binary_search(nums, target, start, stop)


print(binary_search([1, 4, 6, 8, 9, 20, 25, 30, 37], 0))
