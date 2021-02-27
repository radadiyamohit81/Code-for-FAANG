class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        i = 0
        summ = 0
        
        while i < len(nums)-1:
            summ += nums[i]
            i += 2
        return summ
        