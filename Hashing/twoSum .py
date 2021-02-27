class Solution:
    def twoSum(self, nums, target):
        d = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement not in d:
                d[num] = index
            else:
                return [d[complement], index]