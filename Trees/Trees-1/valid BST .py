
# ITERATIVE SOLUTION / DFS APPROACH

# BETTER than creating a list out of  the inorder traversal of tree and then checking if it is in increasing order
# this solution returns False immediately when a breach happens.

# Time Complexity: O(N), WORST CASE of perfect BST, it has to traverse through all nodes to return True
# Space Complexity: No additional space, except the Recursive stack

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class Solution:
    def isValidBST(self, root):
        if root == None:
            return True
        return self.helper(root, None, None)  
    def helper(self, root, minn, maxx):
        # BASE CASE
        if not root:
            return True
        if minn != None and root.val <= minn:
            return False
        if maxx != None and root.val >= maxx:
            return False

        # LOGIC
        return self.helper(root.left, minn, root.val) and self.helper(root.right, root.val, maxx)

a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(25)
a.left.left = TreeNode(13)
a.left.right = TreeNode(18)
a.right.left = TreeNode(24)
a.right.right = TreeNode(27)
a.left.left.left = TreeNode(10)
a.left.left.right = TreeNode(14)
a.left.right.left = TreeNode(16)
a.left.right.right = TreeNode(19)

obj = Solution()
print(obj.isValidBST(root = a))



# INORDER TRAVERSAL ITERATIVE SOLUTION
# Time Complexity: O(N)
# Space Complexity: O(N) for 1 stack 

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class Solution2:
    def inorder_isValidBST(self, root):
        if root == None:
            return True
        
        st = []
        previous = None
        while root != None or st != []:
            while root != None:
                st.append(root)
                root = root.left
            root = st.pop()
            if previous != None and root.val <= previous:
                return False
            
            previous = root.val
            root = root.right
        return True


a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(25)
a.left.left = TreeNode(13)
a.left.right = TreeNode(18)
a.right.left = TreeNode(24)
a.right.right = TreeNode(27)
a.left.left.left = TreeNode(10)
a.left.left.right = TreeNode(14)
a.left.right.left = TreeNode(16)
a.left.right.right = TreeNode(19)

obj = Solution()
print(obj.inorder_isValidBST(root=a))





            
        











