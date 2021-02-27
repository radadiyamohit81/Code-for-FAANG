
# Stack approach        (storing -- unresolved elements in stack)
# time : O(2N), we will loop through the array twice 
# space : O(1)

class Solution:
    def nextGreaterElements1(self, nums):
        if nums == []:
            return []
        
        unresolvedIndexes = [0]
        result = [-1]*len(nums)
        solved = 0
        to_solve = len(nums)
        for i in range(2*len(nums)): 
            i = i % len(nums)
            while unresolvedIndexes != [] and nums[unresolvedIndexes[-1]] < nums[i]:
                unresolved = unresolvedIndexes.pop()
                result[unresolved] = nums[i]
                solved += 1
            unresolvedIndexes.append(i)
                
        return result



obj = Solution()
print(obj.nextGreaterElements1(nums=[1,2,1]))
print(obj.nextGreaterElements2(nums=[1,2,1]))







