"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
from heapq import merge
from statistics import median


nums1 = [1, 3]
nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
nums1 = [1, 2]
nums2 = [3, 4]


def findMedianSortedArrays(nums1, nums2):
    merge = []
    counter = 0
    nums1.append('stop')
    nums2.append('stop')
    while (nums1[0] != 'stop') & (nums2[0] != 'stop'):
        if nums1[0] < nums2[0]:
            merge.append(nums1.pop(0))
        else:
            merge.append(nums2.pop(0))
        counter += 1

    while (nums1[0] != 'stop'):
        merge.append(nums1.pop(0))
        counter += 1
    while (nums2[0] != 'stop'):
        merge.append(nums2.pop(0))
        counter += 1

    is_merge_odd = counter % 2

    if is_merge_odd:
        center = counter // 2
        return float(merge[center])
    else:
        center = int(counter / 2)
        return float((merge[center - 1] + merge[center]) / 2)


def findMedianSortedArrays_(nums1, nums2):
    num1_first = nums1[0]
    num2_first = nums2[0]
    counter = -1
    added_element = None
    common = []
    while((added_element != num1_first) & (added_element != num2_first)):
        num1 = nums1.pop()
        num2 = nums2.pop()

        if(num1 > num2):
            nums2.append(num2)
            common.append(num1)
            counter -= 1
            added_element = num1
        else:
            nums1.append(num1)
            common.append(num2)
            counter -= 1
            added_element = num2

    if(added_element == num2_first):
        added_element = nums1.pop()
        while(added_element != num1_first):
            common.append(added_element)
            counter -= 1
            added_element = nums1.pop()
        common.append(added_element)
        counter -= 1

    else:
        added_element = nums2.pop()
        while(added_element != num2_first):

            common.append(added_element)
            counter -= 1
            added_element = nums2.pop()
        common.append(added_element)
        counter -= 1

    is_merge_odd = abs(counter) % 2
    print(common)
    if is_merge_odd:
        center = counter // 2
        return float(common[center])
    else:
        center = int(counter / 2)
        return float((common[center - 1] + common[center]) / 2)


# print(findMedianSortedArrays(nums1, nums2))
print(findMedianSortedArrays_(nums1, nums2))
