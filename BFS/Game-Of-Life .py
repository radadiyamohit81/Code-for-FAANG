class Solution:
    def gameOfLife(self, matrix: List[List[int]]) -> None:
        if matrix == [] or len(matrix) == 0:
            return []
        
        dirs = [[0,1], [0,-1], [1,0], [-1,0], [1,1],[-1,1],[1,-1],[-1,-1]]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                activeNeighbors = 0
                for dir in dirs:
                    row = dir[0] + i
                    col = dir[1] + j
                    if 0 <= row <= len(matrix)-1 and 0 <= col <= len(matrix[0])-1:
                        if matrix[row][col] == 1 or matrix[row][col] == 2:
                            activeNeighbors += 1
                if matrix[i][j] == 0 and activeNeighbors == 3:
                    matrix[i][j] = 3
                elif matrix[i][j] == 1:
                    if activeNeighbors > 3 or activeNeighbors < 2:
                        matrix[i][j] = 2
                        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 2:
                    matrix[i][j] = 0
                elif matrix[i][j] == 3:
                    matrix[i][j] = 1
        return matrix