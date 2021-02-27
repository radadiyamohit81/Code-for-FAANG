
class ListNode:
    def __init__(self, key):
        self.val = key
        self.next = None


class Solution:
    # time : O(N*K), N: avg.no.of.nodes/linkedlist, K: no.of.linkedlist
    # space: O(N) to store result LL

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == None or len(lists) == 0:
            return None
        
        merged = ListNode(float('-inf'))
        result = merged
        for head in lists:
            merged = self.mergeTwoLists(merged, head)
        return result.next
            

    def mergeTwoLists(self, l1, l2):
        # EDGE CASE
        if l1 == None and l2 == None:
            return None

        dummy = ListNode(0)
        result = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
            else:
                dummy.next= l2
                l2 = l2.next
                dummy = dummy.next
        if l1 != None:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        return result.next
    

#========================================================================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class SolutionOPTIMIZED:
    import heapq

    # O[NlogK] Time
    # O[K] Space for Heapq + O[N] for Result LL
    def mergeKLists(self, lists):
        if lists == []:
            return None
        
        # Maintain a MinHeap of all the 1t nodes in the Lists
        minHeap = []
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i])) 
        
        result = current = ListNode(-1)
        while minHeap:
            poppedVal, index, poppedNode = heapq.heappop(minHeap)

            current.next = ListNode(poppedVal)
            current = current.next
            
            node = poppedNode.next
            if node != None:
                heapq.heappush(minHeap, (node.val, index, node))
             
        return result.next  
        