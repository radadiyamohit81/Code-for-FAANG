class Solution:
    def subarraySum(self, nums, k):     
        # O[N * N * N] Time, TLE
        counter = 0  
        for i in range(len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                summ += nums[j]
                if summ ==k:
                    counter += 1
        return counter
    
    def subarraySum(self, nums, k): 
        counter = 0
        d = {}
        d[0] = 1

        runningSum = 0
        for num in nums:
            runningSum += num
            if runningSum - k in d:
                counter += d[runningSum - k]
            
            if runningSum in d:
                d[runningSum] += 1
            else:
                d[runningSum] = 1
        return counter
        