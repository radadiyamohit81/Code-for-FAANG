
# RECURSIVE SOLUTION

# TLE Maximum Recursion Depth Exceeded
# Time Complexity: O(2^N)
# Space Complexity: No Extra Space, Recursive Stack O(N)

class Solution:
    def rob(self, nums):
        if nums == []:
            return 0
        
        return self.helper(nums, index=0, amount=0)
    
    def helper(self, nums, index, amount):
        # BASE CASE
        if index >= len(nums):
            return amount
        
        # LOGIC
        # Choose house,
        choose = self.helper(nums, index+2, amount + nums[index] )
        
        # Not-Choose house,
        notChoose = self.helper(nums, index+1, amount )        
        
        # Reduced Number of Comparisons than updating a Global variable tracking the maxAmount
        return max(choose, notChoose)
        
           
        




#---------------------------------------------------------------------------------


# DYNAMIC PROGRAMMING SOLUTION

# Did problem run on Leetcode: yes 
# Time Complexity: O(m * n), where m: no of rows in dp matrix and n: no of columns in dp matrix
# Space Complexity: O(m * n), is the size of DP martix

class Solution:
    def rob(self, nums):
        if nums == []:
            return 0
        
        dp = [[0 for col in range(2)] for row in range(len(nums))]
        
        dp[0][0] = 0             # choose
        dp[0][1] = nums[0]       # Not-choose
        
        for row in range(1, len(nums)):
            for col in range(0, 2):
                
                # Not-choose the num
                if col == 0:
                    dp[row][col] = max(dp[row-1][col], dp[row-1][col+1])
                
                # Choose the num
                elif col == 1:
                    dp[row][col] = dp[row-1][col-1] + nums[row]
            
        print(dp)
            
        return max(dp[-1][-1], dp[-1][0])
    
            



#---------------------------------------------------------------------------------
# DYNAMIC PROGRAMMING SOLUTION OPTIMIZED USING 2 VARIABLES

# Did problem run on Leetcode: yes 
# Time Complexity: O(m*n) => O(m) as n is small 
# Space Complexity: O(1), as we are using only two variables


    def rob(self, nums):
        if nums == []:
            return 0
        
        notChoose = 0
        choose = nums[0]
        
        for i in range(1, len(nums)):
            temp = choose
            choose = notChoose + nums[i]
            notChoose = max(temp, notChoose)
            
            
        return max(choose, notChoose)

output = Solution()
print(output.houseRobber(nums=[1, 2, 3, 1]))