class Solution:
    def removeAllDuplicates_inPlace(self, nums):
        slow = 0
        fast = 1
        
        while fast <= len(nums)-1:
            if nums[fast] == nums[fast-1]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return len(nums[:slow+1])



    def removeDuplicates_inPlace(self, nums):
        if not nums:
            return 0
        flag = False
        slow = 0
        fast = 1
        
        while fast <= len(nums)-1:
            if nums[slow] == nums[fast]:
                if flag == False:
                    flag = True
                    slow += 1
                    nums[slow] = nums[fast]
                    fast += 1
                else:
                    while fast <= len(nums)-1 and nums[fast] == nums[fast-1]:
                        fast += 1
            else:
                flag = False
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return len(nums[:slow+1])
            
        