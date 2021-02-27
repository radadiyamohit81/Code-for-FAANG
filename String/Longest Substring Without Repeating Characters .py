class Solution:
    def lengthOfLongestSubstring(self, s):
        # BRUTEFORCE TLE
        # Time: O[N*N*N] 
        # Space: O[26] for set
        maxLen = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                substring = s[i:j]
                if self.isValid(substring):
                    maxLen = max(maxLen, len(substring))
        return maxLen
    def isValid(self, substring):
        visited = set()
        for i in range(len(substring)):
            if substring[i] in visited:
                return False
            else:
                visited.add(substring[i])
        return True

    def lengthOfLongestSubstring(self, s):
        # OPTIMIZED - SLIDING WINDOW APPROACH
        # O[N] Time
        # O[N] Sapce for HashMap

        maxLen = 0
        d = {}
        # initiate a slow and fast pointer and move fast pointer untill you can make a window of all unique ch
        slow = 0
        for fast in range(len(s)): 
            if s[fast] not in d:
                d[s[fast]] = fast
                maxLen = max(maxLen, fast+1-slow)
            else:
                # DUPLICATE is Found => 
                # MOVE YOUR SLIDING WINDOW by updating the SLOW to check for other possibilites by taking the current fast element as we already have seen the casewith the previous duplicate element, 
                # => slow should move to include the current fast character in our window,

                slow = max(slow, d[s[fast]]+1)   
                d[s[fast]] = fast              
                maxLen = max(maxLen, fast+1-slow)
        return maxLen 
            