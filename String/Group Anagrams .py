class Solution1:
    # O[NK] Time
    # O[NK] Space
    def groupAnagrams(self, strs):
        if strs == []:
            return []

        d = {}
        for word in strs:
            # create a ordinance array => tuple to create unique entries
            hashVal = [0]*26
            for ch in word:
                hashVal[ord('a') - ord(ch)] += 1
            hashVal = tuple(hashVal)
            if hashVal not in d:
                d[hashVal] = [word]
            else:
                d[hashVal].append(word)
        result = []
        for key in d:
            result.append(d[key])
        return result 
                

class Solution2:
    # O[ NK ] Time
    # O[ N * KlogK ] Space
    def groupAnagrams(self, strs):
        if strs == []:
            return []
            
        d = {}
        for word in strs:
            hashVal = "".join(sorted(word))
            if hashVal not in d:
                d[hashVal] = [word]
            else:
                d[hashVal].append(word)
        
        res = []
        for key in d:
            res.append(d[key])
        return res