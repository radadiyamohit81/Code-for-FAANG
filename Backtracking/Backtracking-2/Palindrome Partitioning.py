# Time Complexity : Exponential
# Space Complexity : 
# Did this code successfully run on Leetcode : YES


class Solution:
    def partition(self, s):
        self.result = []
        self.dfs(s, 0, [])
        return self.result
    
    def dfs(self, s, index, temp):
        # Base case
        if index == len(s):
            self.result.append(temp[::])
            return
        
        # Logic
        for i in range(index, len(s)):
            subString = s[index:i+1]
            if self.isPalindrome(subString):
                temp.append(subString)
                self.dfs(s, i+1, temp)
                
                # Backtrack to remove the last combination to try other combination
                temp.pop()
        
    def isPalindrome(self, subString):
        l = 0
        r = len(subString)-1
        
        if l == r:
            return True
        
        while l < r:
            if subString[l] == subString[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        
        
                
                
            
        