class Solution:
    def findPeakElement(self, nums):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if low == high or nums[mid] > max(nums[mid-1], nums[mid+1]):
                return mid
            if nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid-1

        return nums[-1]