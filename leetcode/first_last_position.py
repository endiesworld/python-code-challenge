class Solution:
    def searchRange(self, nums, target: int):
        if len(nums) < 1:
            return [-1, -1]
        elif len(nums) == 1:
            return [-1, -1] if nums[0] != target else [0, 0]

        store = []

        def search_val(nums, target):
            mid = len(nums) // 2

            if mid == 1:
                return 0 if nums[0] == target else 'No'
            elif nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return search_val(nums[:mid], target)
            else:
                try:
                    return mid + search_val(nums[mid:], target)
                except TypeError as e:
                    return -1

        ref_point = search_val(nums, target)

        if ref_point == -1:
            return [-1, -1]
        store.append(re)
        first_part = nums[:ref_point]
        second_part = nums[ref_point:]
        # pointer =
