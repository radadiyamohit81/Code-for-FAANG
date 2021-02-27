# Intuition

# Let's figure out how to sort the input here. 
# The input should be sorted by a parameter which indicates a money lost for the company.

# The company would pay anyway : price_A to send a person to the city A, or price_B to send a person to the city B. 
# By sending the person to the city A, the company would lose price_A - price_B, which could negative or positive.

# To optimize the total costs, let's sort the persons by price_A - price_B and then send the first n persons to the city A, and the others to the city B, because this way the company costs are minimal.

# Algorithm
# Sort the persons in the ascending order by price_A - price_B parameter, which indicates the company additional costs.
# To minimise the costs, send n persons with the smallest price_A - price_B to the city A, and the others to the city B.


class Solution:

    # O(NlogN) Time
    # O[1] Space
    def twoCitySchedCost(self, costs):
        if costs == []:
            return 0
        
        total = 0
        costs.sort(key = lambda x: x[0] - x[1])
        # This type of sorting ensures 1s half of array has smaller costs difference, 2nd half has larger costs difference ========> cityA - cityB 
        # LEFT HALF  --------> cityA is SMALLER
        # RIGHT HALF --------> cityB is SMALLER
        
        n = len(costs)//2
        for i in range(n):
            total += costs[i][0] 
        for i in range(n, len(costs)):
            total += costs[i][1]
        return total
            