class Solution:
    def wordPattern(self, pattern, str):
        list_str = str.split(' ')
        if len(pattern) != len(list_str) or len(set(pattern)) != len(set(list_str)):
            return False
            
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = list_str[i]
            else:
                if d[pattern[i]] != list_str[i]:
                    return False
        print(d)
        return True