class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, num : int):
        self.stack.append(num)
        if self.minStack:
            self.minStack.append(min(num, self.minStack[-1]))
        else:
            self.minStack.append(num)
    
    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]


