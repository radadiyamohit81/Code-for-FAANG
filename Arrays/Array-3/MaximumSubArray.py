class Solution:

    # BRUTEFORCE: N*N Time
    # OPTIMIZED: SLIDING WINDOW Approach, 2 Pointers: N Time
    
    def maxSubArray(self, nums):
        if nums == []:
            return 0
        
        globalMaxima = float('-inf')
        runningSum = 0
        for num in nums:
            runningSum += num
            if runningSum > num:    # if adding the num has increased the value
                globalMaxima = max(runningSum, globalMaxima)
            else:
                runningSum = num
                globalMaxima = max(runningSum, globalMaxima)
        return globalMaxima
