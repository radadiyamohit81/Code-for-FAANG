class Solution:
    
    def spiralOrder(self, matrix):
        if len(matrix) == 0: 
            return []
        if len(matrix) == 1:
            return matrix[0]
        
        result = []
        
        top_row = 0
        bottom_row = len(matrix)-1
        left_col = 0
        right_col = len(matrix[0])-1

        while top_row <= bottom_row and left_col <= right_col:
            # TOP-MOST ROW 
            for col in range(left_col, right_col+1):
                result.append( matrix[top_row][col] )
            top_row += 1
            
            # RIGHT-MOST COL
            for row in range(top_row, bottom_row+1):
                result.append( matrix[row][right_col] )
            right_col -= 1
            
            # BOTTOM-MOST ROW      
            if bottom_row >= top_row:                # --- EDGE CASE ---
                for col in range(right_col, left_col-1, -1):
                    result.append( matrix[bottom_row][col] )
                bottom_row -= 1
            
            # LEFT-MOST COL 
            if left_col <= right_col:                 # --- EDGE CASE ---
                for row in range(bottom_row, top_row-1, -1):
                    result.append( matrix[row][left_col] )
                left_col += 1
        return result
        
        
        

output = Solution()
print(output.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]))


                    

        

        