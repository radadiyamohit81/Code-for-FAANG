# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        if head == None:
            return 
        
        # finding the midpoint
        mid = self.midPoint(head)
        
        # breaking the LL into 2 halves
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2) 
        l1 = temp = head
        
        # reordering the LL
        while l1.next != None and l2 != None:
            temp = l1.next
            l1.next = l2
            l2 = l2.next 
            l1.next.next = temp 
            l1 = temp
        return head
            
        
    def midPoint(self, head):
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow 

    
    def reverse(self, head):
        if not head:
            return None
        
        dummy = None
        slow = head
        fast = head.next   
        while slow.next != None:
            slow.next = dummy
            dummy = slow  
            slow = fast
            fast = fast.next
        slow.next = dummy
        return slow  
    
    
             
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        if head == None or head.next == None:
            return None
        
        result = l1 = head
        # Floyd's Algorithm to find the MID-POINT        
        mid = self.findMid(head)
        
        # Breaking the LL into l1, l2
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)
        
        # reordering the LL
        dummy = ListNode(-1)
        while l1 != None and l2 != None:
            dummy.next = l1
            l1 = l1.next
            dummy = dummy.next
            dummy.next = l2
            l2 = l2.next 
            dummy = dummy.next
        
        if l1 != None:
            dummy.next = l1
        return result
    
    def findMid(self, head):
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def reverse(self, head):
        if head == None or head.next == None:
            return head
        
        slow = None
        current = head
        fast = head
        while current.next != None:
            fast = fast.next
            current.next = slow
            slow = current
            current = fast
        current.next = slow
        return current
        
        
            
        
        
        
        
        
        