class Solution:
    import collections

    # def groupAnagram(self, strs):
        # d = {}
        # result = []
        # for word in strs:
        #     hashVal = ''.join(sorted(word))
        #     if hashVal not in d:
        #         d[hashVal] = [word]
        #     else:
        #         d[hashVal].append(word)
        
        # for val in d.values():
        #     result.append(val)
        # return result
    
    def groupAnagram2(self, strs):
        d = collections.defaultdict(list)
        for word in strs:
            count = [0]*26
            for ch in word:
                position = ord(ch) - ord('a') 
                count[position] += 1 
            # print(count)
            # print("Tuple is: ", tuple(count))

            d[tuple(count)].append(word) 
        return d.values()
               
        

obj = Solution()
print(obj.groupAnagram2(strs = ["eat","tea","tan","ate","nat","bat"]))