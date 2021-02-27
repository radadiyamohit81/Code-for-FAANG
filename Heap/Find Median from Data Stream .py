# OPTIMIZED: 2HEAPS SOLUTION,
# O[5 logN] Time,   (max of 3 Heap Insertions+ 2 Heap Deletions)

class MedianFinder:
    import heapq

    def __init__(self):
        self.lo = []        # MAX HEAP
        self.hi = []        # MIN HEAP
        
    def addNum(self, num):
        if len(self.lo) == 0:
            heapq.heappush(self.lo, -num)
            return
        
        # ADD THE num TO THE APPROPRIATE HEAP
        if num < -self.lo[0]:
            heapq.heappush(self.lo, -num)
        else:
            heapq.heappush(self.hi, num)
            
        # BALANCING THE SIZE OF BOTH THE HEAPS TO BE EQUAL OR DIFFERENCE OF 1 
        if len(self.lo) - len(self.hi) == 2:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.lo) - len(self.hi) == -2:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0])/2
        elif len(self.lo) > len(self.hi):
            return -float(self.lo[0])
        elif len(self.hi) > len(self.lo):
            return float(self.hi[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()