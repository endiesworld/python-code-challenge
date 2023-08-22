from typing import List
import sys
import math

def binary_search(nums, target, start=0, stop=None):
    start = start
    stop = stop if stop else len(nums)
    
    if start == stop:
        return start if nums[start] == target else -1
    
    while(start < stop ):
        mid = math.ceil((start + stop) / 2)
        print(f"stop: {stop}, mid: {mid}, start: {start}")
        if nums[mid] == target:
            # return mid
            print(f" target found at {mid}")
            break
        elif (nums[mid] > target):
            stop = mid - 1
        else:
            start = mid + 1
    # return -1
    print("end of search")
        
    
    
def main(nums:List, target: int):
    start = 0 
    tot_len = len(nums)
    stop = tot_len // 2
    
    #pivot area
    while(nums[start] < nums[stop]):
        start = stop
        stop = (start + tot_len) // 2
    
    print(f" Array entered is: {nums}, and target is: {target}")
    print(f" pivot area is: {start}, and stop: {stop}")
    

if __name__ == "__main__":
    nums = sys.argv[1]
    target = int(sys.argv[2])
    
    nums = [int(data) for data in nums if data.isdigit()]
    main(nums, target)
    binary_search(nums, target)
     