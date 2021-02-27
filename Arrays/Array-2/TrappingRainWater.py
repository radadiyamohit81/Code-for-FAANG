class Solution:




    # ????????? why TRAP WATER on the side with the SMALLER WALL at every step

    # ==> WATER TRAPPED AT THE LAST CASE IS BOUNDED BETWEEN LEFTWALL & RIGHTWALL => WATER-TRAPPED IS THE HEIGHT OF THE SMALLER WALL AMOUNG THEM.
    
    def trap(self, height):
        if height == []:
            return 0
        
        waterTrapped = 0
        left = 0
        leftWall = float('-inf')   # MOVE left and leftWall until leftWall > height[left], to create a BARRIER with LeftWall to TRAP WATER
#       --------------------------
        rightWall = float('-inf')
        right = len(height)-1
        
        while left <= right:     # TRAP all water BTWN LEFT & RIGHT 
            if leftWall <= rightWall:    # at every iteration, TRAP WATER on the side with the SMALLER WALL ~ we should trap the last water with the bigger wall...   
                if leftWall <= height[left]:       # NO-WATER
                    leftWall = height[left]
                    left += 1
                elif leftWall > height[left]:      # Water can be TRAPPED, left alone moves for the same leftWall               
                    waterTrapped += (leftWall - height[left])
                    left += 1
            
            elif rightWall < leftWall:
                if rightWall <= height[right]:     # NO-WATER
                    rightWall = height[right]
                    right -= 1
                elif rightWall > height[right]:     # Water can be TRAPPED, right alone moves for the same rightWall
                    waterTrapped += (rightWall - height[right])
                    right -= 1
        
        return waterTrapped
                    