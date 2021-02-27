
# Time Complexity : O(N), where N is the length of word searched / inserted
# Space Complexity : O(N), For storing every character in a word, we have a TrieNode that uses an array of fixed size of 26
# Did this code successfully run on Leetcode : YES


class Solution:

    class TrieNode:
        def __init__(self):
            self.children = [None]*26
            self.word = ""
            
    def __init__(self):
        self.root = self.TrieNode()
    
    def insert(self, word):
        node = self.root
        for i in word:
            if node.children[ord(i) - ord('a')] == None:
                node.children[ord(i) - ord('a')] = self.TrieNode()
            node = node.children[ord(i) - ord('a')]
        node.word = word

    def longestWord(self, words):
        if words == [] or len(words) == 0:
            return -1
        for word in words:
            self.insert(word)    #forms the entire trie for all the words
            
        # Implementing BFS 
        q = [self.root]
        result=[]
        while q != []:
            size = len(q)
            for i in range(size):
                node = q.pop(0)   #popping every node
                for j in range(25, -1, -1):      #checking the children array
                    if node.children[j] != None and node.children[j].word != "":
                        q.append(node.children[j])
                        result.append(node.children[j].word)
        #print(result)
        return node.word
                    