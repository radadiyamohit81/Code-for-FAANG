
class Solution:
    # BFS
    # time : O(M*N)
    # space : O(1)

    def updateMatrix(self, matrix):
        if not matrix or len(matrix) == 0:
            return matrix

        q = []
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append([i, j])
                else:
                    matrix[i][j] = float('inf')
        
        while q != []:
            root = q.pop(0)
            for dir in dirs:
                r = dir[0]+root[0]
                c = dir[1]+root[1]
                if  0 <= r <= len(matrix)-1 and 0 <= c <= len(matrix[0])-1 and matrix[r][c] > matrix[root[0]][root[1]] + 1:
                    matrix[r][c] = matrix[root[0]][root[1]] + 1
                    q.append([r, c])
                    
        return matrix

# DFS approach can be done with an additional space for visted Array and visiting only the RIGHT & BOTTOM cells
# DFS => NO EXTRA SPACE SOLN => ******** TRY DOING IT **********
    
obj = Solution()
print(obj.updateMatrix(matrix=[[0,0,0], [0,1,0], [1,1,1]]))