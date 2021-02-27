class DLLnode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.previous = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        
        # cache ===> { KEY : DLL(order of elements accessed, LRU at Tail)}
        # storing every Node to its Key in cache HashMap
        # Initiate a DLL to maintain the order of all Keys Accessed, LRU near Tail
        
        self.head = DLLnode(-1, -1)
        self.tail = DLLnode(-1, -1)
        self.head.next = self.tail
        self.tail.previous = self.head
        
    def addToHead(self, node):
        node.next = self.head.next
        self.head.next = node
        node.previous = self.head
        node.next.previous = node
        
    def deleteNode(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
        
    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # once accessed a node, it should be removed from its position and added to the head
        self.deleteNode(node)
        self.addToHead(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            # we accessed the node => delete the node from DLL and add it to Head of DLL
            self.deleteNode(node)
            self.addToHead(node)
        else:
            node = DLLnode(key, value)
            if self.size < self.capacity:
                self.cache[key] = node
                self.addToHead(node)
                self.size += 1
            elif self.size == self.capacity:
                del self.cache[self.tail.previous.key]
                self.deleteNode(self.tail.previous)
                self.cache[key] = node
                self.addToHead(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)