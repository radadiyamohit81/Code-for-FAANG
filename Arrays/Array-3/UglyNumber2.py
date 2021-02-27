import heapq
class Solution:
    # BRUTEFORCE: check all the possible factor of every number and add the numbers having only 2, 3, 5 in an array in result array, return the nth element
    # HeapQ + Visited SET  => O[ N*logN ] Time, O[ N ] HASH-SET Space
    def nthUglyNumber(self, n):
        visited = set()
        pq = []

        visited.add(1)
        heapq.heappush(pq, 1)
        i = 1
        while i < n:
            currentUgly = heapq.heappop(pq)
            for num in [2,3,5]:
                newUgly = currentUgly*num
                if newUgly not in visited:
                    visited.add(newUgly)
                    heapq.heappush(pq, newUgly)
            i += 1
        return heapq.heappop(pq)


    # OPTIMIZED: O[1] Time, O[1] Space
    def nthUglyNumber2(self, n):
        i2 = i3 = i5 = 0
        nums = [1]
        
        for i in range(1, 1690):
            newUgly = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            nums.append(newUgly)
            
            if newUgly == nums[i2]*2:
                i2 += 1
            if newUgly == nums[i3]*3:
                i3 += 1
            if newUgly == nums[i5]*5:
                i5 += 1
            
        return nums[n-1]

obj = Solution()
print(obj.nthUglyNumber(50))
