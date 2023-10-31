from typing import List

class Stack:
    def __init__(self, stack: List = []):
        self.stack = stack
        self.stack_len = len(stack)
        
    def push(self, value):
        self.stack.append(value)
        self.stack_len += 1
        
    def pop(self):
        if self.stack_len > 0:
            return self.stack.pop()
        return None
        
    def peek(self):
        if self.stack_len > 0:
            return self.stack[-1]
        return None
    
    def __str__(self) -> str:
        return str(self.stack)


my_stack = Stack([20,14,20])

my_stack.push(10)

print(f"current stack value: {my_stack}")