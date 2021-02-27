class Solution:
    def candyCrush(self, board):
        
        # STEP1: MARK ELEMENTS that have to be crushed
        
        # O[M*N] Time -> dfs: O[2M + 2N](Horizontal drop + Vertical Drop)
        # ------> ( O[M*N] * O[2M + 2N] ) + Complxity for CRUSHING: O[ M*N *M ]

        for i in range(len(board)):
            for j in range(len(board[0])):

                # for every (i, j) VERTICAL CHECK & HORIZONTAL CHECK, fill the board, so we can visit all points in the board
                self.dfs(board, i, j)
                
        # STEP2: CRUSH the candies
        if self.crushCandies(board):
            return self.candyCrush(board)
        else:
            return board     # FINAL STATE
            
            
    def crushCandies(self, board):                          # O[ M*N * N ] Time
        crush = False

        for col in range(0, len(board[0])):
            for row in range(0, len(board)):

                # O[ (M*N) * N ] Time
                #********************* MOVE  candies 1 STEP DOWN for collapse at any row
                if board[row][col] < 0:
                    crush = True
                                                            
                    while row >= 0:          
                        if row == 0:   ##
                            board[row][col] = 0
                            break
                        board[row][col] = board[row-1][col]
                        row -= 1
        return crush
        
    def dfs(self, board, r, c):

        # 1) VERTICAL DROP
        r_orig = r
        c_orig = c
        count = 0
        while r < len(board):
            if r+1 == len(board):   ####
                break
            if abs(board[r][c]) == abs(board[r+1][c]):      
                count += 1
            else:
                break
            r += 1

        if count >= 2:           #********************* IF 3 CANDIES ARE SAME, only 2 matches -> COUNT = 2
            while count >= 0:
                if board[r][c] > 0:
                    board[r][c] = -board[r][c]
                r -= 1
                count -= 1

        # 2) HORIZONTAL DROP
        count = 0
        r = r_orig
        while c < len(board[0]):
            if c+1 == len(board[0]):   ####
                break
            if abs(board[r][c]) == abs(board[r][c+1]):
                count += 1
            else:
                break
            c += 1

        if count >= 2:           #*********************
            while count >= 0:
                if board[r][c] > 0:
                    board[r][c] = -board[r][c]
                c -=1
                count -= 1
        
