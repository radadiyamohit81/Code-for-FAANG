class Solution:
    def minMaxValue(self, nums):
        if nums == []:
            return None

        minVal, localMin = float('inf'), float('inf')
        maxVal, localMax = float('-inf'), float('-inf')
        i = 0

        while i < len(nums):
            if i + 1 > len(nums)-1:
                minVal = min(nums[len(nums)-1], minVal)
                maxVal = max(nums[len(nums)-1], maxVal)
                return [minVal, maxVal]

            if nums[i] > nums[i+1]:
                localMax = nums[i]
                localMin = nums[i+1]
            else:
                localMax = nums[i+1]
                localMin = nums[i]
            maxVal = max(localMax, maxVal)
            minVal = min(localMin, minVal)
            i += 2

        return [minVal, maxVal]



obj = Solution()
print(obj.minMaxValue([99,1,2,3,4,-1,9]))
print(obj.minMaxValue([-14, 2, 0, 4, 5, 6, -2, 14]))