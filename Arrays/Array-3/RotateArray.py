class Solution:
    def rotateArray1(self, nums, k):
        while k > 0:
            val = nums.pop(-1)
            nums.insert(0, val)
            k -= 1
    
    def rotateArray2(self, nums, k):
        ans = [0]*len(nums)

        for index in range(len(nums)-1):
            new_index = (index + k) % len(nums)
            ans[new_index] = nums[index]
        nums = ans[:]
        return nums
    
    def rotateArray3(self, nums, k):
        if k > len(nums):
            k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        return nums
    def reverse(self, nums, left, right):
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
    
    