class RandomizedSet:
    import random
    def __init__(self):
        self.nums = []
        self.position = {}

    def insert(self, val):
        if val not in self.position:
            self.nums.append(val)
            self.position[val] = len(self.nums)-1
            return True
        return False
        
    def remove(self, val):
        if val in self.position:
            index = self.position[val]
            lastValue = self.nums[-1]
            self.nums[index] = lastValue
            self.position[lastValue] = index
            self.nums.pop()
            del self.position[val]
            
            return True
        return False

    def getRandom(self): 
        return self.nums[ random.randint(0, len(self.nums)-1) ]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()