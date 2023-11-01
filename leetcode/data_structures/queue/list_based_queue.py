from typing import List, Any

class Queue:
    def __init__(self, queue: List = []) -> None:
        self.queue = queue
        self.queue_len = len(self.queue)
        
    def enqueue(self, data) -> None:
        self.queue.append(data)
        self.queue_len += 1
        
    def dequeue(self) -> Any:
        if self.is_empty():
            return None
        
        data = self.queue[0]
        self.queue_len -= 1
        self.queue = self.queue[1:]
        return data
    
    def is_empty(self) -> bool:
        return self.queue_len == 0
    
    def size(self) -> int:
        return self.queue_len
    
    
queue = Queue()

for data in [5,10,50, 60, 80, 100]:
    queue.enqueue(data)
    
print(f"The current size of the queue is: {queue.size()}")

print(f"Dequeued form the queue is: {queue.dequeue()}")

print(f"The current size of the queue is: {queue.size()}")

print(f"Dequeued form the queue is: {queue.dequeue()}")

print(f"The current size of the queue is: {queue.size()}")