# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Input: nums = [3, 3, 7, 7, 10, 11, 11]
# Output: 10
# If array is sorted, and every element appears only twice accept one, it means:
# Every diferent element starts on an even position(i = even), and its pairs follows,
# eccept for the single element
from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def singleNonDuplicate(self, nums: List[int]) -> int:
        """ Returns the single element that appears only once 
            in a sorted array
        """
        even_index = 0
        single_element = nums[even_index]
        while even_index < len(nums)-1:
            if single_element != nums[even_index + 1]:
                break
            even_index += 2
            single_element = nums[even_index]
        return single_element


solution_instance = Solution()
print(solution_instance.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
