# HEAPQ MODULE

# property of this data structure in python is that each time the smallest of heap element is popped(min heap). Whenever elements are pushed or popped, heap structure in maintained. The heap[0] element also returns the smallest element each time.

# HEAP OPERATIONS :
# import heapq
# 1. heapq.heapify(iterable)     converts the iterable into a heap data structure. i.e. in heap order.
# 2. heapq.heappush(heap, ele)   to insert the element mentioned in its arguments into heap. The order is adjusted, so as heap structure is maintained.
# 3. heapq.heappop(heap)         to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained.
# 4. heapq.heappushpop(heap, ele)   element is first pushed, then the element is popped, increasing efficiency. Heap order is maintained after this operation.
# 5. heapq.heapreplace(heap, ele)   element is first popped, then the element is pushed. i.e, the value larger than the pushed value can be returned. 

# heapreplace() returns the smallest value originally in heap regardless of the pushed element as opposed to heappushpop().



list_stu = [(5,'Rina'),(1,'Anish'),(3,'Moana'),(2,'cathy'),(4,'Lucy')] 

import heapq
heapq.heapify( list_stu )   # Arrange based on the roll number 

print("\nThe order of presentation is : \n") 
print("On Iterating over the HeapQueue:")
for i in range(len(list_stu)): 
  print( list_stu[i] )

print("\nOn Applying HeapPop Operation: ")
for i in range(len(list_stu)): 
  print( heapq.heappop(list_stu) )





# --------------------------------------
# li = [5, 7, 9, 1, 3] 
# heapq.heapify(li)
# print(list(li))

# heapq.heappush(li, 4)
# print(list(li))
# print(heapq.heappop(li))

# li1 = [5, 7, 9, 4, 3]
# li2 = [5, 7, 9, 4, 3]
# print(heapq.heappushpop(li1, 2))

# print("The popped element after the heapreplace is: ", end="")
# print(heapq.heapreplace(li2, 2))

# li3 = [5, 7, 9, 4, 3]

# print("The 3 largest elements in the li3 are: ", end="")
# print(heapq.nlargest(3, li3))

