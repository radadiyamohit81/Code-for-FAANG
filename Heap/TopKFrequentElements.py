# MIN HEAP OF SIZE K
# O[N log K] Time
# O[N+ K] Space

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
                
        minHeap = []
        for key in num_count:
            heapq.heappush( minHeap, [num_count[key], key] )
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        result = []
        while minHeap != []:
            result.append(heapq.heappop(minHeap)[1])
        return result