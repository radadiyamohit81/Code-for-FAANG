# Thinking process - How?

# Here's my thought process, Hope it helps you

# Let's see test cases
# x = 1024 y = 1
# -- the only way we can reach a lower number is by decrementing (CORNER CASE 1)

# x = 4 y = 4
# -- no operations needed so zero (BASE CASE)

# x = 5 y=8
# -- I can double 5 and decrement
# -- I can decrement 5 and double it
# -- I have two options to choose from, in some cases first one could give right answer and in some cases, the second one can give the right answer. Ex: x = 5 y= 9 or x = 5 y = 8
# -- There will be lot of edge cases if I go with above approach

# ** Let's try some other approach **
# -- Observation: The only way to increase value is by doubling it and the only way to decrease value is by decrementing it.
# -- To get minimum operations we have to use doubling as much as possible and decrementing as few as possible.
# -- if y is odd there's no way I can reach it by doubling a number, I have to reach y+1 and decrement it by one, to reach y+1 i have to reach (y+1)/2 in minimum steps
# -- if y is even I can reach it by doubling a number, so it boils down to reaching y/2 in minimum steps.
# Use test cases to reason and logic around your solution.
# Hope it helped you. Cheers.




class Solution:
    def brokenCalc(self, x, y):
        operations = 0
        while y > x:
            if y % 2 != 0:
                y = y+1
            else:
                y = y//2
            operations += 1

        return operations + (x-y)