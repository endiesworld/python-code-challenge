import sys
from typing import List


def binary_search(arr:List, target:int)->int:
    start = 0
    tot_len = len(arr)
    stop = tot_len -1
    
    while(start <= stop):
        mid = (start + stop) // 2
        if arr[mid] == target:
            return True
        elif (arr[mid] > target):
            stop = mid - 1
        else:
            start = mid +1
    return False

# First approach
def main_1(matrix, target):
    for arr in matrix:
        if arr[0] == target:
            return True
        elif arr[-1] == target:
            return True
        elif (arr[0] < target) and (arr[-1] > target):
            return binary_search(arr, target)
        
# Second approach
def main_2(matrix, target):
    start = 0
    tot_len = len(matrix)
    stop = tot_len - 1
    while(start <= stop):
        mid = (start + stop) // 2
        if (matrix[mid][0] == target):
            return True
        elif(matrix[mid][-1] == target):
            return True
        elif (matrix[mid][0] < target and matrix[mid][-1] > target):
            return binary_search(matrix[mid], target)
        elif (matrix[mid][0] > target):
            stop = mid - 1
        else:
            start = mid + 1
    return False


if __name__ == '__main__':
    if len(sys.argv) < 1:
        matrix = sys.argv[1]
        target = int(sys.argv[2])
        matrix = [int(x) for x in matrix if x.isdigit()]
        
        print(f"matrix enterred {matrix}")
        print(f"target enterred {target}")
    else:
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
    print(f"Result from first approach: {main_1(matrix, target)}")
    print(f"Result from first approach: {main_2(matrix, target)}")
