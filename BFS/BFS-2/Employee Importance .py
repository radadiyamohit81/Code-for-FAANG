
"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

class Solution:
    # LookUp from the list to find Importance value of each employee O(N) ===> O(N*N) LookUp for all Employees
    # Creating an HASHMAP graph, O(N) ===> O(1) LookUP on each employee_id and [id, importance, subordinates]
    # BFS / DFS on the Employee using lookUp, add the Importance, LookUp its Subordinates Importance

    # BFS 
    # time : O(N)
    # space : O(2N), HashMap (graph) + q 
    def getImportance(self, employees, id):
        if employees == None:
            return 0

        # creating a HashMap as a ADJACANCY-GRAPH for O(1) lookup
        graph = {}
        for employee in employees:
            graph[employee.id] = employee
        
        # BFS on the Employee HashMap graph, to add all the importance values of all connected subordinates,
        q = [id]
        importanceSum = 0
        while q != []:
            size = len(q)
            for i in range(size):
                root = q.pop(0)
                importanceSum += graph[root].importance
                for sub in graph[root].subordinates:
                    q.append(sub)
        
        return importanceSum

# -----------------------------------------------------------------------
    # DFS 
    # time : O(N)
    # space : O(1) + Recursive call stack

    def getImportance(self, employees, id):
        if employees == []:
            return 0
        
        self.d = {}
        for emp in employees:
            self.d[emp.id] = emp
            
        self.imp = 0
        self.dfs(employees, id)
        return self.imp
    
    def dfs(self, employees, id):
        # Base case     (for loop takes care of the base case)
        
        # Logic
        self.imp += self.d[id].importance
        sub = self.d[id].subordinates
        for emp in sub:
            self.dfs(employees, emp)
            
                
