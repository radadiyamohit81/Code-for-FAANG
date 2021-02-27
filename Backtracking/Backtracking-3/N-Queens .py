class Solution:
    def solveNQueens(self, n):
        self.result = []
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.placequeens(0)
        return self.result
    
    def placequeens(self, i):   
        # for every row index i, Placing Q at different col for every row i
        
        # Base case
        if i == len(self.board):
            temp = []
            for row in range(len(self.board)):
                res = ''
                for col in range(len(self.board[0])):
                    if self.board[row][col] == 1:
                        res += 'Q'
                    else:
                        res += '.'
                temp.append(res)
    
            self.result.append(temp)
            return False
        
        # Logic                 
        for j in range(len(self.board[0])):  
            if self.isValidPosition(i, j):
                self.board[i][j] = 1
                if self.placequeens(i+1):     # placing next Q on next row
                    return True
            
            # backtrack the last position to explore other combinations
            self.board[i][j] = 0
        return False

        
    def isValidPosition(self, i, j):
        # check the entire column
        for row in range(i):
            if self.board[row][j] == 1:
                return False
        
        # check the left diagonal
        m = i -1
        n = j -1
        while m >= 0 and n >= 0:
            if self.board[m][n] == 1:
                return False
            m -=1
            n -=1
        
        # check the right diagonal
        m = i -1
        n = j +1
        while m >= 0 and n < len(self.board[0]):
            if self.board[m][n] == 1:
                return False
            m -=1
            n +=1
        
        return True
            
        
        