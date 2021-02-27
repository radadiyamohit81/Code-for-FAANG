# APPROACH 1: MIN HEAP (OPTIMAL)

# Time Complexity : O(n lg k), n: len(nums), k: size of heap - lg k for heapify op
# Space Complexity : O(k), size of min heap

class Solution:
    import heapq
    def findKthLargest(self, nums, k):
        # MIN HEAP
        q = []
        size = 0
        for num in nums:
            if size == k:
                heapq.heappush(q, num)
                heapq.heappop(q)
            else:
                heapq.heappush(q, num)
                size += 1
        return heapq.heappop(q)    


# APPROACH 2: MAX HEAP

# Time Complexity : O(n lg (n - k)), n: len(nums), k: size of heap - lg n - k for heapify op
# Space Complexity : O(k), size of min heap

# To use max heap in python, negate all the elements then call heapq as heapq by default only implements min heap.
# 1. Use max heap of size n - k + 1 and store only the n - k + 1 smallest elements in max heap
# 2. Return the popped element from the maxHeap after adding all the elements

    def findKthLargest(self, nums, k):
        maxHeap = []
        size = 0
        N = len(nums)
        
        for num in nums:
            if size == N-k+1:     # max capacity is reached
                heapq.heappushpop(maxHeap, -num)
            else:
                heapq.heappush(maxHeap, -num)
                size += 1
        return -(heapq.heappop(maxHeap))
                

    def findKthLargest(self, nums, k):

        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)
        
        for i in range(1, k):
            heapq.heappop(maxHeap)
        return -(heapq.heappop(maxHeap))
        