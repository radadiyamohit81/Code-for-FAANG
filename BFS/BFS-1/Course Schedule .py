
# TOPOLOGICAL SORTING OF NODES IN GRAPH, as processing of one node is dependent on processing nodes before it
# BFS of all the nodes connected to it 
# DataStructures used: HashMap (representing the Graph in HashMap, with dependents of each course --> O(1) retrieval); 
#                      Array (maintains no.of.prereqs to be completed for each course)
#                      Queue (BFS on the graph node that has no prereqs and reduce the prereq count of its dependant subjects by 1)

# time : O(N)
# space : O(2N), graph and Array



class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0]*numCourses    # represents no.of prereq to be completed for each course 
        adjacency_d = {}              # { course: [dependents] }
        q = []
        
        # prerequisite, [1,0] ->  dependant is at index 0, sub1 has sub0 as prereq
        for prerequisite in prerequisites:
            indegrees[prerequisite[0]] += 1
            if prerequisite[1] not in adjacency_d:
                adjacency_d[prerequisite[1]] = [prerequisite[0]]
            else:
                adjacency_d[prerequisite[1]].append(prerequisite[0])
                
        # add all the subjects who have 0 prereq to be completed to takecourse
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
                
        # BFS on these subjects to decrease the prereq count by 1 on all its dependants
        while q != []:
            course = q.pop(0)
            if course in adjacency_d:
                children = adjacency_d[course]
                for child in children:
                    indegrees[child] -= 1
                    if indegrees[child] == 0:
                        q.append(child)
        
        for i in range(len(indegrees)):
            if indegrees[i] != 0:
                return False
        return True





class Solution:
    def canFinish(self, numCourses, prerequisites):

        # the dependent is at the index 1 in each prerequisites array
        # [[1,0]], we need to increase the count at prerequisites[i][1] of our indegrees array

        indegrees = [0]*numCourses   # indegrees array represents no.of.prereqs
        graph = {}                   # { course: [dependents] }, for O[1] lookup
        q = []

        for i in range(len(prerequisites)):
            indegrees[prerequisites[i][0]] += 1
            if prerequisites[i][1] not in graph:
                graph[prerequisites[i][1]] = [prerequisites[i][0]]    
            else:
                graph[prerequisites[i][1]].append(prerequisites[i][0]) 
        
        # add all subjects with 0 prereq to q
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)

        # BFS on subjects with 0 prereqs to reduce the prereq count by 1 on its dependants ie., indegrees
        while q != []:
            course = q.pop(0)
            if course in graph:
                children = graph[course]    # decrease the dependents of the course by checking the HashMap by 1 in the indegrees
                for child in children:
                    indegrees[child] -= 1             
                    if indegrees[child] == 0:
                        q.append(child)

        for i in range(len(indegrees)):
            if indegrees[i] != 0:
                return False
        return True


obj = Solution()
print(obj.canFinish(numCourses=2, prerequisites=[[1,0]]))





                
        
        
            
        
        