class Solution:
    def recoverTree(self, root):         
        # Inorder Traversal using previous pointer to find the two breaches (isValid BST)
        # first => previous value at first breach 
        # second => 1st breach root val
        # third => 2nd breach root val (can be None)

        # if third != None:  swap(first, third) else: swap(first, second)
        
        
        if root == None:
            return None
        
        previous = None
        st = []
        first = None
        second = None
        third = None
        while root != None or st != []:
            while root != None:
                st.append(root)
                root = root.left
            root = st.pop()
            if previous != None and previous.val >= root.val:
                # BREACH HAPPENING
                if first == None:
                    first = previous
                    second = root
                else:                # if breaches happens at different branch of Tree
                    third = root
    
            previous = root
            root = root.right
            
        if third == None:
            self.swap(first, second)
        else:
            self.swap(first, third)
    
    def swap(self, node1, node2):
        temp = node1.val
        node1.val = node2.val
        node2.val = temp