class Solution:
    
    def generateParenthesis(self, n):
        self.n = n
        self.result = []
        self.backtrack(0, 0, "")
        return self.result
    
    def backtrack(self, left, right, stringg):
        # BASE CASE
        if left == right == self.n:
            self.result.append(stringg)
            return
            
        if left < self.n:
            self.backtrack(left+1, right, stringg+'(')
        if right < left:
            self.backtrack(left, right+1, stringg+')')
