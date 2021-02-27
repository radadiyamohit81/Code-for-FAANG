class Solution:
    # GREEDY APPROACH
    # O[N] Time
    # O[1] Space
    
    def longestPalindrome(self, s):
        if s == '':
            return 0
        
        l = 0
        hashSet = set()
        for i in range(len(s)):
            if s[i] not in hashSet:
                hashSet.add(s[i])
            elif s[i] in hashSet:
                hashSet.remove(s[i])
                l += 2
        
        if len(hashSet) == 0:
            return l
        else:
            return l+1 