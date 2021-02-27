# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):

        left = 0
        right = 1
        
        # Identifying the Search Space
        while reader.get(right) < target:
            # Identify the Search space
            left = right
            right = right*2
        
        # Binary Search on the Search Space 
        return self.binarySearch(reader, target, left, right)
        return -1
                
    def binarySearch(self, reader, target, left, right):
        # BASE CASE
        if left > right:
            return -1
        
        mid = left + (right-left)//2
        if reader.get(mid) == target:
            return mid
        
        if reader.get(left) <= target <= reader.get(mid):
            right = mid -1
        else:
            left = mid +1
        return self.binarySearch(reader, target, left, right)
        