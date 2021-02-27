
class Solution:
    def findDisappearedNumbers(self, nums):   

        # Time Complexity : O(N) 
        # Space Complexity : O(N)
        # Did this code successfully run on Leetcode : YES
        # Logic: Using HashSet, Search Operation in HashSet is O(1)

        if nums == [] or len(nums) == 0:          #Edge Case
            return []

        result = []
        _hashset = set()
        for i in nums:
            _hashset.add(i)
        for i in range(len(nums)):
            if i+1 not in _hashset:
                result.append(i+1)

        return result


    def findDisappearedNumbers(self, nums):   

        # Time Complexity : O(N*N) 
        # Space Complexity : O(1)
        # Did this code successfully run on Leetcode : NO, Time Limit Exceeded

        if nums == [] or len(nums) == 0:           #Edge Case
            return []
             
        result = []
        for i in range(len(nums)):
            if i+1 not in nums:
                result.append(i+1)
        return result


    def findDisappearedNumbers(self, nums):   

        # Time Complexity : O(N) 
        # Space Complexity : O(1)

        # -----------OPTIMAL SOLUTION--------------

        if nums == []:
            return []
        
        for num in nums:
            # negate the num-1 index in the arr to Indicate VISITED
            index = abs(num) -1
            if nums[index] > 0:
                nums[index] *= -1
            
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result

output = Solution()
print(output.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
        
        