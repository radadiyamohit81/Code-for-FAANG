class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st1 = []
        self.minSt = [float('inf')]
        

    def push(self, x):
        self.st1.append(x)
        self.minSt.append(min(self.minSt[len(self.minSt)-1], x))

    def pop(self):
        self.minSt.pop()
        self.st1.pop()

    def top(self):
        if len(self.st1) == 0:
            return "Empty Stack"
        return self.st1[len(self.st1)-1]

    def getMin(self):
        return self.minSt[len(self.minSt)-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(9)
obj.push(4)
obj.pop()
print(obj.top())
print(obj.getMin())
obj.push(12)
obj.pop()
obj.push(3)
obj.pop()
obj.pop()
obj.pop()
print(obj.top())
print(obj.getMin())