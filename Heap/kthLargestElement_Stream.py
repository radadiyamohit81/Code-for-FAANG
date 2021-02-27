class KthLargest:
    # O[N log K] Time
    # O[K] Space

    import heapq
    def __init__(self, nums, k):
        self.k = k
        self.nums = nums

        # MAINTAIN A MIN-HEAP of size K, Kth largest element is at top at all times
        heapq.heapify(self.nums) 
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
        return self.nums[0]
  
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)