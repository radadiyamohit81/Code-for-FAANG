# Definition for a Node.
class Node:
    def __init__(self, val= 0, left= None, right= None, next= None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # O[N] Time
    # O[1] Space
    def connect(self, root):   #Iterative Approach
        if root == None:
            return None
        # Maintain a pointer TEMP of the left most node at every level
        # copy the TEMP at every level to another variable and move on its next pointer to fill all the next pointers on the next level
        temp = root
        while temp != None:
            current = temp
            # current keeps moving from the leftmost node on the level on its next pointer to the None pointer at the end of that level
            # At every current we will be filling the next pointers on the next row
            while current != None:
                if current.right != None:
                    current.left.next = current.right
                if current.next != None and current.right != None:
                    current.right.next = current.next.left
                current = current.next
            temp = temp.left
        return root

    def connect(self, root):    #Recursive Approach
        if root == None:
            return None
        self.helper(root.left, root.right)
        return root

    def helper(self, left, right):
        # BASE CASE
        if left == None or right == None:
            return 
        # LOGIC
        left.next = right
        self.helper(left.left, left.right)
        self.helper(left.right, right.left)
        self.helper(right.left, right.right)