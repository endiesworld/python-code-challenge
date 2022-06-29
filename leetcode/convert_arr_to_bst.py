"""
    Given an integer numsay nums where the elements nums sorted in ascending order, convert it to a height-balanced binnums senumsh tree.

A height-balanced binnums tree is a binnums tree in which the depth of the two subtrees of every node never differs by more than one.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] nums both height-balanced BSTs.
"""

nums = [-10, -3, 0, 5, 9]
# nums = [1, 3]


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def sorted_numsayToBST(nums):

    if not nums:
        return None

    # find middle
    mid = (len(nums)) // 2
    print(f'mid point is {mid}')
    # make the middle element the root
    root = Node(nums[mid])
    print(f'node value is: {root.value}')

    # left subtree of root has all
    # values <nums[mid]
    root.left = sortednumsayToBST(nums[:mid])
    # print(f'root.left value is {root.left}')
    # right subtree of root has all
    # values >nums[mid]
    root.right = sortednumsayToBST(nums[mid+1:])
    # print(f'root.right value is {root.left}')

    return None


# def preOrder(node):
#     if not node:
#         return
#     preOrder(node.left)
#     preOrder(node.right)
#     print(node.value)


def sortednumsayToBST(nums):
    mid = len(nums) // 2
    L_side = nums[:mid]
    R_side = nums[mid+1:]
    new_numsay = [Node(nums[mid]).value]
    l_len = len(L_side)
    r_len = len(R_side)
    l_count = 0
    r_count = 0
    normal_count = 1
    while (l_len > l_count) | (r_len > r_count):
        if(l_len > l_count):
            new_numsay.append(L_side.pop())
            l_count += 1
        if(r_len > r_count):
            if (normal_count % 2 > 0):
                new_numsay.append(R_side.pop())
                r_count += 1
            else:
                new_numsay.append('null')
        normal_count += 1
    return new_numsay


print(sortednumsayToBST(nums))
