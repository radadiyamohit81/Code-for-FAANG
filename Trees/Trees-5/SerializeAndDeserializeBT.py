# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec1:         
    # DFS Approach on Serialization and De-Serialization
    # O[N] Time
    # O[N] Space
    def serialize(self, root):
        if root == None:
            return []
        return (self.dfs_serialize(root, []))
    def dfs_serialize(self, root, data):
        # BASE CASE
        if root == None:
            data.append('None,')
            return
        else:
            data.append(root.val)
            self.dfs_serialize(root.left, data)
            self.dfs_serialize(root.right, data)
        return data

    def deserialize(self, data):
        if data == []:
            return None
        if data[0] == 'None,':
            data.pop(0)
            return None
        
        root = TreeNode(data[0])
        data.pop(0)
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Codec2:
    def serialize(self, root):     # BFS Level-Order Traversal (q) Iterative
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
        root = TreeNode(int(lst[0]))
        index = 1
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
            

#=========================================================================

