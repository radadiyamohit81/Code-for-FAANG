class Solution:
    # BRUTEFORCE
    # O[N*N*N] Time TLE
    # O[1] Space
    def longestPalindrome(self, s):   
        if len(s) == 0 or s == "":
            return ""

        res = ""
        # find all substrings,
        for i in range(len(s)):
            for j in range(len(s)):
                if self.isPalindrome(s, i, j) and len(s[i:j+1]) > len(res) :
                    res = s[i:j+1]
        return res
    
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    #=============================================================
    # EXPAND AROUND CENTER
    # O[N*N] Time
    # O[1] Space
    def longestPalindrome(self, s):
        if s == '':
            return ''
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = self.expandCenter(s, i, i)
            l2 = self.expandCenter(s, i, i+1)
            maxLen = max(l1, l2)
            if maxLen > end - start:
                start = i - (maxLen-1)//2    # O indexing
                end = i + (maxLen)//2        # 0 indexing compensated with slicing
        return s[start:end+1]
    
    def expandCenter(self, s, left, right):
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left-1
    