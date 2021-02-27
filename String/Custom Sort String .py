class Solution:
    # O[ST] Time
    # O[T] Space
    def customSortString(self, S, T):
        if T == '':
            return ''
        
        res = ''
        d = {}
        for ch in T:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        
        for ch in S:
            if ch in d:
                res += ch*d[ch]
                del d[ch]
        
        for key in d:
            res += key*d[key]
        return res
        