
# BRUTEFORCE RECURSIVE SOLUTION

# Time Complexity: O(m * 2^n), m: no.of. columns, n: no.of.rows       => TLE
# Space Complexity: No additional space except the space for Recursive stack
# Did problem run on Leetcode: yes, with TLE
class Solution1:
    def minCost(self, costs):
        if costs == []:
            return 0
        
        # BRUTEFORCE APPROACH => FOR EACH HOUSECOLOR, CHOOSE MIN OF THE OTHER HOUSE COLORS IN THE NEXT LEVEL
        
        self.minCost = float('inf')
        for houseColor in range(0, 3):
            # houseColor => 0 Red/ 1 Blue/ 2 Green 
            
            pathCost = self.helper(costs, houseColor, i=0, cost=0)
            if pathCost < self.minCost:
                self.minCost = pathCost
        return self.minCost
    
    def helper(self, costs, houseColor, i, cost):
        # BASE CASE
        if i == len(costs):
            return cost
        
        # LOGIC
        # for every color this level, the next levels can be any of the other 2 colors
        option1 = 0
        option2 = 0
        if houseColor == 0:
            option1 += self.helper(costs, 1, i+1, cost + costs[i][1])
            option2 += self.helper(costs, 2, i+1, cost + costs[i][2])
        elif houseColor == 1:
            option1 += self.helper(costs, 0, i+1, cost + costs[i][0])
            option2 += self.helper(costs, 2, i+1, cost + costs[i][2])
        elif houseColor == 2:
            option1 += self.helper(costs, 0, i+1, cost + costs[i][0])
            option2 += self.helper(costs, 1, i+1, cost + costs[i][1])
        
        return min( option1, option2 )

obj = Solution()
print(obj.minCost(costs=[[17,2,17],[16,16,5],[14,3,19]]))




# DP SOLUTION

# Time Complexity: O(M*N), M: no.of.rows, N: no.of. columns
# Space Complexity: O(M*N) for dp matrix
# Did problem run on Leetcode: yes
class Solution2:
    def minCost(self, costs):

        if costs == []:
            return 0
        
        dp = [[0 for col in range(len(costs[0]))] for row in range(len(costs))]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        
        for i in range(1, len(costs)):
            dp[i][0] = costs[i][0] + min( dp[i-1][1], dp[i-1][2] )
            dp[i][1] = costs[i][1] + min( dp[i-1][0], dp[i-1][2] )
            dp[i][2] = costs[i][2] + min( dp[i-1][0], dp[i-1][1] )
        
        l = len(dp)
        return min( dp[l-1][0], dp[l-1][1], dp[l-1][2] )

obj = Solution()
print(obj.minCost(costs=[[17,2,17],[16,16,5],[14,3,19]]))



# MUTATING THE GIVEN MATRIX

# Time Complexity: O(M*N), M: no.of.rows, N: no.of. columns
# Space Complexity: O(1), No extra Data Structure used
# Did problem run on Leetcode: yes
class Solution3:
    def minCost(self, costs):
        if costs == []:
            return 0
        
        # Mutataing the same array
        for row in range(1, len(costs)):
            costs[row][0] += min(costs[row-1][1], costs[row-1][2])
            costs[row][1] += min(costs[row-1][0], costs[row-1][2])
            costs[row][2] += min(costs[row-1][0], costs[row-1][1])
        return min(costs[-1][0], costs[-1][1], costs[-1][-1])
        

# WITHOUT MUTATING THE GIVEN MATRIX USING 3 VARIABLES 

# Time Complexity: O(M*N), M: no.of.rows, N: no.of. columns
# Space Complexity: O(1), No extra Data Structure used
# Did problem run on Leetcode: yes

class Solution:
    def minCost(self, costs):
        if not costs:
            return 0
        lastR = costs[0][0]
        lastB = costs[0][1]
        lastG = costs[0][2]

        for i in range(1, len(costs)):
            currentR = costs[i][0] + min(lastB, lastG)
            currentB = costs[i][1] + min(lastR, lastG)
            currentG = costs[i][2] + min(lastR, lastB)
            lastR = currentR
            lastB = currentB
            lastG = currentG
        return min(lastR, lastB, lastG)
        

obj = Solution()
print(obj.minCost(costs=[[17,2,17],[16,16,5],[14,3,19]]))