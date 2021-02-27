# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def buildTree(self, inorder, postorder):
        if len(postorder) == 0 or len(inorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        
        postorderLeft = postorder[:index]
        postorderRight = postorder[index:len(postorder)-1]
        inorderLeft = inorder[:index]
        inorderRight = inorder[index+1:]
        root.left = self.buildTree(inorderLeft, postorderLeft)
        root.right = self.buildTree(inorderRight, postorderRight)
        return root

class Solution2:
    def buildTree(self, inorder, postorder):
        if len(postorder) == 0 or len(inorder) == 0:
            return None
        
        root = TreeNode(postorder.pop())
        index = inorder.index(root.val) 
        
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:len(postorder)])
        return root
    
        