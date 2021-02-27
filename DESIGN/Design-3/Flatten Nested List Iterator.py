# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """

#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """

#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# APPROACH: Using a Queue 

# Time Complexity : O(N)
# Space Complexity : O(N) because of Recursion stack
# Did this code successfully run on Leetcode : YES


class NestedIterator:

    # Each of the elements in the NestedList are objects of class NestedInteger that have their methods
    def __init__(self, nestedList):
        self.q = self.fillQueue(nestedList)

    def fillQueue(self, nestedList):
        temp = []
        for nest in nestedList:
            # if integer, add it to result
            # if list, recursively call on the list until digit is accessed
            if nest.isInteger():
                temp.append( nest.getInteger() )       
            else:
                temp += self.fillQueue( nest.getList() )    # fn return a []
        return temp
    
    def next(self):
        return self.q.pop(0)
    def hasNext(self):
        return len(self.q) != 0


         

