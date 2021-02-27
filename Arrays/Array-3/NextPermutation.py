class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-2
        while i >= 0 and nums[i]>=nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j -=1
            self.swap(nums, i, j)
        self.reverse(nums, i+1)
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def reverse(self, nums, start):
        end = len(nums)-1
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start +=1 
            end -= 1
    