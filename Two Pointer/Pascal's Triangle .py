class Solution:
    def pascalTriangle(self, n):
        if n == 0:
            return []
        res = [[1]]
        for row in range(1, n):
            temp = [1]
            for j in range(1, row):
                val = res[row-1][j-1] + res[row-1][j]
                temp.append(val)
            temp.append(1)
        res.append(temp)
        return res
