# Time Complexity : O(M * N)
# Space Complexity : O(M * N)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : Logic

class Solution:
    def findDiagonalOrder(self, matrix):
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        
        m = len(matrix)
        n = len(matrix[0])
        row_ind = 0
        col_ind = 0
        direction = +1
        
        result = []
        elem_count = 0
        while elem_count < m*n:
            result.append(matrix[row_ind][col_ind]) 
            
            # FORWARD DIRECTION: 2 SPECIAL CASES: DIRECTION CHANGES -> 0th ROW, LAST COL 
            if direction == +1:   
                if col_ind == n-1:
                    row_ind += 1
                    direction = -1
                elif row_ind == 0:
                    col_ind += 1
                    direction = -1
                else:
                    row_ind -= 1
                    col_ind += 1
                
            # BACKWARD DIRECTION: 2 SPECIAL CASES: DIRECTION CHANGES -> 0th ROW, LAST COL 
            elif direction == -1:                           
                if row_ind == m-1:
                    col_ind += 1
                    direction = +1
                elif col_ind == 0:
                    row_ind += 1
                    direction = +1
                else:
                    row_ind += 1
                    col_ind -= 1
            # print(row_ind, col_ind, result)
            elem_count += 1
        return result
        


matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

output = Solution()
print(output.findDiagonalOrder(matrix))

        