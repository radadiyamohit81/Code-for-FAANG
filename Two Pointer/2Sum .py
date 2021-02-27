class Solution:
    def twoSum(self, nums, target):
        d = {}
        
        for index, elem in enumerate(nums):
            # checking if the complement of this element lies in the HashMap
            complement = target - elem
            if complement in d:
                return [index, d[complement]]
            
            d[elem] = index
