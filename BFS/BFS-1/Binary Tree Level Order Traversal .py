
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    # BFS / Level Order Traversal
    # time : O(N)
    # space : O( no.of.nodes at the LAST LEVEL )
      
    def levelOrderTraversal(self, root):
        if root == None:
            return []
        
        result = []
        q = []
        q.append(root)
        while q != []:
            level_size = len(q)
            level_list = []
            for i in range(level_size):
                root = q.pop(0)
                level_list.append(root.val)
                if root.left != None:
                    q.append(root.left)
                if root.right != None:
                    q.append(root.right)
            result.append(level_list)
        return result
                



a = TreeNode(3)
a.left = TreeNode(9)
a.left.left = TreeNode(1)
a.left.right = TreeNode(0)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

obj = Solution()
print(obj.levelOrderTraversal(root=a))