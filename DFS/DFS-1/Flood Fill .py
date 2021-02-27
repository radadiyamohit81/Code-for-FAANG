
class Solution:
    # BFS
    # time : O(M*N)
    # space : O(1)
    def floodFill(self, image, sr, sc, newColor):
        # EDGE CASE
        if image[sr][sc] == newColor or len(image) == 0:
            return image
        
        count = 0
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        q = [[sr, sc]]
        while q != []:
            root = q.pop(0)
            for dir in dirs:
                r, c = root[0] + dir[0], root[1] + dir[1]
                if 0 <= r <= len(image)-1 and 0 <= c <= len(image[0])-1 and image[r][c] == oldColor:
                    image[r][c] = newColor
                    q.append([r, c])
                    count += 1
        return image
    
    # DFS
    # time : O(M*N)
    # space : O(1) + Recursive call stack
    def floodFill(self, image, sr, sc, newColor):
        # EDGE CASE
        if image[sr][sc] == newColor or len(image) == 0:
            return image

        oldColor = image[sr][sc]
        self.helper(image, sr, sc, newColor, oldColor)
        return image
    
    def helper(self, image, sr, sc, newColor, oldColor):
        # BASE CASE
        if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] != oldColor:
            return

        # LOGIC
        image[sr][sc] = newColor
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dir in dirs:
            r = sr + dir[0]
            c = sc + dir[1]
            self.helper(image, r, c, newColor, oldColor)
        

obj = Solution()
print(obj.floodFill(image=[[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))