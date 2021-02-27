class Solution:
    def contiguousSubArray_maxLen(self, nums):
        d = {0 : -1}
        runningSum = 0
        l = 0

        for i, num in enumerate(nums):
            if num == 1:
                runningSum += 1
            else:
                runningSum -= 1
            if runningSum not in d:
                d[runningSum] = i
            else:
                l = max(l, i-d[runningSum])
        return l