class Solution:

    # BruteForce Solution 
    # O(N*M) Time
    def optimizeAirRoutes1(self, maxTravelDist, forwardRouteList, returnRouteList):
        maxDistance = -1
        totalDistance = 0

        for i in forwardRouteList:
            if i[1] > maxTravelDist:
                break
            for j in returnRouteList:
                if j[1] > maxTravelDist - i[1]:
                    continue
                totalDistance = i[1] + j[1]
                if totalDistance >= maxDistance:
                    maxDistance = totalDistance
        return maxDistance

    # Two Pointer Approach,
    # O(M+N) Time
    def optimizeAirRoutes2(self, maxTravelDist, forwardRouteList, returnRouteList):

        p1 = 0
        p2 = len(returnRouteList)-1
        max_val = 0

        while p1 < len(forwardRouteList):
            while p2 >= 0:
                totalDistance = forwardRouteList[p1][1] + returnRouteList[p2][1]
                if totalDistance <= maxTravelDist and totalDistance > max_val:
                    max_val = totalDistance
                    break
                else:
                    p2 -= 1
            p1 += 1 
        return max_val

    # Binary Search Approach
    # O(M * logN) Time
    def optimizeAirRoutes3(self, maxTravelDist, forwardRouteList, returnRouteList):
        if forwardRouteList is None and returnRouteList is None:
            return None

        if len(returnRouteList) < len(forwardRouteList):
            self.optimizeAirRoutes3( maxTravelDist, returnRouteList, forwardRouteList )

        max_so_far = float('-inf')
        
        for froute in forwardRouteList:
            low = 0
            high = len(returnRouteList)-1
            while low <= high:
                mid = low + (high-low)//2
                routecost = returnRouteList[mid][1] + froute[1]
                if routecost <= maxTravelDist:
                    if routecost > max_so_far:
                        max_so_far = routecost
                    low = mid + 1
                else:
                    high = mid - 1
        return max_so_far

             
obj = Solution()
print("Iterative Bruteforce Solution: ", obj.optimizeAirRoutes2( maxTravelDist = 7000, forwardRouteList = [[1, 2000],[2, 4000],[3,6000]], returnRouteList = [[1,2000], [2,4500], [3,7000]] ))
print("Two Pointer Solution: ",obj.optimizeAirRoutes2( maxTravelDist = 7000, forwardRouteList = [[1, 2000],[2, 4000],[3,6000]], returnRouteList = [[1,2000], [2,4500], [3,7000]] ))
print("Binary Search Solution: ",obj.optimizeAirRoutes3( maxTravelDist = 7000, forwardRouteList = [[1, 2000],[2, 4000],[3,6000]], returnRouteList = [[1,2000], [2,4500], [3,7000]] ))



