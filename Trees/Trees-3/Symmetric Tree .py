
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:

    # DFS Recursive Solution
    # time : O(N)
    # space = O(1) + Recursive Call Stack
    def symmetricTree(self, root):
        if root == None:
            return True
        
        return self.symmetryCheck(root.left, root.right)
        
    def symmetryCheck(self, left, right):
        # BASE CASE
        if left == None and right == None:
            return True
        if left == None or right == None or left.val != right.val:
            return False
        
        # LOGIC
        return self.symmetryCheck(left.left, right.right) and self.symmetryCheck(left.right, right.left)


    # DFS Iterative APPROACH
    # time : O(N)
    # space = O(2H)

    def isSymmetric(self, root):
        if root == None:
            return True
        
        st = []
        st.append((root.left, root.right))
        while st != []:
            left, right = st.pop()
            if left == None and right == None:
                continue
            if left == None or right == None or left.val != right.val:
                return False
            
            st.append((left.left, right.right))
            st.append((left.right, right.left))
        return True


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
            if l == None or r == None or l.val != r.val:
                return False
            stack.append(l.left)
            stack.append(r.right)
            stack.append(l.right)
            stack.append(r.left)
        return True

    # BFS (Iterative) Solution
    # time : O(N)
    # space = O(H), H is height of Tree
    def symmetricTreeBFS(self, root):
        if root == None:
            return True
        q = [(root.left, root.right)]
        while q != []:
            left, right = q.pop(0)
            if left == None and right == None:
                continue
            if left == None or right == None or left.key != right.key:
                return False
            q.append((left.left, right.right))
            q.append((left.right, right.left))
        return True




a = TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(15)
a.left.left = TreeNode(13)
a.left.right = TreeNode(14)
a.right.left = TreeNode(14)
a.right.right = TreeNode(13)


obj = Solution()
print(obj.symmetricTreeBFS(root = a))