class Solution:
    # O( (M+N)log(M+N) )
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = nums1 + nums2
        nums1.sort()
        
        l = len(nums1)
        low = 0
        high = len(nums1)-1
        mid = low + (high-low)//2
        
        if l%2 != 0:    # odd number of elements
            return nums1[mid]
        else:           # even number of elements
            return (nums1[mid] + nums1[mid+1])/2

class Solution2:
    # Binary Search Approach
    def findMedianSortedArrays(self, A, B):
        n1 = len(A)
        n2 = len(B)
        
        if n1 > n2:
            return self.findMedianSortedArrays(B, A)
        
        low = 0 
        high = n1
        
        while low <= high:
            partition_A = low + (high - low)//2
            partition_B = (n1 + n2 + 1)//2 - partition_A
            
            # finding the l1, r1, l2, r2
            l1 = float('-inf') if partition_A == 0 else A[partition_A -1]
            r1 = float('inf') if partition_A == n1 else A[partition_A]
            
            l2 = float('-inf') if partition_B == 0 else B[partition_B -1]
            r2 = float('inf') if partition_B == n2 else B[partition_B]
            
            # Check
            if l1 <= r2 and l2 <= r1:
                # Return the Median
                if (n1+n2) % 2 != 0:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
                
            elif l2 > r1:
                low = partition_A +1
            else:
                high = partition_A -1
        
        
        
                
                
            
        
        
        

        
        
        
        

    
    

        
        
        
        