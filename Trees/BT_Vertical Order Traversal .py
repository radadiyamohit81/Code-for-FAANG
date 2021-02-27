# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    # Time Complexity: O[N] Time
    # Space Complexity: O[N] Space 
    def __init__(self):
        self.d = {}
        
    def verticalOrder_BFS(self, root):
        if root == None:
            return []

        # ITERATIVE APPROACH, BFS
        q = []
        q.append((root, 0))
        minCol = float('inf')    # Avoiding the Complexity of SORTING HASH-MAP maintaining MIN & MAX
        maxCol = float('-inf')

        while q != []:
            node, col = q.pop(0)
            if col not in self.d:
                self.d[col] = [node.val]
                minCol = min(minCol, col)
                maxCol = max(maxCol, col)
            else:
                self.d[col].append(node.val)     # we need not SORT in rows as BFS takes care of it
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))

        
        result = []
        for col in range(minCol, maxCol+1):
            if col in self.d:
                result.append(self.d[col])
        return result

    #------------------------------------------------------------------
    # DFS SOLUTION,
    # O[ W * H logH ] Time
    # O[ N ] Space 
    # W -> no.of.columns, H -> height of Tree, N -> no.of.nodes in Tree

    def verticalOrder_DFS(self, root):
        if root == None:
            return []

        self.result = {}
        self.minCol = float('inf')     # Avoiding the Complexity of SORTING HASH-MAP maintaining MIN & MAX
        self.maxCol = float('-inf')
        self.helper(root, 0, 0)

        print(self.result)
        ans = []
        for col in range(self.minCol, self.maxCol+1):                 # O[W] Time
            
            self.result[col].sort(key = lambda x: x[1])          # SORT based on ROW, O[H logH]
             
            colVals = []
            for val, row in self.result[col]:
                colVals.append(val)
            ans.append(colVals) 
        return ans


    def helper(self, node, col, row):
        # BASE CASE
        if node == None:
            return 
        
        # LOGIC
        if col in self.result:
            self.result[col].append( [node.val, row] )
        else:
            self.minCol = min(self.minCol, col)
            self.maxCol = max(self.maxCol, col)
            self.result[col] = [[node.val, row]]

        if node.left:                           # the order of rows is not Maintained in DFS, so we need to sort based on the rows later on
            self.helper(node.left, col-1, row+1)
        if node.right:
            self.helper(node.right, col+1, row+1)