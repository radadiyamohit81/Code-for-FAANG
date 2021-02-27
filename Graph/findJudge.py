# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:
# 1) The town judge trusts nobody.
# 2) Everybody (except for the town judge) trusts the town judge.
# 3) There is exactly one person that satisfies properties 1 and 2.

# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3

class Solution:
    def findJudge(self, N, trust):
        # Each person gains 1 "point" for each person they are trusted by, and loses 1 "point" for each person they trust. 
        # Then at the end, the town judge, if they exist, must be the person with N - 1 "points".


        # <------- INDEGREES ARRAY CONCEPT -------->
        if len(trust) < N - 1:
            return -1

        indegrees_trust = [0] * (N+1) 
        for a, b in trust:
            indegrees_trust[a] -= 1
            indegrees_trust[b] += 1
        
        # we are mapping person 1 to index 1,
        # do not consider index 0
        for i in range(1, len(indegrees_trust)):
            score = indegrees_trust[i]
            if score == N - 1:
                return i
        return -1