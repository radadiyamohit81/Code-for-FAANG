class Solution:
    def deleteAndEarn(self, nums):
        self.helper(nums, i=0, points=0)
        self.helper(nums, i=1, points=0)


    # OPTIMIXED, O[N] Time + O[10000] for building the COUNTER ARRAY
    # O[10000] Space for the COUNTER ARRAY
    def deleteAndEarn(self, nums):
        
        # COUNTER TABLE
        dp = [0]*10000
        for num in nums:
            dp[num] += num
        
        prevSkip = 0 
        preTake = 0
        for i in range(1, 10000):
            skip = max(prevSkip, preTake)
            take = prevSkip + dp[i] 
            
            prevSkip = skip
            preTake = take
        
        return max(prevSkip, preTake)
            
            