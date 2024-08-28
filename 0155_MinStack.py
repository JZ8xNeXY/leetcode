class MinStack:

    def __init__(self):
        self.stack = []
        self.mini_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.mini_stack or val <= self.mini_stack[-1]:
            self.mini_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.mini_stack[-1]:
            self.mini_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini_stack[-1]


min_stack = MinStack()

# 操作の実行例
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())
min_stack.pop()
print(min_stack.top())
print(min_stack.getMin())
