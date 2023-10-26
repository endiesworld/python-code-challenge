from typing import List
import sys
import math


def binary_search(nums, terget, start_index = 0, stop_index= 1):
    start_index = start_index
    stop_index = stop_index
    while (start_index < stop_index ):
        mid =  math.ceil((start_index + stop_index) / 2)
        print(
            f"start index: {start_index},  mid index: {mid}, stop index: {stop_index}")
        if nums[mid] == terget:
            return mid
        elif nums[mid] > terget:
            stop_index = mid
        else:
            start_index = mid
    return -1

def linear_search(nums, terget, start_index=0, stop_index=1):
    while(start_index <= stop_index):
        if nums[start_index] == terget :
            return start_index
        start_index += 1
    return -1

def main(nums: List[int], terget: int):
    
    start = 0 
    tot_len = len(nums) 
    stop = tot_len // 2
    
    while( start < stop): 
        
        if (nums[start]  > nums[stop]):
            result = linear_search(nums, terget, start, stop)
            if result == -1:
                stop = start
                start = (stop + tot_len) // 2
            else:
                return result
            print(
                f"start index: {start}, stop index: {stop}")
        elif ((nums[start] > target) and (nums[stop] > target) or (nums[start] < target) and (nums[stop] < target)):
            print(
                f"start index: {start}, stop index: {stop}")
            start = stop
            stop = math.ceil((start + tot_len) / 2 )
            print(
                f"updated start index: {start}, stop index: {stop}")
            
            
        else:
            print(
                f"start index: {start}, stop index: {stop}")
            result = binary_search(nums, terget, start, stop)
            return result
    return -1
            
    
    
    # print(binary_search(nums, terget))
    
    # start = 0
    # tot_len = len(nums)
    # stop = tot_len // 2
    # print(f"stop index at index is given: {stop}, at point {nums[stop]}")

    # def search_pivot(start):
    #     while( nums[start + 1] > nums[start]):
    #         start += 1
    #     return start
    
    # while(start < stop):
    #     result = None
    #     pivot = None
    #     if nums[start] < nums[stop]:
    #         result = binary_search(start, stop)
    #         if result != -1:
    #             print(f"target found at index is given: {result}")
    #             break
    #     else:
    #         pivot = search_pivot(start)
    #         print(f"Pivot is given: {pivot}")
        
    #     if pivot:
    #         stop = pivot
    #     else:
    #         start = stop
    #         stop = (start + tot_len) // 2
            
            


if __name__ == '__main__':
    
    arr = sys.argv[1]
    target = int(sys.argv[2])
    
    nums = [int(data) for data in arr if data.isdigit()]
    
    print(f"array entered is: {nums}, and the target is {target}")
    
    # nums = [2, 3, 4, 5,6, 7, 8, 9 ]
    # target = 9
    
    print(main(nums, target))
    