
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# Like PREORDER DFS,
# O[N] Time, O[N] Space
class IterativeSolution:
    def flatten(self, head):
        if head == None:
            return None
        
        st = []
        st.append(head)
        previous = dummy = Node(-1, None, head, None)
        while st:
            current = st.pop()
            
            # establish DLL between current and previous nodes
            previous.next = current
            current.prev = previous
            
            if current.next != None:
                st.append(current.next)
            if current.child != None:
                st.append(current.child)
                current.child = None
            previous = current
            
        dummy.next.prev = None
        return dummy.next



class RecursiveSolution:
    def flatten(self, head):
        if not head:
            return head
        
        dummy = Node(-1, None, head, None)
        self.flattenDLL(head, dummy)
        
        dummy.next.prev = None
        return dummy.next
    
    def flattenDLL(self, current, previous):
        # BASE CASE
        if not current:
            return previous
        
        # LOGIC
        previous.next = current
        current.prev = previous
        

        tempNext = current.next
        tail = self.flattenDLL(current.child, current)
        current.child = None

        return self.flattenDLL(tempNext, tail)
        
        