# // Throws an error if 'row' or 'col' is out of bounds
# public Response getResponse(int row, int col) {
# 	// black box
# }
# enum Response {
# 	HOTTER,  // Moving closer to target
# 	COLDER,  // Moving farther from target
# 	SAME,    // Same distance from the target as your previous guess
# 	EXACT;   // Reached destination
# }

# Output: [4, 3]

# Binary Search
grid = [['o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'x', 'o'],
        ['o', 'o', 'o', 'o', 'o']]

class Solution:
    def findObject(self, grid):
        m = len(grid)
        n = len(grid[0])
        top, bottom = 0, m-1
        left, right = 0, n-1

        rowIndex = self.find_row_binarySearch(top, bottom)
        colIndex = self.find_col_binarySearch(left, right)

        return [rowIndex, colIndex]


    def find_row_binarySearch(self, low, high):
        while low <= high:
            # for any fixed column, finding the row by binary searching 
            # through the row length at its midpoints 
            mid = low + (high - low)//2
            col = 0

            if self.getResponse(grid, mid, col) == 'Exact' or (self.getResponse(grid, mid-1, col) != 'Hotter' and self.getResponse(grid, mid+1, col) != 'Hotter'):
                return mid
            elif self.getResponse(grid, mid+1, col) == 'Hotter':
                low = mid +1
            else:
                high = mid -1

    def find_col_binarySearch(self, low, high):
        while low <= high:
            # for any fixed row, finding the column by binary searching through the col length at its midpoints 
            row = 0
            mid = low + (high - low)//2
            
            if self.getResponse(grid, row, mid) == 'Exact' or (self.getResponse(grid, row, mid-1) != 'Hotter' and self.getResponse(grid, row, mid+1) != 'Hotter'):
                return mid
            elif self.getResponse(grid, row, mid+1) == 'Hotter':
                low = mid +1
            else:
                high = mid -1
