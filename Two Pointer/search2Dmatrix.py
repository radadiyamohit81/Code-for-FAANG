class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False

        row = len(matrix)-1
        col = 0

        while row >= 0 and col <= len(matrix[0])-1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -=1
            elif matrix[row][col] < target:
                col += 1
        return False
