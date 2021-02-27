class Solution:
    def candyCrush(self, board):
        
        
        # STEP1: mark the elements that have to be crushed
        # originalBoard = board[:][:]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # fill the board
                self.dfs(board, i, j)
                
        # STEP2: crush the candies
       # print(board)
        if self.crushCandies(board):
            return self.candyCrush(board)
        else:
            return board
            
            
    def crushCandies(self, board):
        crush = False
        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col] < 0:
                    crush = True
                    # board[row][col] = 0
                    while row >= 0:
                        if row == 0:
                            board[row][col] = 0
                            break
                        board[row][col] = board[row-1][col]
                        row -= 1
        return crush
        
    def dfs(self, board, r, c):
        # BASE CASE
        # Vertical Drop
        r_orig = r
        c_orig = c
        count = 0
        while r < len(board):
            if r+1 == len(board):            ####
                break
            if abs(board[r][c]) == abs(board[r+1][c]):
                count += 1
            else:
                break
            r += 1
        if count >= 2:
            while count >= 0:
                if board[r][c] > 0:
                    board[r][c] = -board[r][c]
                r -= 1
                count -= 1
        # Horizontal Drop
        
        count = 0
        r = r_orig
        while c < len(board[0]):
            if c+1 == len(board[0]):        ####
                break
            if abs(board[r][c]) == abs(board[r][c+1]):
                count += 1
            else:
                break
            c += 1
        #print("horizontal count",r,c-count,count)
        if count >= 2:
            while count >= 0:
                if board[r][c] > 0:
                    board[r][c] = -board[r][c]
                c -=1
                count -= 1
        
        
        
                
                
                    
                
                
                    
                    
                    
                    
                
                
        
        
        