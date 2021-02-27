
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Solution:
    # Tree Traversals: DFS (Inorder, Preorder, Postorder)

    # time: O(N), space: O(N)
    def inorderT_iterative(self, root):
        if root == None:
            return []

        stack = []
        ans = []

        while root != None or stack != []:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root= root.right
        return ans
    
    # time: O(N), space: O(N) for recursive call stack
    def inorderT_recursive(self, root):
        if root == None:
            return []

        ans = []
        self.helper(root, ans)
        return ans
    
    def helper(self, root, ans):
        if root:
            self.helper(root.left, ans)
            ans.append(root.val)
            self.helper(root.right, ans)

    #----------------------------------------------------------
    # time: O(N) space: O(N)
    def preorderT_iterative(self, root):
        if root == None:
            return []

        stack = [root]
        ans = []

        while stack != []:
            root = stack.pop()
            ans.append(root.val)
            if root.right != None:
                stack.append(root.right)
            if root.left != None:
                stack.append(root.left)
        return ans
    
    # time: O(N) space: O(N) for recursive call stack
    def preorderT_recursive(self, root):
        if root == None:
            return []

        ans = []
        self.helper(root, ans)
        return ans
    
    def helper(self, root, ans):
        if root != None:
            ans.append(root.val)
            self.helper(root.left, ans)
            self.helper(root.right, ans)

    #----------------------------------------------------------
    def postorderT_iterative(self, root):
        if root == None:
            return []
        
        stack1 = [root]
        stack2 = []
        ans = []

        while stack1 != []:
            root = stack1.pop()
            if root.left != None:
                stack1.append(root.left)
            if root.right != None:
                stack1.append(root.right)
            stack2.append(root.val)
        while stack2 != []:
            ans.append(stack2.pop())
        return ans

    # time: O(N), space: O(2N)
    def postorderT_recursive(self, root):
        if root == None:
            return []

        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if root:
            self.helper(root.left, ans)
            self.helper(root.right, ans)
            ans.append(root.val)


#==================================================================================================================
# BST (inorder Recursive Soln, Iterative Soln)

    # time: O(N), space: O(N)
    def BST_recursive(self, root): 
        return self.helper(root, None, None)

    def helper(self, root, min, max):
        # base case
        if root == None:
            return True
        if min != None and root.val <= min:
            return False
        if max != None and root.val >= max:
            return False

        # logic
        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)

    # time: O(N), space: O(N) worst case
    def BST_iterative(self, root):
        if root == None:
            return True
        
        stack = []
        previous = None

        while root != None or stack != []:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if previous != None and root.val <= previous.val:
                return False
            previous = root
            root = root.right
        return True

# ================================================================================================================


    # Build Tree 
    def buildTree(self, preorder, inorder):
        if preorder == None:
            return None

        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
                break
        inLeft = inorder[:i]
        inRight = inorder[i+1:]
        preLeft = preorder[1:i+1]
        preRight = preorder[i+1:]
        root.left = self.buildTree(preLeft, inLeft)
        root.right = self.buildTree(preRight, inRight)
        return root

    def buildTree(self, inorder, postorder):
        if postorder == []:
            return None
        
        root = TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
                break
        inLeft = inorder[:i]
        inRight = inorder[i+1:]
        postLeft = postorder[:i]
        postRight = postorder[i : len(postorder)-1]
        root.left = self.buildTree(inLeft, postLeft)
        root.right = self.buildTree(inRight, postRight)
        return root

        
# ================================================================================================================

    # Recursive Solution
    def sum2Leaf(self, root):
        return self.helper(root, 0)
    def helper(self, node, value):
        # base case
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return value*10+node.val

        # Logic
        return self.helper(node.left, value*10+node.val) + self.helper(node.right, value*10+node.val) 
    
    # Iterative Solution
    def sum2Lef(self, root):
        if root == None:
            return 0
        
        stack = []
        stack.append((root, 0))
        result = 0

        while stack != []:
            p = stack.pop()
            node = p[0]
            value = p[1]

            if node != None:
                value = value*10 + node.val
                if node.left == None and node.right == None:
                    result += value
                stack.append((node.right, value))
                stack.append((node.left, value))
        return result
# ================================================================================================================
 
    # DFS Iterative APPROACH
    # time : O(N)
    # space = O(2H)

    def isSymmetric(self, root):
        if root == None:
            return True
        
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        
        while stack != []:
            
            r = stack.pop()
            l = stack.pop()
            
            if l == None and r == None:
                    continue
            if l != None and r != None and l.val == r.val:
                stack.append(l.left)
                stack.append(r.right)
                stack.append(l.right)
                stack.append(r.left)
            if l == None or r == None or l.val != r.val:
                return False
        return True
    
    # BFS Iterative Approach
    # time : O(N)
    # space: O(N)

    def isSymmetric(self, root):
        if root == None:
            return True
        
        q = []
        q.append((root.left, root.right))
        
        while q != []:
            t = q.pop()
            l = t[0]
            r = t[1]
            if l == None and r == None:
                continue
            
            if l != None and r != None and l.val == r.val:
                q.append((l.left, r.right))
                q.append((l.right, r.left))
            if l == None or r == None or l.val != r.val:
                return False
        return True

# ================================================================================================================
                
            
        
                    
                



a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(25)
a.left.left = TreeNode(13)
a.left.right = TreeNode(18)
a.right.left = TreeNode(24)
a.right.right = TreeNode(27)
a.left.left.left =  TreeNode(10)
a.left.left.right = TreeNode(14)
a.left.right.left = TreeNode(16)
a.left.right.right = TreeNode(19)

obj = Solution()
print("BST_iterative soln: ",obj.BST_iterative(a))
print("BST_recursiveive soln: ",obj.BST_recursive(a))
        


