class Solution:
    def circularArrayLoop(self, nums):
        if len(nums) <= 1:
            return False
        
        for i in range(len(nums)):
            slow = fast = i
        
            # initially set the direction of the loop
            if nums[i] > 0:
                direction = +1
            else:
                direction = -1
            
            # check if a loop is happening by tortoise and heir algo
            while True:
                slow = self.getNextPosition(nums, slow, direction)
                if slow == -1:
                    break

                fast = self.getNextPosition(nums, fast, direction)
                if fast == -1:
                    break
                
                # since the fast pointer should move 2 steps, ****************
                fast = self.getNextPosition(nums, fast, direction)
                if fast == -1:
                    break

                # ^^^^LOOP FOUND^^^^
                if slow == fast:
                    return True
        return False

    def getNextPosition(self, nums, index, direction):
        if nums[index] > 0:
            currentDirection = +1
        else:
            currentDirection = -1

        if currentDirection != direction:
            return -1
        
        nextIndex = (index + nums[index]) % len(nums)
        
        if nextIndex == index:
            return -1
        return nextIndex
    
        