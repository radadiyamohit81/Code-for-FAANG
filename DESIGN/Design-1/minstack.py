# Implement a Stack with O(1) : push, pop, top, getMin operations

class MinStack1:
    # using 2 Stacks, O(2N) space
    def __init__(self):
        self.st = []
        self.minSt = [float('inf')]

    def push(self, x):
        self.st.append(x)
        self.minSt.append(min(self.minSt[-1], x))

    def pop(self):
        self.st.pop()
        self.minSt.pop()

    def top(self):
        return self.st[-1]
    
    def getMin(self):
        return self.minSt[-1]

class MinStack2:
    # using 1 stack, 1 variable 
    def __init__(self):
        self.st = []
        self.minVar = float('inf')

    def push(self, x):
        self.st.append(x)
        if x <= self.minVar:
            self.minVar = x                
            self.st.append(self.minVar)
    
    def pop(self):
        poppedVal = self.st.pop()
        if poppedVal == self.minVal:
            self.minVal = self.st.pop()
    
    def top(self):
        return self.st[-1]

    def getMin(self):
        return self.minVar



