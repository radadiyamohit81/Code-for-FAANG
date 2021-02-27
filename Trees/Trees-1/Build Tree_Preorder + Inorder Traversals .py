# time = O(N*N), list.index() --> O(N) and all elements of preorder are visited once
# space = O(N) for storing result Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder, inorder):
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(root.val)         # O[N] operation
        
        inL = inorder[:i]
        inR = inorder[i+1:]
        preL = preorder[1:i+1]
        preR = preorder[i+1:]
        root.left = self.buildTree(preL, inL)
        root.right = self.buildTree(preR, inR)
        return root


class Solution2:
    def buildTree(self, preorder, inorder):
        
        # BASE CASE
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        # LOGIC
        root = TreeNode(preorder.pop(0))
        k = inorder.index(root.key)                # list.index() ==> O(N) as it has to do a for loop over all elements in list
        
        root.left = self.buildTree(preorder, inorder[:k])
        root.right = self.buildTree(preorder, inorder[k+1:])
        return root


obj = Solution()
print(obj.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))