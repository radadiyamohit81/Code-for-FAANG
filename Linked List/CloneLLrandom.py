
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution1:
    def __init__(self):
        self.visitedHash = {}
    def copyRandomList(self, head):
        if head == None:
            return None
        if head in self.visitedHash:
            return self.visitedHash[head]
    
        node = Node(head.val, None, None)
        self.visitedHash[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node

class Solution2:
    def __init__(self):
        self.visitedHash = {}
        
    def createClone(self, node):
        if node != None:
            if node in self.visitedHash:
                return self.visitedHash[node]
            else:
                self.visitedHash[node] = Node(node.val, None, None)
                return self.visitedHash[node]
        return None
                
        
    def copyRandomList(self, head):
        if head == None:
            return None
        old_node = head
        new_node = Node(old_node.val, None, None)  # create a new node for every node and store
        self.visitedHash[old_node] = new_node 
        while old_node != None:
            new_node.random = self.createClone(old_node.random)
            new_node.next = self.createClone(old_node.next)
            old_node = old_node.next
            new_node = new_node.next
        return self.visitedHash[head]


class Solution3:
    # O[2N] Time
    # O[1] Space
    def copyRandomList(self, head):
        if head == None:
            return None
        
        # Insert a cloned node next to every Original Node
        old_ll = head
        while old_ll != None:
            new_ll = Node(old_ll.val, None, None)
            new_ll.next = old_ll.next
            old_ll.next = new_ll
            old_ll = new_ll.next

        # assign the random node for the Cloned Nodes
        ptr = head
        while ptr != None:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Un-Weiving the LL to the Original LL and Cloned LL
        old_ll = head
        result = new_ll = head.next
        while old_ll != None:
            old_ll.next = old_ll.next.next
            new_ll.next = new_ll.next.next if new_ll.next != None else None
            old_ll = old_ll.next
            new_ll = new_ll.next
        return result
        



d = {}
d[(1, 8)] = 50
for key in d:
    print(key[0])