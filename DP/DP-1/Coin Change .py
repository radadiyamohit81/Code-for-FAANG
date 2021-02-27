
# BRUTEFORCE: RECURSIVE SOLUTION

# Did problem run on Leetcode: yes with TLE 
# Time Complexity: O(2^n)
# Space Complexity: No Extra Space, Recursive Stack uses O(n)

class Solution:
    def coinChange(self, coins, amount):
        return self.helper(coins,amount,0,0)
    
    def helper(self, coins, amount, index, minn):

        # BASE CASE
        if index > len(coins)-1 or amount < 0:
            return -1
        if amount == 0:          #exit case
            return minn

        # LOGIC
        case1 = self.helper(coins, amount-coins[index], index, minn+1)         # choose coin
        case2 = self.helper(coins, amount, index+1, minn)                      # Not-choose coin

        if case1 == -1:
            return case2
        elif case2 == -1:
            return case1
        else:
            return min(case1,case2)

output = Solution()
print(output.coinChange(coins=[1, 2, 5], amount=11))





#-------------------------------------------------------------------------------------------------------
# OPTIMIZED: DYNAMIC PROGRAMMING SOLUTION

# Did problem run on Leetcode: yes 
# Time Complexity: O(m * n), where m: no of rows in dp matrix and n: no of columns in dp matrix
# Space Complexity: O(m * n), is the size of DP martix created

class Solution:
    def coinChange(self, coins, amount):

        # extra row for adding float(inf); extra column for adding 0
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]

        # populating all the rows of 0th column with 0,
        for i in range(1, len(coins)+1):
            dp[i][0] = 0

        # populating all the columns of 0st row with INF, to indicate IMPOSSIBLE
        for i in range(1, amount+1):
            dp[0][i] = float('inf')

        # populating the DP Matrix,
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j < coins[i - 1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min( dp[i-1][j], dp[i][j-coins[i-1]]+1 ) 
        
        # answer is the last element in the matrix
        result = dp[-1][-1]

        if result == float('inf'):
            return -1
        else:
            return result

output = Solution()
print(output.coinChange(coins=[1, 2, 5], amount=11))
