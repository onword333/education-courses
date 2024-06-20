"""
232. Implement Queue using Stacks
"""


class MyQueue:

    def __init__(self):
        self._stack = []     

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:        
        return self._stack.pop(0)

    def peek(self) -> int:
        return self._stack[0]

    def empty(self) -> bool:
        return not self._stack


# Your MyQueue object will be instantiated and called as such:

obj = MyQueue()
obj.push(3)
obj.push(2)
obj.push(4)

param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)