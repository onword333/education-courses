"""
219. Contains Duplicate II
"""


class MyStack:

    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def empty(self) -> bool:
        return len(self._stack) == 0


myStack = MyStack()
myStack.push(1)
myStack.push(2)

print(myStack.top())
print(myStack.pop())
print(myStack.empty())
