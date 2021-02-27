class Solution:

    # Iterative Solution
    def search(self, nums, target):
        # EDGE CASE
        if len(nums) == 0:
            return -1
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:   # 1st half is sorted
                if nums[low] <= target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:                        # 2nd half is sorted
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1

    # Recursive Solution

class Solution2:
    # O(Log N) Time; O(N) space
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        return self.helper(nums, target, 0, len(nums)-1)

    def helper(self, nums, target, low, high):
        # Base Case
        if low > high:  
            return -1

        # Logic
        mid = low + (high-low)//2        # to avoid Integer overflow in Java
        if nums[mid] == target:
            return mid
        elif nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
        return self.helper(nums, target, low, high)



