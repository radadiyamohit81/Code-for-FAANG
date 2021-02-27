class Solution:
    # O[N] Time
    # O[N] Space
    def lowestCommonAncestor_BT(self, root, p, q):
        # BASE CASE
        if root == None:
            return None        
        if root == p or root == q:
            return root
        
        # LOGIC
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None:
            return root
        if left != None:
            return left
        if right != None:
            return right