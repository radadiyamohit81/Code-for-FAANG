class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.previous = None
        self.next = None
        self.frequency = 1

class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.size = 0          # size of doubly linked list will be zero, initially.

        # connect head to tail pointers
        self.head.next = self.tail
        self.tail.previous = self.head

    def addNodeToHead(self, node):
        node.next = self.head.next
        self.head.next = node
        node.previous = self.head
        node.next.previous = node
        self.size += 1

    def removeNode(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
        self.size -= 1
    
    def removeNodeFromTail(self):
        tail_Prev = self.tail.previous
        # tail_Prev.previous.next = tail_Prev.next
        # tail_Prev.next.previous = tail_Prev.previous
        self.removeNode(tail_Prev)
        return tail_Prev


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_size = 0
        self.key_node = {}
        self.cache = {}
        self.min_freq = 0

    def get(self, key):
        if self.min_freq == 0 or self.cache_size==0:
            return -1
        if key not in self.key_node:      # if key is not found in the key node.
            return -1

        self.update(self.key_node[key])
        return self.key_node[key].val


    # function to update the frequency of node in cache
    def update(self, node):
        dll = self.cache[node.frequency]
        dll.removeNode(node)

        if node.frequency == self.min_freq and dll.size == 0:
            self.min_freq += 1
        node.frequency += 1

        # ********  If the increased frequency is not in the cache, create a new DLL
        newDLL = self.cache.get(node.frequency, DLL())
        newDLL.addNodeToHead(node)
        self.cache[node.frequency] = newDLL

    def put(self, key, value):
        if self.capacity == 0:
            return 
        
        # update the existing node on both HashMap's
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self.update(node)

        else:
            
            # Capacity is FULL, delete the lfu
            if self.cache_size >=  self.capacity:
                lfu_DLL = self.cache[self.min_freq]    # fetch the linked list corresponding to the min_freq and remove the last node from tail 
                removed_node = lfu_DLL.removeNodeFromTail()
                
                #****** Delete node from both HashMap's
                del self.key_node[removed_node.key]
                self.cache_size -= 1
            
            #****** Update Node on both HashMap's
            new_node = Node(key, value)
            self.key_node[key] = new_node
            dll = self.cache.get(1, DLL())
            dll.addNodeToHead(new_node)
            self.cache[new_node.frequency] = dll
            self.min_freq = 1
            self.cache_size +=1


