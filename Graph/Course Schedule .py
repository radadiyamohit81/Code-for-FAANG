class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0]*numCourses    # represents no.of prereq to be completed for each course 
        adjacency_d = {}              # { course: [dependents] }
        q = []
        
        # for every edge, build indegrees and adj_map at the same time as N is GIVEN
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
                
        
        
            
        
        