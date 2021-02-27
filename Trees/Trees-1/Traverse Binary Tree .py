# Tree Defenition,
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:

    # Iterative Solution
    # time: O(N)
    # space: O(2N) in worst case
    def inorderTraversal(self, root):
        if root == None:
            return []

        stack, ans = [], []
        while root != None or stack != []:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.key)
            root = root.right
        return ans

    # Recursive Solution
    # time: O(N)
    # space: O(N) for result array + Recursive call stack
    def inorderTraversal(self, root):
        self.result = []
        self.inorder(root)
        return self.result
    
    def inorder(self, root):
        if not root:
            return 
        if root.left:
            self.inorder(root.left)
        self.result.append(root.val)
        if root.right:
            self.inorder(root.right)

# ===============================================================================

    # Iterative Solution --> 1 STACK APPROACH
    # time: O(N)
    # space: O(2N) for 2 arrays 
    def preOrderTraversal(self, root):
        if root == None:
            return None
        
        result = []
        st = []
        st.append(root)
        while st != []:
            root = st.pop()
            result.append(root.val)
            if root.right != None:
                st.append(root.right)
            if root.left != None:
                st.append(root.left)
        return result
            

    # Recursive Solution
    # time: O(N)
    # space: O(N) for result array + Recursive call Stack
    def preOrderTraversal(self, root):
        if not root:
            return []
        self.result = []
        self.preorder(root)
        return self.result
    
    def preorder(self, root):
        if not root:
            return
        self.result.append(root.val)
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)


# ===============================================================================
    # Iterative Solution --> 2 STACK APPROACH
    # time : O(N)
    # space : O(N), WORST CASE: stack2 holds all the node
    def postorderTraversal(self, root):
        if root == None:
            return []
        
        st1 = []
        st2 = []
        result = []
        st1.append(root)
        
        while st1 != []:
            root = st1.pop()
            if root.left:
                st1.append(root.left)
            if root.right:
                st1.append(root.right)
            st2.append(root.val)
        
        while st2 != []:
            result.append(st2.pop())
        return result

    # Recursive Solution
    # time : O(N)
    # space : O(N), WORST CASE: stack2 holds all the node
    def postorderTraversal(self, root):
        if not root:
            return []
        self.result = []
        self.postorder(root)
        return self.result
    
    def postorder(self, root):
        if not root:
            return
        if root.left:
            self.postorder(root.left)
        if root.right:
            self.postorder(root.right)
        self.result.append(root.val)
        

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
print("Preorder Traversal:",obj.preOrderTraversal(root = a))
    
    

        