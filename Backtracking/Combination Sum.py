# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates 
# where the chosen numbers sum to target. 
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

# Time Complexity : Exponential
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : YES
class Solution:
    def combinationSum(self, candidates, target):
        if candidates == [] or target == 0:
            return
        self.result = []
        self.dfs_backtrack(candidates, target, 0, [], 0)
        return self.result

    def dfs_backtrack(self, candidates, target, index, temp, calculated):
        # BASE CASE
        if calculated > target:
            return
        if calculated == target:
            self.result.append(temp[::])

        # LOGIC
        for i in range(index, len(candidates)):    # ACTION
            temp.append(candidates[i])
            self.dfs_backtrack(candidates, target, i, temp, calculated+candidates[i])  # RECURSE

            # BACKTRACK to check the other possibilities
            # remove the last insert and add the next element
            temp.pop()
            
