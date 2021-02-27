
# STACK approach        (storing -- unresolved elements in stack)
# time : O(2N), better than bruteforce O(N*N) 
# space : O(1) 
# run on leetcode: yes


class Solution:
    def dailyTemperatures(self, T):
        # EDGE CASE
        if T == []:
            return []
        
        unresolvedDates = [ 0 ]
        hotterDate = [0]*len(T)
        for i in range(1, len(T)):
            while unresolvedDates != [] and T[i] > T[unresolvedDates[-1]]:
                unresolved = unresolvedDates.pop()
                hotterDate[unresolved] = i - unresolved
            unresolvedDates.append(i)
        return hotterDate
            


        
obj = Solution()
print(obj.dailyTemperatures(T = [73, 74, 75, 71, 69, 72, 76, 73]))
