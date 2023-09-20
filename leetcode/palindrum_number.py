import sys

def main(nums, *args, **kwargs):
    print(f"Numbers enterred are: {nums}")
    tot_len = len(nums)
    start = 0
    stop = -1
    counter = tot_len // 2
    
    while(start < counter):
        if (nums[start] == nums[stop]):
            start += 1
            stop -= 1
        else:
            break
    return True if start == counter else False
        
        
    

if __name__ == '__main__':
    nums = sys.argv[1]
    print(f"Numbers enterred are: {nums}")
    nums = [int(x) for x in nums if x.isdigit()]
    print(f"Numbers enterred are: {nums}")
    print(main(nums))