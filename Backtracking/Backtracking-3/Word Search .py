class Solution:
    def exist(self, board, word):
        self.visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        # print(self.visited)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j): return True
        return False
    
    def dfs(self, board, word, i, j):
        # Base case
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or self.visited[i][j] == 1:
            return False
        
        # Logic
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        if board[i][j] == word[0]:
            if len(word) == 1:
                return True
            self.visited[i][j] = 1
            for dir in dirs:
                r = dir[0] + i
                c = dir[1] + j
                if self.dfs(board, word[1:], r, c):
                    return True
                
            # backtrack if the character doesnt match to find match from previous character
            self.visited[i][j] = 0
                
        return False
                

        
        