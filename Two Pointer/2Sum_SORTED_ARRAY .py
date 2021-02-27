class Solution:
    def twoSum(self, numbers, target):
        p1 = 0
        p2 = len(numbers)-1
        
        while True:
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            elif numbers[p1] + numbers[p2] == target:
                return [p1+1, p2+1]
        