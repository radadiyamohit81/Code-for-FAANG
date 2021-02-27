class Solution:

    # row check + col check + block check => 3 PASS SOLUTION
    def isValidSudoku(self, board):
        return self.row_check(board) and self.col_check(board) and self.block_check(board)
    
    def row_check(self, board):    # row check for every row
        for row in range(9):
            flag = [False]*9
            for col in range(9):
                if board[row][col] != '.':  
                    val = int(board[row][col])-1
                    if flag[ val ] == True:   
                        return False
                    flag[ val ] = True
        return True
        
    def col_check(self, board):     # column check for every col
        for col in range(9):
            flag = [False]*9
            for row in range(9):
                if board[row][col] != '.':
                    val = int(board[row][col])-1
                    if flag[ val ] == True:
                        return False
                    flag[ val ] = True
        return True
                    
    def block_check(self, board):    # block check for every block range
        for row_start in range(0, 9, 3):         # 0, 3, 6
            for col_start in range(0, 9, 3):
            
                # block check            
                flag = [False]*9
                for row in range(row_start, row_start+3): 
                    for col in range(col_start, col_start+3):
                        if board[row][col] != '.':
                            val = int(board[row][col])-1
                            if flag[ val ] == True:
                                return False
                            flag[ val ] = True
        return True
                        
                        
            
            
                
            
        
        