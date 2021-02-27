class Solution1:
    # O(M*N) Time
    # O(1) Space
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or len(needle) == 0:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            haystack_pt = i
            needle_pt = 0
            while haystack_pt < len(haystack) and needle_pt < len(needle):
                if haystack[haystack_pt] == needle[needle_pt]:
                    haystack_pt +=1
                    needle_pt +=1
                else:
                    break
            if needle_pt == len(needle):
                return i
            i+=1
        return -1

#-------------------------------------------------------------------------------------------
class Solution2: 
    # O(M+N) Time
    # O(N) Space for building 
    # KMP-LPS Array on the Pattern Matching

    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        
        if (m == 0 and n == 0) or haystack == needle or n == 0:
            return 0
        if m == 0:
            return -1
        
        # build lps array on the pattern string
        lps = self.buildLPS(needle)
        
        # find the pattern matching using LPS array
        i, j = 0, 0
        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                
            # BASE CASE
            if j == n:
                return i-j
        
            if i < m and haystack[i] != needle[j]:
                if j > 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1
    
    def buildLPS(self, needle):
        n = len(needle)
        lps = [0]*n
        lps[0] = 0
        j = 0
        i = 1
        
        while i < n:
            # case 1
            if needle[j] == needle[i]:
                j += 1
                lps[i] = j
                i += 1 
            # case 2
            elif needle[j] != needle[i] and j == 0:
                i += 1
            # case 3
            elif needle[j] != needle[i] and j > 0:
                j = lps[j-1]
        return lps
                
                
            
        

#--------------------------------------------------------------------------------------

obj1 = Solution1()
print("BruteForce Solution at 0(M*N) Time is : ", obj1.strStr(haystack='aaaacaaaablah', needle='aaacaaaa'))  
                
obj2 = Solution2()
print("KMP-LPS Array Algorithm at O(M+N) Time and O(N) Space is : ", obj2.strStr(haystack='aaaacaaaablah', needle='aaacaaaa')) 
                
            
        

        
        
        
        
        