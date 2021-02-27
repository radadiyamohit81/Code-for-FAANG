class Solution:

    # BRUTEFORCE
    # SORTING + LINEAR SEARCH: (NlogN + N)Time
    # SORTING + BINARY SEARCH: (NlogN + logN)Time

    def hIndex(self, citations):
        citations.sort()
        n = len(citations)
        for index, value in enumerate(citations):
            if citations[index] >= n - index:
                return n - index
        return 0

#----------------------------------------------------------------
    # BINARY-SEARCH  ==> O[N] Time if the Arr is SORTED

    def hIndex(self, citations):
        if citations == []:
            return 0
        
        low = 0
        high = len(citations)-1
        while low <= high:
            mid = low + (high - low)//2
            if citations[mid] == len(citations)-mid:
                return len(citations) - mid
            elif citations[mid] > len(citations)-mid:
                high = mid -1
            else:
                low = mid +1 
                
        return len(citations)-low 


#----------------------------------------------------------------

    # OPTIMIZED 
    # TOPOLOGICAL SORT: (N Time + N Space)

    def hIndex_optimized(self, citations):
        if citations == []:
            return 0
        
        visited = [0]*(len(citations)+1)
        for i in range(len(citations)):
            if citations[i] > len(citations):
                visited[-1] += 1
            else:
                visited[citations[i]] += 1
                
        summ = 0
        for i in range(len(citations), -1, -1):
            summ += visited[i]
            if summ >= i:
                return i
        return 0


#---------------------------------------------------------------- 
