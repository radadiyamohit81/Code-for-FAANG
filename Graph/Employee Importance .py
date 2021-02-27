
# Definition for Employee.
# class Employee:
#     def __init__(self, id: int, importance: int, subordinates: List[int]):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id):
        if id == None or employees == None:
            return 0
        
        self.importance = 0
        d = {}
        for employee in employees:
            d[employee.id] = employee
        
        self.dfs(d, id)
        return self.importance
        
    def dfs(self, d, id):
        # base case
        
        #Logic
        self.importance += d[id].importance
        sub = d[id].subordinates
        for i in sub:
            self.dfs(d, i)

        