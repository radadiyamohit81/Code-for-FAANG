# BRUTEFORCE: find all possible partition Combination sum, O[K^N] Time, EXPONENTIAL SOLN

# DP OPTIMIZED: O[N*K] Time, O[N] Space
class Solution:
    def maxSumAfterPartitioning(self, A, K):
        if A == []:
            return 0
        
        dp = [0]*len(A)
        dp[0] = A[0]
        
        for i in range(1, len(A)):
            partitionMax = A[i]
                                        
            for k in range(K):        # for different partitions of k slices, k = 0, 1, 2,.. k
                if i-k >= 0:          # EDGE CASE, incase of 1st few elements where index < K
                                      # FINDING THE BIGGEST ELEMENT IN SUBARRAY
                    partitionMax = max(partitionMax, A[i-k])   
                    if i-k > 0:       # if previous partition exists
                        dp[i] = max( dp[i], dp[i-k-1] + partitionMax*(k+1) )
                    elif i-k == 0:    # if no previous partitions 
                        dp[i] = max( dp[i], partitionMax*(k+1) )
        return dp[-1]