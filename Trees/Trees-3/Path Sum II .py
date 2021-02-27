
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    # RECURSIVE SOLUTION
    # time : O(N)
    # space : O(H) + Recursive Call Stack 

    def pathSum2(self, root, target):
        self.result = []
        self.helper(root, target, [], 0)
        return self.result

    def helper(self, root, target, temp, value):

        # BASE CASE                 
        if root.left == None and root.right == None and value+root.val == target:  
            self.result.append(temp + [root.val])       ########## temp.append(root.val) ---> ERROR
            return             
            
        # LOGIC
                                ########## temp.append(root.val) ---> ERROR 
        if root.left != None:
            self.helper(root.left, target, temp + [root.val], value+root.val)
        if root.right != None:
            self.helper(root.right, target, temp + [root.val], value+root.val)



    # ============================================================================================================

    # ITERATIVE DFSSOLUTION
    # time : O(N)
    # space : O(H) 

    def pathSum2(self, root, target):
        if root == None:
            return []
        
        st = []
        st.append((root, [root.val], root.val))
        result = []
        
        while st != []:
            node, temp, summ = st.pop()
            if node.left == None and node.right == None:
                if summ == target:
                    result.append(temp)
                continue
            
            if node.left:
                st.append((node.left, temp+[node.left.val], summ + node.left.val))
            if node.right:
                st.append((node.right, temp+[node.right.val], summ + node.right.val))
        
        return result
        
            
    def pathSum2(self, root, target):
        if root == None:
            return []
        
        st = []
        st.append((root, [root.val]))
        result = []
        
        while st != []:
            node, temp = st.pop()
            if node.left == None and node.right == None:
                summ = sum(temp)
                if summ == target:
                    result.append(temp)
                continue
            
            if node.left:
                st.append((node.left, temp+[node.left.val]))
            if node.right:
                st.append((node.right, temp+[node.right.val]))
        
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
print(obj.pathSum2(root = a, target=72))
