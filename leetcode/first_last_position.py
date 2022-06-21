class Solution:
    def __init__(self) -> None:
        pass

    def searchRange(self, nums, target):
        if len(nums) < 1:
            return [-1, -1]
        elif len(nums) == 1:
            return [-1, -1] if nums[0] != target else [0, 0]

        store = []

        def search_val(nums, target):
            mid = len(nums) // 2

            if len(nums) == 1:
                return 0 if nums[0] == target else 'No'
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return search_val(nums[:mid], target)
            else:
                try:
                    return (mid + search_val(nums[mid:], target))
                except TypeError as e:
                    return 'No'

        ref_point = search_val(nums, target)
        if (ref_point == -1) | (ref_point == 'No'):
            return [-1, -1]
        store.append(ref_point)
        first_part = nums[:ref_point]
        second_part = nums[(ref_point+1):]

        for index, data in enumerate(first_part):
            real_index = -1*index - 1
            if first_part[real_index] == target:
                store.append(ref_point + real_index)
            else:
                break
        for index, data in enumerate(second_part):
            if data == target:
                store.append(ref_point + index + 1)
            else:
                break

        store = sorted(store)

        result = [store[0], store[-1]]

        return result


solution = Solution()

# print(solution.searchRange([1, 3], 1))
# print(solution.searchRange([1, 4], 4))
# print(solution.searchRange([-3, -2, -1], 0))
# print(solution.searchRange([-3, -2, -2], -4))
# print(solution.searchRange([2, 2], 3))
# print(solution.searchRange([1, 2, 3], 3))
print(solution.searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3))
