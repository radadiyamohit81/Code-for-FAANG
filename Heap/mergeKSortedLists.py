class Node:
    def __init__(self, value):
        self.key = value
        self.next = None
    
class Solution:        
	# BRUTEFORCE (Adding all the values in array and sorting then cretaing a LL) => O(NKlog(NK)) Time, O(NK) Space

	# SOLUTION 2      Merging 1 List at a Time
    # Time: O(NK)
    # Space: O(1)
    def mergeKLists(self, lists):
        result = merged = Node(float('-inf'))
        for head in lists:
            self.mergeLists(merged, head)
        return result.next
    def mergeLists(self, l1, l2):
        res = dummy = Node(-1)
        while l1 != None and l2 != None: 
            if l1.key <= l2.key:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1 == None:
            dummy.next = l2
        elif l2 == None:
            dummy.next = l1
        return res.next
    


class Solution:
	# SOLUTION 3       HEAPQ
	# Runtime - O[ N log(K) ]     K: # of lists, N: len(list)
	# Memory - O(1) excluding the resultant linked list space

	import heapq
	def mergeKLists(self, lists):
		queue = []
		for i in range(len(lists)):
			if lists[i]:
				heapq.heappush(queue, (lists[i].key, i, lists[i]))

		result = dummy = Node(float('-inf'))

		while queue:
			node_val, index, node = heapq.heappop(queue)   # pop the min element from heapq and add the remainnig chain of LL back to heapq
			dummy.next = node
			dummy = dummy.next
			node = node.next

			if node != None:
				heapq.heappush(queue, (node.key, index, node))
		return result.next


