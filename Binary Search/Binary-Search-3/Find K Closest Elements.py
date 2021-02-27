# Time Complexity : log(N)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : YES

class Solution:
    def findClosestElements(self, arr, k, x):
        l = 0
        r = len(arr) - k
        
        while l < r:
            mid = (l + r) // 2
            
            if abs(arr[mid] - x) > abs(arr[mid + k] -x):
                l = mid + 1
            else:
                r = mid
                
        return arr[l: l+k]
            
        
        