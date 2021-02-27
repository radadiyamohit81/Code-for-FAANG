
class Solution:
    # O(N) Time 
    # O(2N) Space
    def productExceptSelf1(self, nums):
        if nums == []:
            return []
        
        left = [0]*len(nums)
        right = [0]*len(nums)
        left[0] = 1
        right[len(nums)-1] = 1
        
        ans = [0]*len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]        # left side running Product is stored
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]      # right side running Product is stored
        for i in range(len(nums)):
            ans[i] = left[i] * right[i]            # both are multiplied to find answer
        return ans
        
    #--------------------------------------------------------------------------------------
    # O(2N) Time
    # O(N) Space
    def productExceptSelf2(self, nums):
        if nums == []:
            return []

        ans = [0]*len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]      # left side running Product is stored
            
        runningProd = 1                        # right side running Product is calcualted and multiplied
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * runningProd
            runningProd *= nums[i]
        
        return ans
            


output = Solution()
print(output.productExceptSelf2([1,2,3,4]))
