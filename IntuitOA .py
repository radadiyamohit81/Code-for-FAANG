class Solution:
    def findDestinations(self, adjList):
        adjMap = {}                # ADJ-MAP Maintain all children of each node
        nodes = set()              # collection of all nodes

        # d{ source, edge[0] } = to_connection, edge[1]
        for edge in adjList:
            nodes.add(edge[0])
            nodes.add(edge[1])
            if edge[0] not in adjMap:
                adjMap[edge[0]] = [ edge[1] ]
            else:
                adjMap[edge[0]].append( edge[1] )

        # Build Indegrees and Outdegrees Array 
        sources = set()             # Node not in Indegrees
        destinations = set()        # No entry in ADJ-MAP
        indegrees = set()

        for start in adjMap:
            for child in adjMap[start]:
                indegrees.add(child)
                if child not in adjMap:
                    destinations.add(child)
        for node in nodes:
            if node not in indegrees:       # Node with no incoming nodes, not in indegrees
                sources.add(node)

        print("sources",sources)
        print("destinations",destinations)
        answer = {}
        # For each of the source, do BFS to CHECK the possible destinations:
        for source in sources:
            q = []
            q.append(source)
            while q != []:
                node = q.pop(0)
                if node not in destinations:
                    for child in adjMap[node]:
                        q.append(child)
                elif node in destinations:
                    if source not in answer:
                        answer[source] = [node]
                    else:
                        if node not in answer[source]:
                            answer[source].append(node)
                print("q: ",q)
                print("node is: ", node)
        return answer

obj = Solution()
print(obj.findDestinations(
    adjList= [ ['A','B'],['A','C'],['B','K'],['C','K'],['E','L'],['F','G'],['J','M'],['E','F'],['G','H'],['G','I']]
))