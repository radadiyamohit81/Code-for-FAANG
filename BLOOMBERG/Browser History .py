
# 2 STACK SOLN

class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = []

    def visit(self, url):
        self.history.append(url)
        self.future = []

    def back(self, steps):
        while steps > 0 and len(self.history) > 1:
            self.future.append(self.history.pop())
            steps -= 1
        return self.history[-1]

    def forward(self, steps):
        while steps > 0 and self.future != []:
            self.history.append(self.future.pop())
            steps -= 1
        return self.history[-1]
        

# DLL SOLUTION:
class DLL:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.previous = None
        
class BrowserHistory:
    def __init__(self, homepage):
        self.root = DLL(homepage)

    def visit(self, url):            # After we visit a new page, the new page get added next to root page and no other pages exist after it
        node = DLL(url)
        node.previous = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps):
        while steps and self.root.previous:
            self.root = self.root.previous
            steps -= 1
        return self.root.val

    def forward(self, steps):
        while steps and self.root.next:
            self.root = self.root.next
            steps -= 1
        return self.root.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)