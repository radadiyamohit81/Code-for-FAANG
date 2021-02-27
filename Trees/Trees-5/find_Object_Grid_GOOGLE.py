# Given a char grid (o represents an empty cell and x represents a target object) and an API getResponse which would give you a response w.r.t. to your previous position. Write a program to find the object. You can move to any position.

# enum Response {
# 	HOTTER,  // Moving closer to target
# 	COLDER,  // Moving farther from target
# 	SAME,    // Same distance from the target as your previous guess
# 	EXACT;   // Reached destination
# }

# // Throws an error if 'row' or 'col' is out of bounds
# public Response getResponse(int row, int col) {
# 	// black box
# }

# Example :

# Input:
# [['o', 'o', 'o', 'o', 'o'],
#  ['o', 'o', 'o', 'o', 'o'],
#  ['o', 'o', 'o', 'o', 'o'],
#  ['o', 'o', 'o', 'o', 'o'],
#  ['o', 'o', 'o', 'x', 'o'],
#  ['o', 'o', 'o', 'o', 'o']]

# Output: [4, 3]


# BINARY SEARCH 
# O[log M + log N] Time

from enum import Enum, auto

class Response(Enum):
    HOTTER = auto()
    COLDER = auto()
    SAME = auto()
    EXACT = auto()

class Solution:
    def __init__(self, grid):
        self.grid, self.m, self.n = grid, len(grid)-1, len(grid[0])-1
        self.x, self.y = -1, -1         # current position

    def getResponse(self, r, c):
        pass
        # Black Box

    def find_object(self, grid):
        row = self.row_search(grid, 0, self.m)
        col = self.col_search(grid, 0, self.n)
        return [row, col]
    
    def row_search(self, grid, start, end):
        # Binary Seach to find the row
        while start <= end:
            mid = (start + end) // 2
            if self.getResponse(grid, mid, 0) == Response.EXACT or (self.getResponse(grid, mid+1, 0) != Response.HOTTER) and (self.getResponse(grid, mid-1, 0) != Response.HOTTER):
                return mid
            elif self.getResponse(grid, mid+1, 0) == Response.HOTTER:
                start = mid+1
            else:
                end = mid-1

    def col_search(self, grid, start, end):
        # Binary Seach to find the col
        while start <= end:
            mid = (start + end) // 2
            if self.getResponse(grid, mid, 0) == Response.EXACT or (self.getResponse(grid, mid+1, 0) != Response.HOTTER) and (self.getResponse(grid, mid-1, 0) != Response.HOTTER):
                return mid
            elif self.getResponse(grid, mid+1, 0) == Response.HOTTER:
                start = mid+1
            else:
                end = mid-1


    







    



