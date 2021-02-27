
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Solution:

    # DFS Recursive
    # time : O(N)
    # space : O(1) + O[H] Recursive call stack 
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x_parent = None
        self.y_parent = None
        self.x_depth = None
        self.y_depth = None
        self.dfs(root, x, y, 0, None)
    
        if self.x_depth == self.y_depth and self.x_parent != self.y_parent:
            return True
        return False
    
    def dfs(self, root, x, y, depth, parent):
        # BASE CASE
        if root == None:
            return
        if root.val == x:
            self.x_depth = depth
            self.x_parent = parent
        if root.val == y:
            self.y_depth = depth
            self.y_parent = parent
            
        # LOGIC
        self.dfs(root.left, x, y, depth+1, root)
        self.dfs(root.right, x, y, depth+1, root)
        
        
        

    # DFS Iterative, Inorder Traversal
    # O(N) Time
    # O(N) Space
    def isCousins(self, root, x, y):
        if x == None or y == None or root == None:
            return False
        # nodes are cousins if x_depth == y_depth and x_parent != y_parent
        depth = 0
        x_depth = -1
        y_depth = -1
        x_parent = -1
        y_parent = -1
        
        stack = []
        while root != None or stack != []:
            while root:
                stack.append((root, depth))
                if root.left != None and root.left.val == x:
                    x_parent, x_depth = root, depth + 1
                elif root.left != None  and root.left.val == y:
                    y_parent, y_depth = root, depth + 1
                root = root.left
                depth += 1
                
            root, depth = stack.pop()
            if root.right != None and root.right.val == x:
                x_parent, x_depth = root, depth + 1
            elif root.right != None and root.right.val == y:
                y_parent, y_depth = root, depth + 1
            root = root.right
            depth += 1
        
        if x_depth == y_depth and x_parent != y_parent:
            return True
        return False


# ============================================================================================================
    # BFS Solution
    # time : O(N)
    # space : O(2K), WORST CASE: q holds all the nodes in the last Level 
    def cousinsTree(self, root, x, y):
        if x == None or y == None or root == None:
            return False

        q = [root]
        while q != []:
            size = len(q)
            leveList = []                   # levelList : not necessary
            for i in range(size):
                root = q.pop(0)
                leveList.append(root.key)
                if root.left != None and root.right != None:
                    if (root.left.key == x and root.right.key == y) or (root.left.key == y and root.right.key == x):
                        return False
                if root.left != None:
                    q.append(root.left)
                if root.right != None:
                    q.append(root.right)
            if x in leveList and y in leveList:
                return True

    # BFS Solution
    # time : O(N)
    # space : O(K), WORST CASE: q holds all the nodes in the last Level
    def cousinsTree(self, root, x, y):
        if x == None or y == None or root == None:
            return False

        q = [root]
        while q != []:
            size = len(q)
            x_isFound = False
            y_isFound = False              
            for i in range(size):
                root = q.pop(0)
                if root.key == x:
                    x_isFound = True
                if root.key == y:
                    y_isFound = True

                if root.left != None and root.right != None:
                    if root.left.key == x and root.right.key == y:
                        return False
                    if root.left.key == y and root.right.key == x:
                        return False
                
                if root.left != None:
                    q.append(root.left)                    
                if root.right != None:
                    q.append(root.right)

            if x_isFound and y_isFound:
                return True
        return False
                    


        
            
        




a = TreeNode(3)
a.left = TreeNode(9)
a.left.left = TreeNode(1)
a.left.right = TreeNode(0)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

obj = Solution()
print(obj.cousinsTree(root=a, x=1, y=7))