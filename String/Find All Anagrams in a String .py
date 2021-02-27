class Solution:
    # SLIDING WINDOW APPROACH incoming character, outgoing charcters and the size of the match in sliding window is tracked. 
    # Time complexity = O( N + M ), space complexity = O(26)

    def findAnagrams(self, s, p):
        if s == '' or p == '':
            return []
        
        # 1) maintain a COUNTER of p characters in d
        d = {}
        for ch in p:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

        result = []
        match = 0
        for i in range(len(s)):
            # 2) PROCESS IN-COMING CHARACTER
            if s[i] in d:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    match += 1
            
            # 3) PROCESS OUT-GOING CHARACTER after i > len(p)-1
            if i > len(p)-1:
                outgoing_ch = s[i-len(p)]
                if outgoing_ch in d:
                    d[outgoing_ch] += 1
                    if d[outgoing_ch] == 1:
                        match -= 1
                    
            # 4) CHECK FOR ANAGRAM MATCH
            if match == len(d):
                result.append(i-len(p)+1)
        return result
            
                
                

obj = Solution()
print(obj.findAnagrams(s = 'cbaebabacd', p='abc'))
print(obj.findAnagrams(s = "baa" ,p ="aa"))