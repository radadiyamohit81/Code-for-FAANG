class Solution:

    # O[X + KlogX] Time ,X: min(K, N)
    # O[no of rows] Space
    import heapq
    def kthSmallest(self, matrix, k):
        
        # Build a MIN-HEAP with the 1st element from each of the rows in the Matrix,
        # Merge k Sorted Linked List Implementation to identify the Kth smallest value
        minHeap = []
        
        for i in range(len(matrix)):
            heapq.heappush(minHeap, [matrix[i][0], (i,0)])
            
        while k > 0:
            val, position = heapq.heappop(minHeap)
            k -=1 
            row, col = position[0], position[1]
            if col + 1 <= len(matrix[0]) -1:
                heapq.heappush(minHeap, [matrix[row][col+1], (row, col+1)])
        
        return val
             
        
        