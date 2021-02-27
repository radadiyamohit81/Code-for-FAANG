# O(M * N) Time
# O(M * N) Space

class Solution:
    def findDiagonalOrder(self, matrix):
        if len(matrix) == 0:
            return []
        
        i = row = col = 0
        m = len(matrix)
        n = len(matrix[0])
        direction = +1
        result = []
        
        while i < m*n:
            result.append(matrix[row][col])
            if direction == +1:
                # FORWARD DIRECTION, direction changes at Last Col and First row, 
                if col == n -1:
                    direction = -1
                    row += 1
                elif row == 0:
                    direction = -1
                    col += 1
                else:
                    row -= 1
                    col += 1
            elif direction == -1:
                # REVERSE DIRECTION, direction changes at Last row and First column,
                if row == m-1:
                    direction = +1
                    col += 1
                elif col == 0:
                    direction = +1
                    row += 1
                else:
                    row += 1
                    col -= 1
            i += 1
        return result


matrix = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
output = Solution()
print(output.findDiagonalOrder(matrix))

        