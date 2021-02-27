
class Solution:

    def countIsland(self, matrix):
        if matrix == [] or len(matrix) == 0:
            return 0

        island_count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    island_count += 1
                    # DFS to fill the island with 0
                    self.dfs(matrix, i, j)
        return island_count


    def dfs(self, matrix, i, j):
        # BASE CASE
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
            return

        # LOGIC
        matrix[i][j] = 0                 
        dirs = [[-1, 0], [0, -1], [0, 1], [1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]  
        ##considering the diagonal directions aswell
        for dir in dirs:
            r, c = i + dir[0], j + dir[1]
            self.dfs(matrix, r, c)



obj = Solution()
print(obj.countIsland(matrix=[[1,0,1,1], [1,1,0,0], [1,0,0,0], [0,0,1,1]]))


