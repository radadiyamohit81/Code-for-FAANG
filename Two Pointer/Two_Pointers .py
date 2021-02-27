class Solution:
    
    def threeSum(self, nums):           # O(N*N*N) Time
        if not nums:
            return []
        res = []
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        myList = [nums[i], nums[j], nums[k]]
                        myList.sort()
                        if myList not in res:
                            res.append(myList)
        return res
        
    def threeSum(self, nums):           # O(N log N) + O(N*N) ====> O(N*N) Time
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break 

            low = i+1
            high = len(nums)-1
            target = -nums[i]

            while low < high:
                if nums[low] + nums[high] == target:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                    while low < high and nums[high] == nums[high+1]:
                        high -= 1
                else:
                    if nums[low] + nums[high] < target:
                        low += 1
                    else:
                        high -= 1       
        return res
    
    def maxArea(self, height):          # O(N*N)   TLE 
        maxx = float('-inf')
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                area = (j-i) * min(height[i], height[j])
                if area > maxx:
                    maxx = area
        return maxx

    def maxArea(self, height):          # O(N) Time
        maxArea = float('-inf')
        low = 0
        high = len(height)-1
        while low < high:
            area = (high - low)*min(height[low], height[high])
            if area > maxArea:
                maxArea = area
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1        
        return maxArea

    def sortColors(self, nums):      # BruteForce, O[2N] Time
        zeros = 0
        ones = 0
        twos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
            else:
                twos += 1
        i = 0
        while zeros != 0:
            nums[i] = 0
            zeros -= 1
            i += 1
        while ones != 0:
            nums[i] = 1
            ones -= 1
            i += 1
        while twos != 0:
            nums[i] = 2
            twos -= 1
            i += 1
        return nums

    def sortColors(self, nums):        # Optimized, O[N] Time
        if not nums:
            return []
        low = 0
        mid = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 2:
                self.swap(nums, mid, high)
                high -= 1
            elif nums[mid] == 0:
                self.swap(nums, mid, low)
                low += 1
                mid += 1
            else:
                mid += 1
        return nums
    def swap(self, nums, p1, p2):
        temp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = temp

    def merge(self, nums1, m, nums2, n):
        p1 = m-1
        p2 = n-1
        temp = len(nums1)-1
        while p2 >= 0 and p1 >=0:
            if nums1[p1] > nums2[p2]:
                nums1[temp] = nums1[p1]
                temp -= 1
                nums1[p1] = 0
                p1 -= 1
            else:
                nums1[temp] = nums2[p2]
                temp -= 1
                p2 -= 1
        while p2 >= 0:
            nums1[temp] = nums2[p2]
            temp -= 1
            p2 -= 1
        return nums1
            
        
    def searchMatrix(self, matrix, target):
        p1 = len(matrix)-1
        p2 = 0
        
        while p1 >= 0 and p2 <= len(matrix[0]):
            if matrix[p1][p2] == target:
                return True
            elif matrix[p1][p2] > target:
                p1 -= 1
            else:
                p2 += 1
        return False


        
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
obj = Solution()
print(obj.searchMatrix(matrix, target=8))
        

    

