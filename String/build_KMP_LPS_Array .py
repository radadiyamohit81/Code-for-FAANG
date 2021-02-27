class Solution:
    def buildLPS(self, needle):
        n = len(needle)
        lps = [0]*n
        lps[0] = 0
        j = 0
        i = 1
        
        while i < n:
            # case 1
            if needle[j] != needle[i] and j == 0:
                lps[i] = j
                i += 1
            elif needle[j] != needle[i] and j > 0:
                j = lps[j-1]
            else:
                j += 1
                lps[i] = j
                i += 1    
            
        # print("lps array is ", lps)
        return lps             
                
obj = Solution()
print(obj.buildLPS(needle='aaacaaaa'))   