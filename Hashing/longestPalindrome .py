class Solution:
    def longestPalindrome(self, s):
        hashSet = set()
        l = 0
        for char in s:
            if char not in hashSet:
                hashSet.add(char)
            else:
                hashSet.remove(char)
                l += 2 
        if len(hashSet) > 0:
            l += 1
        return l

    def longestPalindrome_2(self, s):
        d = {}
        flag = False
        result = 0

        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        
        for key in d:
            if d[key] % 2 == 0:
                result += d[key]
            else:
                flag = True
                result += d[key] -1  
                # adding only the even count at all time and setting the flag to indicate that 1 additional element can be added at the end 
        
        if flag:
            result += 1
        return result

        
        



            






            