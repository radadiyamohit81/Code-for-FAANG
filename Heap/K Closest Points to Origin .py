class Solution:
    import heapq
    def kClosest(self, points, K):
        # we need to maintain a MIN-HEAP of size K
        # O[N log K] Time
        # O[K] Space
        
        kClosestPoints = []
        size = 0                   # we need to maintain maxHeap of size K,
        for point in points:
            distance = (point[0] - 0)**2 + (point[1]-0)**2
            heapq.heappush(kClosestPoints, (-distance, point))
            size += 1
            if size > K:
                heapq.heappop(kClosestPoints)
            
        result = []
        while kClosestPoints != []:
            result.append(heapq.heappop(kClosestPoints)[1])
        return result
                
            
        