# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        if head ==  None:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        for i in range(n):
            fast = fast.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head, n):
        if n == 1 and head.next == None:
            return None
        
        result = head
        l = 0
        while head != None:
            head = head.next
            l +=1
        head = result
        
        if l == n:
            return result.next
        
        while l-n-1 > 0:
            head = head.next
            l -= 1
        
        head.next = head.next.next
        return result



        
