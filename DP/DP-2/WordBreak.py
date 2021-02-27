# BRUTEFORCE: TRY ALL COMBINATIONS AND CHECK IF A SUBSTRING IS PRESENT IN DICT, IF THEN SEARCH THE REST OF THE SUBSTRING. CONTINUE UNTILL LEN ==0
# RECURSIVE TREE OF CHOICES IS BUILT
# O[2^N] Time, O[# OF WORDS FOR HASHSET]  => TLE
class Solution1:
    def wordBreak(self, s, wordDict):
        if s == "":
            return True
        
        self.found = False
        self.hashSet = set(wordDict)    # for o[1] lookup
        return self.helper(s)
    
    def helper(self, s):
        
        # base case
        if len(s) == 0:    # Split of words have happened and we have reached the end of the string
            self.found = True
            return
        
        # logic
        prefix_s = ""
        for i, ch in enumerate(s):
            prefix_s += ch
            if prefix_s in self.hashSet:
                self.helper(s[i+1:])
        
        return self.found


# DP OPTIMIZED SOLUTION: 
# O[N*N] Time for iterations, O[N+1] for dp array and O[words] for hashSet 

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True

        hashSet = set(wordDict)
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for j in range(0, i):
                if dp[j] == 1 and s[j:i] in hashSet:
                    dp[i] = 1
    
        return dp[-1] == 1

class Solution2:
    def wordBreak(self, s, wordDict):
        if s == "":
            return True

        hashSet = set(wordDict)
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        for i in range(len(dp)):
            j = 0
            while j < i: 
                if dp[j] == 1 and s[j:i] in hashSet:
                    dp[i] = 1
                j += 1
        return dp[-1] == 1



                