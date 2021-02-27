# Binary-Search-3

## Problem1 
Pow(x,n) (https://leetcode.com/problems/powx-n/)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

## Problem2 
Find K Closest Elements (https://leetcode.com/problems/find-k-closest-elements/)


Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104


## Problem3
Optimize Air Routes (https://leetcode.com/discuss/interview-question/318918/amazon-online-assessment)

INPUT
The input to the function/method consisits of three arguments:
maxTravelDist, an integer representing the maximum operating travel distance of the given aircraft;
forwardRouteList, a list of pairs of integers where the first integer represents the unique identifier of a forward shipping
route and the second integer represents the amount of travel distance required bu this shipping route;
returnRouteList, a list of pairs of integers where the first integer represents the unique identifer of a return shipping route
and the second integer represents the amount of travel distance required by this shipping route.

OUTPUT
Return a list of pairs of integers representing the pairs of IDs of forward and return shipping routes that optimally utilize the given aircraft. If no route is possible, return a list with empty pair.

Example 1:
Input:
maxTravelDist = 7000
forwardRouteList = [[1,2000],[2,4000],[3,6000]]
returnRouteList = [[1,2000]]

Output:
[[2,1]]

Explanation:
There are only three combinations [1,1],[2,1],and [3,1], which have a total of 4000, 6000, and 8000 miles, respectively. Since 6000 is the largest use that does tnot exceed 7000, [2,1] is the optimal pair.

Example 2:
Input:
maxTravelDist = 10,000
forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]]
returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]

Output:
[[2,4],[3,2]]
