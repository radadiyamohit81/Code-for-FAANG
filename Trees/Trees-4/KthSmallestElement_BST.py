class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Inorder Traversal (Recursive Solution)
    # O(N) time
    # O(N) space

    def kthSmallest_BST(self, root, k):
        if root == None:
            return -1
        self.result = []
        self.inorder(root)
        return self.result[k-1]
    
    def inorder(self, root):
        # BASE CASE
        if root == None:
            return
        # LOGIC
        if root.left:
            self.inorder(root.left)
        self.result.append(root.val)
        if root.right:
            self.inorder(root.right)

    #------------------------------------------------------------------------------
    def kthSmallest(self, root, k):    #Iterative Solution O(N) Time + O(H) Space  (INORDER TRAVERSAL)
        if root == None:
            return -1
        
        st = []
        while root != None or st != []:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            k -=1
            if k == 0:
                return root.val
            root = root.right
    
    #------------------------------------------------------------------------------
    def kthSmallest(self, root, k):    #Recursive Solution O(N) Time + Recursive call stack space
        self.res = None
        self.k = k
        self.helper(root)
        return self.res
        

    def helper(self, root):
        # BASE CASE
        if root == None:
            return 

        # LOGIC
        self.helper(root.left)

        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        
        self.helper(root.right)




