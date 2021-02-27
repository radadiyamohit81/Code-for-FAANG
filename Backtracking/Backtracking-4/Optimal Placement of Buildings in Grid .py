class Solution:

    # NOT WORKING SOLUTION, NEEDS FIXING ===================================

    def optimalBuildingArrangement(self, L, W, n):
        self.min = float('inf')
        grid = [[-1 for i in range(L)] for j in range(W)]

        # place buildings in the grid with all combinations using BACKTRACKING
        # using BFS fill the distance of the parking spot
        self.placeBuilding(grid, 0, 0, n)

        return self.min

    def placeBuilding(self, grid, i, j, n):
        # Base case
        if n == 0:
            self.bfs(grid, i, j)
            return

        # Logic
        for row in range(i, len(grid)):
            for col in range(j, len(grid[0])):
                # ACTION, place building
                grid[row][col] = 0

                # RECURSE
                # checking all column positions on the same row. Then, moving to the next row and checking all columns from col 0
                if col < len(grid[0]):            
                    self.placeBuilding(grid, row, col+1, n-1)
                else:                          
                    self.placeBuilding(grid, row+1, 0, n-1)
    
                # BACKTRACK, to find all other combinations
                grid[row][col] = -1
        

    def bfs(self, grid):
        q = []
        r_len, c_len = len(grid), len(grid[0])
        for row in range(r_len):
            for col in range(c_len):
                if grid[row][col] == 0:
                    q.append([row, col])

        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        # visited = [[False for i in range(c_len)] for j in range(r_len)]
        dist = 0
        while q != []:
            size = len(q)
            for i in range(size):
                r, c = q.pop(0)
                for dir in dirs:
                    new_r = r + dir[0]
                    new_c = c + dir[1]
                if new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]) and grid[new_r][new_c] == -1:
                    
                    grid[new_r][new_c] = dist    #?????????????????????????
                    q.append([new_r, new_c])
                    # visited[new_r][new_c] = True
            dist += 1
            self.min = min( self.min, dist-1 )

        
        








