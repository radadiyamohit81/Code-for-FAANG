class Solution1:
    # BRUTEFORCE => TLE
    # O[NK] Time 
    # O[N-K+1] Space for O/P + O[K] for sliding Window slice copy
    
    def maxSlidingWindow(self, nums, k):
        if nums == []:
            return []

        result = []
        for i in range(len(nums)+1-k):
            result.append(max(nums[i:i+k]))
        return result

class Solution2:
    # MAX-HEAP, WORST CASE: Increasing Sequence, 
    # O[N log N] Time 
    # O[N] Space
    import heapq
    def maxSlidingWindow(self, nums, k):
        if nums == []:
            return []
        
        maxHeap = []
        result = []
        for i in range(len(nums)):
            heapq.heappush(maxHeap, [-nums[i], i])
            
            # discard elements the values only if the top value dont belong in this Window
            while maxHeap[0][1] <= i-k:
                heapq.heappop(maxHeap)
            
            # Add the top value to my answer,
            if i >= k-1:
                result.append(-maxHeap[0][0])
        return result
        
# class Solution3:
    # DEQUE 
    # O[N] Time
    # O[N-K+1] Space for O/P + O[K] atmost deque size
    
    from collections import deque
    def maxSlidingWindow(self, nums, k):
        if nums == []:
            return []

        result = []
        dq = deque()
        
        # retain only the biggest val and its index in the 1st K slice Window && add the value to result
        for i in range(k):
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            dq.append([nums[i], i])
            while dq and dq[0][1] < i-k:
                dq.popleft()
        result.append(dq[0][0])
        
        for i in range(k, len(nums)):
            # discard all elements from the right whose values are smaller to the value to be added
            # add the current element
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            dq.append([nums[i], i])
            
            # discard all the elements from the left whose index lies outside the Window, to maintain the sliding Window of size K
            while dq[0][1] <= i-k:
                dq.popleft()
            result.append(dq[0][0])
            
        return result
            
                
            
            
            
                
                
        