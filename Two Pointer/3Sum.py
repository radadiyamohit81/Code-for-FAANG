class Solution:

    def threeSum1(self, nums):
        if nums == []:
            return []
        
        # sort the array
        # use 2 pointer approach to find the 2nd and 3rd elements
        
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break     
                
            p1 = i+1
            p2 = len(nums)-1
            
            target = 0
            complement = target-nums[i]
            
            while p1 < p2:
                if nums[p1] + nums[p2] == complement:
                    result.append([nums[i], nums[p1], nums[p2]]) 
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1] == nums[p1 -1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 +1]:
                        p2 -= 1
                else:
                    if nums[p1] + nums[p2] < complement:
                        p1 += 1
                    elif nums[p1] + nums[p2] > complement:
                        p2 -= 1
        return result
            
            
                
        

    
    def threeSum2(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.twoSum(nums, i, result)
        return result

    def twoSum(self, nums, index, result):  

        p1 = index +1
        p2 = len(nums) -1
        target = 0
        
        while p1 < p2:
            total = nums[index] + nums[p1] + nums[p2]
            if total < target:
                p1 += 1
            elif total > target:
                p2 -= 1
            elif total == target:
                result.append([nums[index], nums[p1], nums[p2]])
                p1 += 1
                p2 -= 1
                while p1 < p2 and nums[p1] == nums[p1-1]:
                    p1 += 1
                while p1 < p2 and nums[p2] == nums[p2+1]:
                    p2 -= 1
            
                
        
