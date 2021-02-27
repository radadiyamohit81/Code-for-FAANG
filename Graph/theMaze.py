# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
# Given the maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.
# You may assume that the borders of the maze are all walls (see examples).

# Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        a, b = start
        visited = set()
        
        # DFS approach to explore all directions
        visited.add((a, b))
        q = [ [a, b] ]
        while q != []:
            a, b = q.pop(0)
            # choose a direction
            for dir in dirs:
                r = a + dir[0]
                c = b + dir[1]
                # Move in that direction until stopping point
                while 0 <= r <= len(maze)-1 and 0 <= c <= len(maze[0])-1 and maze[r][c] != 1:
                    r += dir[0]
                    c += dir[1]
                r -= dir[0]
                c -= dir[1]
                
                # check if the stopped point is the destination, else mark the stopped point visited and add the ending position to stack to process on all possible directions
                if [r, c] == destination:   
                    return True
                if (r, c) not in visited:
                    visited.add((r, c))
                    q.append([r, c])
                    
        return False
