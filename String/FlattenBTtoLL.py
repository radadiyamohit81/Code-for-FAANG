class Node:
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # O[N] Time, O[N] Recursive call Stack space
    
    def flatten(self, root):
        # BASE CASE
        if root == None or root.left == None and root.right == None:
            return

        # LOGIC
        self.flatten(root.left)

        # detach the right node and attach the leftmost node
        temp = root.right
        root.right = root.left
        root.left = None

        # attach the detached right node to the end
        while root.right:
            root = root.right
        root.right = temp

        self.flatten(root.right)

