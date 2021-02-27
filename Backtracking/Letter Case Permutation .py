class Solution:
    def letterCasePermutation(self, S):
        if S == '':
            return ''
        
        self.result = []
        self.helper(S, 0, '')
        return self.result
    
    def helper(self, S, i, temp):
        # BASE CASE
        if i == len(S):
            self.result.append(temp)
            return
    
        # LOGIC
        if S[i].isalpha():
            self.helper(S, i+1, temp+S[i].upper())
            self.helper(S, i+1, temp+S[i].lower())
        else:
            self.helper(S, i+1, temp+S[i])