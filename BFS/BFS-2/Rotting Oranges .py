
class Solution:
    # BFS 
    # time : O(M*N)
    # space : O(M*N)
    # NOTE: pay attenetion to boundary conditions 

    def orangesRotting(self, grid):
        if len(grid) == 0:
            return 0

        dirs = [[1,0], [-1,0], [0, 1], [0,-1]]
        freshCount = 0
        minute = 0

        # take count of all fresh, add (i, j) of rotten items to q
        q = [] 
        for i in range(len(grid)):     
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    q.append((i, j))           
        if q == []:
            if freshCount == 0:
                return 0
            return -1

        # every minute all the adjacent items to rotten items are rotten,
        # change freshItems(1) adjacent to the rottenItem(2) to (2), decrease fresh count, increase a minute after 1 one iteration
        while q != []:
            size = len(q)
            for i in range(size):
                root = q.pop(0)
                for dir in dirs:
                    r = root[0] + dir[0]
                    c = root[1] + dir[1]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                        grid[r][c] = 2
                        freshCount -= 1
                        q.append([r, c])
            minute += 1
            
        if freshCount != 0:
            return -1
        return minute-1    # last step adds additional minute
        
                    

obj = Solution()
print(obj.rottingOranges(grid=[[2,1,1],[1,1,0],[0,1,1]]))


    
            


