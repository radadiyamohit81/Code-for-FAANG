class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # BRUTEFORCE: O[N] Time, O[N] Space
    # push all Nodes into a set and if node already exists in set, return Node

    # O[2N] Time, O[1] Space
    def detectCycle(self, head):
        slow = fast = head
        cycle = False
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # check if cycle is detected
            if slow == fast:
                cycle = True
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
                

class Solution:
    # O[2N] Time, O[1] Space
    def detectCycle(self, head):
        # EDGE CASE
        if head == None or head.next == None:
            return None
        self.slow = head
        self.fast = head
        self.flag = False
        
        while self.fast != None and self.fast.next != None:     # Find if Cycle is present
            self.slow = self.slow.next
            self.fast = self.fast.next.next
            if self.slow == self.fast:
                self.flag = True
                break

        if self.flag == False:      # No Cycle Detected, return None
            return None
                      
        self.slow = head            # Cycle Detected, return Node by Floyd's Tortoise Heir ALGO
        while self.slow != self.fast:
            self.slow = self.slow.next
            self.fast = self.fast.next
        return self.slow
         
    



