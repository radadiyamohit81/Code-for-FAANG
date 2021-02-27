class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.frequency = 1
        self.next = None
        self.previous = None

class DLList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.size = 0
        self.head.next = self.tail
        self.tail.previous = self.head
    
    def addToHead(self, node):
        node.next = self.head.next
        self.head.next = node
        node.previous = self.head
        node.next.previous = node
        self.size += 1

    def removeNode(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
        self.size -= 1 
    
    def removeFromTail(self):
        tailPrevious = self.tail.previous
        self.removeNode(tailPrevious) 
        return tailPrevious
    
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.nodeMap = {}
        self.freqMap = {}
        self.minFreq = 0

    def get(self, key):
        if self.minFreq == 0 or self.size == 0:
            return -1
        if key not in self.nodeMap:
            return -1
        
        print('get')
        node = self.nodeMap[key]
        self.updateNode(node)
        return node.val


    # UPDATING NODE IN FREQ_MAP
    def updateNode(self, node):
        oldDLList = self.freqMap[node.frequency]
        oldDLList.removeNode(node)
        
        if oldDLList.size == 0 and node.frequency == self.minFreq:
            self.minFreq += 1
        node.frequency += 1
        
        if node.frequency not in self.freqMap:
            newDLList = DLList()
        else:
            newDLList = self.freqMap[node.frequency]
        newDLList.addToHead(node)
        self.freqMap[node.frequency] = newDLList
        
    def put(self, key, val):
        if self.capacity == 0:
            return 
        print('put')
        
        # CASE 1: KEY already in nodeMap
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = val
            self.updateNode(node)
            
        else:
            
            # CASE 2: ONLY IF CAPACITY REACHED, Create SPACE
            if self.size == self.capacity:
                oldDLL = self.freqMap[self.minFreq]
                removed_node = oldDLL.removeFromTail()
                del self.nodeMap[removed_node.key]
                self.size -= 1
                
            new_node = Node(key, val)
            
            # CASE 3: ADD THE NODE to FREQ == 1
            dll = self.freqMap.get(1, DLList())
            dll.addToHead(new_node)
            self.freqMap[1] = dll
            self.nodeMap[key] = new_node
            self.minFreq = 1
            self.size += 1
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)