class MinStack:
    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val : int):
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
    
    def pop(self):
        self.minStack.pop()
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]


