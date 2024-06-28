# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List

# First try
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return cost[0]

        n1, n2 = cost[-1], 0
        for i in range(len(cost) - 2, -1, -1):
            cost[i] += min(n1, n2)
            n2 = n1
            n1 = cost[i]

        return min(cost[0], cost[1])

# Optimised (Neetcode)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
