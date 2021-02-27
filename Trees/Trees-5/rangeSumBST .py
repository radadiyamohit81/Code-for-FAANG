class Solution:
    def rangeSumBST(self, root, L, R):
        # CONTROLLED DFS, Inorder
        result = 0
        stack = []
        while root != None or stack != []:
            while root != None:
                stack.append(root)
                if root.val < L:
                    break
                root = root.left
            root = stack.pop()
            if root.val >= L and root.val <= R:
                result += root.val
            if root.val > R:
                break
            root = root.right
        return result

    def rangeSumBST(self, root, L, R):     #ITERATIVE dfs, Inorder
        result = 0
        stack = []
        while root != None or stack != []:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val >= L and root.val <= R:
                result += root.val
            root = root.right
        return result
    
    def rangeSumBST(self, root, L, R):      #RECURSIVE dfs
        self. result = 0
        self.helper(root, L, R)
        return self.result
    def helper(self, root, L, R):
        if root == None:
            return
        self.helper(root.left, L, R)
        if root.val >= L and root.val <= R:
            self.result += root.val
        self.helper(root.right, L, R)

    