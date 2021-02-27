class Solution:
    # O[N] Time , BEST CASE (balanced BST): O[log N] 
    # O[1] Space
    def lowestCommonAncestor_BST(self, root, p, q):    #Iterative Solution
        if root == None:
            return None
        
        while root != None:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


    # O[N] Time , BEST CASE (balanced BST): O[log N] 
    # O[H] Recursive Call-Stack Space
    def lowestCommonAncestor_BST(self, root, p, q):      
        if root == None:
            return None
        return self.findCommonAncestor(root, p, q)
    
    def findCommonAncestor(self, root, p, q):
        # BASE CASE
        if root == None:
            return None
        
        # LOGIC
        if p.val < root.val and q.val < root.val:
            return self.findCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.findCommonAncestor(root.right, p, q)
        else:
            return root
        
        
        