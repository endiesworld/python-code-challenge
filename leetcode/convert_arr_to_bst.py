"""
    Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

arr = [-10, -3, 0, 5, 9]


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def sortedArrayToBST(arr):

    if not arr:
        return None

    # find middle
    mid = (len(arr)) // 2
    print(f'mid point is {mid}')
    # make the middle element the root
    root = Node(arr[mid])
    print(f'node value is: {root.value}')

    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])
    # print(f'root.left value is {root.left}')
    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid+1:])
    # print(f'root.right value is {root.left}')

    return None


def preOrder(node):
    if not node:
        return
    preOrder(node.left)
    preOrder(node.right)
    print(node.value)


print(sortedArrayToBST(arr))
