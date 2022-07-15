"""
    You are given an integer array height of length n. There are n vertical lines drawn such that the 
    two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
"""

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49


def maxArea(height):
    max_area = 0
    for index_1, num in enumerate(height):
        count = 1
        for data in height[index_1+1:]:
            l = num if num < data else data
            area = l * count
            max_area = area if area > max_area else max_area
            count += 1
    return max_area


def maxArea(height):
    a = height[0]
    b = height[1]
    l, ref = a, b if a < b else b, a
    breadth = 1
    max_area = l * breadth

    for index_1, num in enumerate(height[2:]):
        count = 1

    return max_area


print(maxArea(height))
