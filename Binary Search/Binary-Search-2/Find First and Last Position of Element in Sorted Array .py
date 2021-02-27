        
class Solution:
    # O[log N] Time
    # O[1] Space
    
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        
        left = 0
        right = len(nums)-1
        result = []
        
        while left <= right:
            if left > right:
                return [-1, -1]
            mid = left + (right - left)//2
            if nums[mid] == target:
                start = self.startIndex(nums, target, mid)
                end = self.endIndex(nums, target, mid)
                result.append(start)
                result.append(end)
                return result
            if nums[left] <= target <= nums[mid]:
                right = mid -1
            else:
                left = mid +1
        return [-1, -1]
                
    def startIndex(self, nums, target, index):
        while index-1 >= 0:
            if nums[index-1] == target:
                index -= 1
            elif nums[index-1] != target:
                return index
        return index

    def endIndex(self, nums, target, index):
        while index+1 < len(nums):
            if nums[index+1] == target:
                index += 1
            elif nums[index+1] != target:
                return index
        return index
            
    

#--------------------------------------------------------------------------


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.startIndex(nums, target)
        end = self.endIndex(nums, target)
        return [start, end]
        
    def startIndex(self, nums, target):
        if len(nums)==0:
            return -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                if low == mid or nums[mid-1] < target:
                    return mid
                else:
                    high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1

    
    def endIndex(self, nums, target):
        if len(nums) == 1 and nums[0] == target:
            return 0
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                if high == mid or nums[mid+1] > target:
                    return mid
                else:
                    low = mid+1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1
                        
                    

      
                    
            
            
        
        


    
