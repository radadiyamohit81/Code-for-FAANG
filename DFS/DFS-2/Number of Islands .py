
class Solution:

    # BFS 
    # time : O(M*N) ; space : O(1)

    # NOTE: once a '1' is visited, increase count += 1, change it to '0' BEFORE THE BFS immediately to avoid DEADLOCK ~ infinte loop,

    def numIslands(self, grid):
        # EDGE CASE
        if grid == [] or len(grid) == 0:
            return 0

        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        island_count = 0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # if island is found, BFS to fill the connected island with 0
                if grid[i][j] == '1':
                    island_count += 1
                    grid[i][j] = '0'
                    q.append([i, j])    # Filling only the connected island with 0

                    while q != []:
                        node = q.pop(0)
                        for dir in dirs:
                            newR = node[0] + dir[0]
                            newC = node[1] + dir[1]
                            if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == '1':
                                q.append([newR, newC])
                                grid[newR][newC] = '0'            
        return island_count

# -------------------------------------------------------------------------------------------------------------------
    # DFS 
    # time : O(M*N)
    # space : O(1) + Recursive call stack
    # NOTE: once a '1' is visited, increase count += 1, change it to '0' immediately BEFORE THE DFS to avoid DEADLOCK ~ infinte loop,


    def numIslands(self, grid):
        if len(grid) == 0:
            return 0

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if island is found, DFS to fill the connected island with 0
                if grid[i][j] == '1':
                    island_count += 1
                    self.dfs(grid, i, j)     # Filling only the connected island with 0
        return island_count
    
    def dfs(self, grid, r, c):
        # BASE CASE
        if r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1 or grid[r][c] == '0':
            return

        # LOGIC
        grid[r][c] = '0'       #*********************
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        for dir in dirs:
            newR, newC = dir[0]+r, dir[1]+c
            self.dfs(grid, newR, newC)


obj = Solution()
print(obj.numIslands(grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
                        
        

        

        
