class queueUsingStack:
    def __init__(self):
        self.inqueue = []
        self.outqueue = []
    def push(self, x):
        self.inqueue.append(x)
    def pop(self):
        if self.outqueue != []:
            return self.outqueue.pop()
        while self.inqueue != []:
            self.outqueue.append(self.inqueue.pop())
        return self.outqueue.pop() if self.outqueue != [] else -1
            
    def peek(self):
        if self.outqueue != []:
            return self.outqueue[-1]
        while self.inqueue != []:
            self.outqueue.append(self.inqueue.pop())
        return self.outqueue[-1]
    def empty(self):
        return self.inqueue==[] and self.outqueue==[]

    