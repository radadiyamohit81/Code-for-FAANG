class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.hashset = [None] * self.size

    def hashFunction(self, key):
        return key % self.size 

    def add(self, key):
        index = self.hashFunction(key)
        if self.hashset[index] == None:
            self.hashset[index] = Node(key)  
            return  

        current = self.hashset[index]
        while current:
            if current.key == key:
                return
            elif current.next == None:
                break
            current = current.next
        current.next = Node(key)
            

    def remove(self, key):
        index = self.hashFunction(key)
        if self.hashset[index] == None:
            return

        previous = current = self.hashset[index]
        if current == None: 
            return
        if current.key == key:
            self.hashset[index] = current.next
        else:
            current = current.next
            while current:
                if current.key == key:
                    previous.next = current.next
                    break
                else:
                    previous = current
                    current = current.next
                        
    def contains(self, key):
        index = self.hashFunction(key)
        if self.hashset[index] == None:
            return False

        current = self.hashset[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False


# -----------------------------------------------------------
class Hashset_DoubleHashing:
    def __init__(self):
        self.size = 1000
        self.hashset = [None] * self.size

    def hashFunction1(self, key):
        return key%(self.size)
    def hashFunction2(self, key):
        return key//(self.size)
        
    def add(self, key):
        h1 = self.hashFunction1(key)
        h2 = self.hashFunction2(key)
        if not self.hashset[h1]:
            self.hashset[h1] = [False] * self.size
            self.hashset[h1][h2] = True
        else:
            self.hashset[h1][h2] = True

    def remove(self, key):
        h1 = self.hashFunction1(key)
        h2 = self.hashFunction2(key)
        if self.hashset[h1]:
            self.hashset[h1][h2] = False

    def contains(self, key):
        h1 = self.hashFunction1(key)
        h2 = self.hashFunction2(key)
        if self.hashset[h1]:
            return self.hashset[h1][h2] 
        else:
            return False







