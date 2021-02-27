# This is Sea's API interface.
# class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

# BinarySearch + BFS 
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        res = 0
        left, right = bottomLeft.x, topRight.x
        top, bottom = topRight.y, bottomLeft.y
        q = [(left, right, top, bottom)]
        
        while q:
            left, right, top, bottom = q.pop(0)
            # EDGE CASE
            if left > right or bottom > top:
                continue
            
            hasShip = sea.hasShips(Point(right, top), Point(left, bottom))
            if hasShip == False:
                continue
                
            # BASE CASE
            if left == right and top == bottom:
                res += 1
            else:
                # create 4 quadrants and search in them untill BASE CASE IS REACHED
                midX = (left + right) // 2
                midY = (top + bottom) // 2
                q.append((left, midX, top, midY+1))     # QUADRANT 1
                q.append((midX+1, right, top, midY+1))    # QUADRANT 2
                q.append((left, midX, midY, bottom))       # QUADRANT 3
                q.append((midX+1, right, midY, bottom))     # QUADRANT 4
        return res            
        