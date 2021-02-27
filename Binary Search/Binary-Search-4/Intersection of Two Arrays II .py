class Solution:
    # Bruteforce 
    # O(M+N) Time
    # O(M) Space 

    # create counter for elements on nums1
    # for elem in nums2, if the elem is in nums1, decrement count, add it to result
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
        
        res = []
        d = {}
        for i in nums1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in nums2:
            if i in d:
                d[i] -= 1
                res.append(i)
            elif i not in d:
                continue
            if d[i] == 0:
                del d[i]
        return res

    #-----------------------------------------------------------------------------
    # Two Pointers
    # O(MlogM + NlogN) Time
    # O[1] Space

    # sort both num1, nums2
    # compare element on both and if p1 val is smaller, increment p1 until maatch happens and vice-versa,

    def intersection(self, nums1, nums2):
        if nums1 == [] or nums2 == []:
            return []
        
        if len(nums2) > len(nums1):
            return self.intersection(nums2, nums1)
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        result = set()
        
        while p1 <= len(nums1)-1 and p2 <= len(nums2)-1:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] == nums2[p2]:
                result.add(nums1[p1])
                p1 += 1
                p2 += 1
        return result
            

    #-----------------------------------------------------------------------------
    # Binary Search Solution
    # O(MlogM + NlogN) Time

    # sort both nums1, num2
    # for elem in smaller arr, BS on nums1 and find index
    # repeat the same for other elements in nums2 with low set to index+1

    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
        nums1.sort()
        nums2.sort()
        res = []
        low = 0
        
        for num in nums1:
            search_res = self.binarySearch(nums2, low, len(nums2)-1, num)
            if search_res != -1:
                res.append(num)
                low = search_res + 1
        return res
    
    def binarySearch(self, nums, low, high, target):
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                if mid == low or nums[mid-1] < target:
                    return mid
                else:
                    high = mid - 1

            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1
        return -1
            
            
    