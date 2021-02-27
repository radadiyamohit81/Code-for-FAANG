# Time Complexity : O(N), where N is the length of word searched / inserted
# Space Complexity : O(N), For storing every character in a word, we have a TrieNode that uses an array of fixed size of 26
# Did this code successfully run on Leetcode : YES


class Trie:
    class TrieNode:
        def __init__(self):
            self.isEnd = False
            self.children = [None]*26
        
        
    def __init__(self):
        self.root = self.TrieNode()

        
    def insert(self, word):
        node = self.root

        for i in word:
            # if there is no node for the i character in trie,
            if node.children[ord(i) - ord('a')] == None:   
                node.children[ord(i) - ord('a')] = self.TrieNode()
            node = node.children[ord(i) - ord('a')]
        node.isEnd = True
            

    def search(self, word):
        node = self.root
        
        for i in word:
            if node.children[ord(i) - ord('a')] != None:
                node = node.children[ord(i) - ord('a')]
            else:
                return False
        if node.isEnd == True:
            return True
        else:
            return False
                

    def startsWith(self, prefix):
        node = self.root
        
        for i in prefix:
            if node.children[ord(i) - ord('a')] != None:
                node = node.children[ord(i) - ord('a')]
            else:
                return False
        return True
         
    
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)