from collections import deque 

my_deque = deque()

for data in [2,4,6,8,10]:
    my_deque.append(data)
    
for data in [3,5,7,9]:
    my_deque.appendleft(data)
    

print(f"Data stored in deque is {my_deque}")