class Solution:
    import heapq
    from collections import deque
    def topKFrequent(self, words, k):
        word_count = {}
        maxLen = 0
        for word in words:
            maxLen = max(maxLen, len(word))
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

        minHeap = []
        for key in word_count:
            ord_lst = []
            for ch in key:
                ord_val = -(ord(ch)-ord('a'))           #***************
                ord_lst.append(ord_val)
            while len(ord_lst) < maxLen:
                ord_lst.append(float('inf'))
            if len(minHeap) < k:
                heapq.heappush(minHeap, [word_count[key], ord_lst, key])
            else:
                heapq.heappush(minHeap, [word_count[key], ord_lst, key])
                heapq.heappop(minHeap)
            
        
        result = deque()                                #***************
        while minHeap != []:
            result.appendleft(heapq.heappop(minHeap)[2])
        return result
        
