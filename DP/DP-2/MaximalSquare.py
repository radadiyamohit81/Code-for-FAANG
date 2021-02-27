
# BRUTEFORCE: O[M*N] Time
class Solution:
    def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        
        maxLen = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                
                if matrix[row][col] == "1":
                    curLen = 1
                    flag = False
                    while row+curLen < len(matrix) and col+curLen < len(matrix[0]) and flag == False:
                        
                        # row check for the same column
                        for k in range(row+curLen, row-1, -1):
                            if matrix[k][col+curLen] == '0':
                                flag = True
                                break
                        if flag == True:
                            break
                        # col check, for the same row
                        for k in range(col+curLen, col-1, -1):
                            if matrix[row+curLen][k] == '0':
                                flag = True
                                break
                        if flag == False:
                            curLen += 1
                    maxLen = max(maxLen, curLen)
        return maxLen*maxLen 
                

#------------------------------------------------------------------------
# DP SOLUTION: O[M*N] Time, O[M*N] Space

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        
        dp = [[0 for col in range(len(matrix[0])+1)] for row in range(len(matrix)+1)]
        maxLen = 0

        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] =='1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
                    maxLen = max(maxLen, dp[i][j])
        return maxLen * maxLen
