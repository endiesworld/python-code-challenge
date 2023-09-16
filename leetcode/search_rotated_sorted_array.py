from typing import List
import sys
import math

def binary_search(nums, target, start=0, stop=None):
    start = start
    stop = stop if stop else len(nums) - 1
    
    if start == stop:
        return start if nums[start] == target else -1
    
    while(start <= stop ):
        mid = (start + stop) // 2
        print(f"stop: {stop}, mid: {mid}, start: {start}")
        if nums[mid] == target:
            return mid
            # print(f" target found at {mid}")
            # break
        elif (nums[mid] > target):
            stop = mid -1
        else:
            start = mid + 1
    return -1
    # print("end of search")
        
def linear_search(nums, target, start=0, stop=None):
    while(start <= stop):
        print(f"linear search stop: {stop}, start: {start}")
        if nums[start] == target:
            return (start, start, stop)
        start += 1
    return (-1, start, stop)
    
def main(nums:List, target: int):
    start = 0 
    tot_len = len(nums)
    stop = tot_len // 2
    if start == stop:
        return -1 if nums[start] != target else start 
    #No pivot area area found
    while(nums[start] < nums[stop]):
        result = binary_search(nums, target, start, stop)
        if result != -1:
            return result
        start = stop
        stop = (start + tot_len) // 2
        
    if start != stop:
        #Linear search on pivot area
        (result, start, stop) = linear_search(nums, target, start, stop)
        
        if (result == -1 ) and (stop < tot_len):
            return binary_search(nums, target, start, tot_len - 1)
        return result
    return -1
    
    

if __name__ == "__main__":
    nums = sys.argv[1]
    target = int(sys.argv[2])
    
    nums = [int(data) for data in nums if data.isdigit()]
    print(main(nums, target))
    # binary_search(nums, target)
     