class Solution:
    def findMin(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0] 
        
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if high > mid and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if low < mid and nums[mid] < nums[mid-1]:
                return nums[mid]
            
            # eliminate the sorted half in the search space
            if nums[low] <= nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return nums[0]
        
        






        