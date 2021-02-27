
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive solution
    # time: O(N)
    # space: O(1) + Recursion call stack
    def sumNumbers(self, root):
        if root == None:
            return 0
        
        self.result = 0
        self.helper(root, 0)
        return self.result
    
    def helper(self, root, val):
        # BASE CASE
        if root.left == None and root.right == None:
            self.result += val*10+root.val
            return
        
        # LOGIC
        if root.left:
            root.left = self.helper(root.left, val*10+root.val)
        if root.right:
            self.right = self.helper(root.right, val*10+root.val)
        
            
 
class Solution2:
    # Iterative solution
    # time: O(N)
    # space: O(H) ,H: height of tree
    def sumNumbers(self, root):
        if root == None:
            return 0
        
        st = [(root, 0)]
        result = 0
        
        while st != []:
            node, val = st.pop()
            
            # BASE CASE
            if node.left == None and node.right == None:
                result += val*10+node.val
                
            # LOGIC
            if node.left != None:
                st.append((node.left, val*10+node.val))
            if node.right != None:
                st.append((node.right, val*10+node.val))
        return result 


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
print(obj.sum_Root_to_Leaf(root = a))