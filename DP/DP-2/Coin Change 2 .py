
# RECURSIVE SOLUTION

# Time Complexity: O( Amount^n )
# Space Complexity: No additional space except the space for Recursive stack
# Did problem run on Leetcode: yes, with TLE

class Solution:
    def coinChange2(self, amount, coins):
        return self.helper(amount, coins, 0)

    def helper(self, amount, coins, index):

        # BASE CASE
        if amount == 0:
            return 1
        if amount < 0 or index > len(coins)-1:
            return 0

        #LOGIC
        # Not-Choose the coin,
        case1 = self.helper(amount, coins, index+1)
        # Choose the coin,
        case2 = self.helper(amount-coins[index], coins, index)

        return case1 + case2

obj = Solution()
print(obj.coinChange2(amount=5, coins=[1, 2, 5]))



# DP SOLUTION

# Time Complexity: O(M*N), M: no.of.rows made, N: no.of. columns made
# Space Complexity: O(M*N) for dp matrix built
# Did problem run on Leetcode: yes

class Solution2:
    def coinChange2(self, coins, amount):

        #creating a DP matrix,
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]

        dp[0][0] = 1
        for i in range(1, len(coins)+1):
            # populating the 0th column with 1 ~ to make amount 0 (always 1 way to make 0 from any denomination)
            dp[i][0] = 1

            for j in range(1, amount+1):
                # ***  coins = [1,2,3]    ,coin 3 is at index i = 3 in dp matrix and at index 2 in coins array => i-1  ***
                # if the amount to be made is less than the current denomination, use the result from previous row
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                # use the current denomination with no.of.ways to make ( amount - currentDenomation ),
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                    
        return dp[-1][-1]




        




