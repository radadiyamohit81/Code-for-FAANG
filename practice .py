class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Solution:
    def inorder_Recursive(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left)
            res.append(root.key)
            self.helper(root.right)

    def inorder_Iterative(self, root):
        st = []
        res = []

        while st != None or root != None:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            res.append(root)
            root = root.right
        return res

    def validBST(self, root):
        previous = None
        st = []

        while root != None or st != []:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            if previous != None and root.val <= previous:
                return False
            previous = root.val
            root = root.right
        return True

    #------------------------------------------------------------------------------
    def preorder_Recursive(self, root):
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)
    
    def preorder_Iterative(self, root):
        st = [root]
        res = []
        while st != []:
            root = st.pop()
            res.append(root.val)
            if root.right != None:
                st.append(root.right)
            if root.left != None:
                st.append(root.left)
        return res

    #------------------------------------------------------------------------------
    def postorder_Recursive(self, root):
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            self.helper(root.right, res)
            res.append(root.val)
    
    def postorder_Traversal(self, root):
        if root == None:
            return []
        res = []
        st1 = [root]
        st2 = []

        while st1 != []:
            root = st1.pop()
            if root.left != None:
                st1.append(root.left)
            if root.right != None:
                st1.append(root.right)
            st2.append(root.val)
        
        while st2 != []:
            res.append(st2.pop())
        return res
        
    #------------------------------------------------------------------------------
    def buildTree(self, preorder,  inorder):    
        if preorder == []:
            return None

        root = TreeNode(preorder[0])
        i = inorder.index(root.val)
        inL = inorder[:i]
        inR = inorder[i+1:]
        preL = preorder[1:i+1]
        preR = preorder[i+1:]

        root.left = self.buildTree(preL, inL)
        root.right = self.buildTree(preR, inR)
        return root

    def buildTree(self, inorder, postorder):      
        if postorder == []:
            return None

        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        inL = inorder[:i]
        inR = inorder[i+1:]
        postL = postorder[:i]
        postR = postorder[i:len(postorder)-1]

        root.left = self.buildTree(inL, postL)
        root.right = self.buildTree(inR, postR)
        return root

    #------------------------------------------------------------------------------
    def rootToLeaf(self, root):   #Iterative
        result = 0
        stack = []
        stack.append((root, 0))

        while stack != []:
            tup = stack.pop()
            node = tup[0]
            value = tup[1]
            if node != None:
                value = value*10 + node.val
                if node.left == None and node.right == None:
                    result += value
                    continue
                stack.append((node.left, value))
                stack.append((node.right, value))
        return result


    def rootToLeaf(self, root):   #Recursive
        return self.helper(root, 0)

    def helper(self, node, value):
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return value*10+node.val
        return self.helper(node.left, value*10+node.val) + self.helper(node.right, value*10+node.val)

    #------------------------------------------------------------------------------
    def pathSum(self, root, target):     # Iterative
        if root == None:
            return []
        result = []
        stack = []
        stack.append((root, []))

        while stack != []:
            node, lst = stack.pop()
            if node.left == None and node.right == None:
                lst.append(node.val)
                summ = 0
                for num in lst:
                    summ += num
                if summ == sum:
                    result.append(lst)
            if node.left != None:
                stack.append((node.left, lst+[node.val]))
            if node.right != None:
                stack.append((node.right, lst+[node.val]))
        return result

    #------------------------------------------------------------------------------
    def pathSum(self, root, target):     # Recursive
        if root == None:
            return []
        
        self.result = []
        self.helper(root, sum, [], 0)
        return self.result

    def helper(self, root, target, lst, value):
        # BASE CASE
        if root == None:
            return 
        if root.left == None and root.right == None and value+root.val == target:
            lst.append(root.val)
            self.result.append(lst)
    
        #LOGIC
        self.helper(root.left, target, lst+[root.val], value+root.val)
        self.helper(root.right, target, lst+[root.val], value+root.val)

    #------------------------------------------------------------------------------
    #DFS (ITERATIVE)
    def symmetricTree(self, root):
        if root == None:
            return True
        stack = []
        stack.append((root.left, root.right))

        while stack != []:
            left, right = stack.pop()
            if left == None and right == None:
                continue
            if left == None or right == None or left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
    

    #DFS (RECURSIVE)
    def symmetricTree(self, root):
        if root == None:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        #BASE CASE
        if left == None and right == None:
            return True
        if left == None or right == None or left.val != right.val:
            return False
        
        #LOGIC
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)

    #BFS 
    def symmetricTree(self, root):
        if root == None:
            return True
        q = []
        q.append((root.left, root.right))

        while q != []:
            left, right = q.pop(0)
            if left == None and right == None:
                continue
            if left == None or right == None or left.val != right.val:
                return False
            q.append((left.left, right.left))
            q.append((left.right, right.right))
        return True
            
    #------------------------------------------------------------------------------
    def kthSmallest(self, root, k):    #Iterative Solution O(N) Time + O(H) Space
        if root == None:
            return None
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kthSmallest(self, root, k):    #Recursive Solution O(N) Time + Recursive call stack space
        if root == None:
            return None
        self.result = None
        self.count = k
        self.helper(root)
        return self.result
    def helper(self, root):  #Inorder Traversal
        # LOGIC
        if root.left:
            self.helper(root.left)
        self.count -= 1
        if self.count == 0:
            self.result = root.val
            return
        if root.right:
            self.helper(root.right)

    #------------------------------------------------------------------------------
    def lowestCommonAncestor_BST(self, root, p, q):    #Iterative Solution
        if root == None:
            return None
        
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

    def lowestCommonAncestor_BST(self, root, p, q):      #Recursive Solution
        if root == None:
            return None
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor_BST(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor_BST(root.right, p, q)
        else:
            return root

    #------------------------------------------------------------------------------
    def lowestCommonAncestor_BT(self, root, p, q):
        # BASE CASE
        if root == None or root == p or root == q:
            return root

        # LOGIC
        left = self.lowestCommonAncestor_BT(root.left, p, q)
        right = self.lowestCommonAncestor_BT(root.right, p, q)
        if left != None and right != None:
            return root
        if left != None:
            return left
        if right != None:
            return right

    #------------------------------------------------------------------------------
    def connect(self, root):    #Iterative Approach
        if root == None:
            return None
        temp = root
        while temp != None:
            current = temp
            while current != None:
                if current.left != None:
                    current.left.next = current.right
                if current.right != None and current.next != None:
                    current.right.next = current.next.left
                current = current.next
            temp = temp.left
        return root

    def connect(self, root):    #Recursive Approach
        if root == None:
            return None
        self.helper(root.left, root.right)
        return root
    def helper(self, left, right):
        if left == None or right == None:
            return 
        left.next = right
        self.helper(left.left, left.right)
        self.helper(left.right, right.left)
        self.helper(right.left, right.right)

    #------------------------------------------------------------------------------
    def recoverTree(self, root):         
        # Inorder Traversal using previous pointer to find the two breaches (isValid BST)
        # first => previous value at first breach 
        # middle => 1st breach root val
        # last => 2nd breach root val (can be None)
        
        stack = []
        previous = None
        first = None
        middle = None
        last = None

        while root != None or stack != []:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if previous != None and previous.val > root.val:
                if first == None:
                    first = previous
                    middle = root
                else:
                    last = root
            previous = root
            root = root.right
        
        # SWAPPING THE NODES TO RECOVER THE BST
        if last != None:        # if breaches happens at different subtree
            temp = first.val
            first.val = last.val
            last.val = temp
        else:
            temp = first.val
            first.val = middle.val
            middle.val = temp

    #------------------------------------------------------------------------------
    def rangeSumBST(self, root, L, R):     #ITERATIVE dfs
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
        if root:
            self.helper(root.left, L, R)
            if root.val >= L and root.val <= R:
                self.result += root.val
            self.helper(root.right, L, R)

    def rangeSumBST(self, root, L, R):
        # CONTROLLED DFS
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

    #------------------------------------------------------------------------------
    def serialize(self, root):     # BFS (q) Iterative
        if root == None:
            return ''
        q = [root]
        result = ''
        while q != []:
            l = len(q)
            for i in range(l):
                current = q.pop(0)
                if current == None:
                    result += 'None,'
                    continue
                result += str(current.val) + ','
                q.append(current.left)
                q.append(current.right)
        return result

    def deserialize(self, data):
        if data == '':
            return None
        lst = data.split(',')
        index =0
        root = TreeNode(int(lst[index]))
        index += 1
        q = [root]
        while index < len(lst) and q != []:
            current = q.pop(0)
            if lst[index] != 'None' and index < len(lst):
                current.left = TreeNode(int(lst[index]))
                q.append(current.left)
            index += 1
            if lst[index] != 'None' and index < len(lst):
                current.right = TreeNode(int(lst[index]))
                q.append(current.right)
            index += 1
        return root

    def serialize(self, root): # DFS (stack) Iterative
        if root == None:
            return ''
        result = ''
        stack = [root]
        while stack != []:
            current = stack.pop(0)
            if current == None:
                result += 'None,'
                continue
            result += str(current.val)
            stack.append()

    #------------------------------------------------------------------------------







        
            

