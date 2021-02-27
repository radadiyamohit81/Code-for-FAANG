# SORT by COUNT
# O[N + 2N] Time
# O[A] Space,       
# A: no.of.alphabets, 26
class Solution:
    def reorganizeString(self, S):
        if S == "":
            return ""
        
        ch_count = {}
        max_ch_count = 0
        max_ch = ""
        for ch in S:
            if ch not in ch_count:
                ch_count[ch] = 1
            else:
                ch_count[ch] += 1
            if ch_count[ch] > max_ch_count:
                max_ch_count = max(max_ch_count, ch_count[ch])
                max_ch = ch
        
        # ****** EDGE CASE *******
        if max_ch_count > (len(S)+1)//2:
            return ""
        
        del ch_count[max_ch]
        result = [None]*len(S)
        i = 0
        while max_ch_count:
            for position in range(i, len(result), 2):
                result[position] = max_ch
                max_ch_count -=1
                if max_ch_count == 0:
                    ch_count[max_ch] = 0
                    for key in ch_count:
                        if ch_count[key] > 0:
                            max_ch = key
                            max_ch_count = ch_count[key]
                            break
            i = 1
        
        return "".join(result)


# GREEDY with MAX-HEAP
# O[N logA] Time 
# O[A] Space
# A: # of alphabets, 26

class Solution2:
    import heapq
    def reorganizeString(self, S):
        if S == "":
            return ""
        
        ch_count = {}
        max_ch_count = 0
        for ch in S:
            if ch not in ch_count:
                ch_count[ch] = 1
            else:
                ch_count[ch] += 1
            if ch_count[ch] > max_ch_count:
                max_ch_count = ch_count[ch]
                max_ch = ch
                
        if max_ch_count > (len(S)+1)//2:
            return ""
        
        maxHeap = []
        for key in ch_count:
            heapq.heappush(maxHeap, [-ch_count[key], key])
        result = ""
        while maxHeap:
            val1, ch1 = heapq.heappop(maxHeap)
            if maxHeap:
                val2, ch2 = heapq.heappop(maxHeap)
            else:
                result += ch1
                break                   #***************
            result += ch1
            result += ch2
            if val1+1 != 0:
                heapq.heappush(maxHeap, [val1+1, ch1])
            if val2+1 != 0:
                heapq.heappush(maxHeap, [val2+1, ch2])
        return result
            
        
        