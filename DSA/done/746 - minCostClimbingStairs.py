# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List

# Memo
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return dp[i]
        return min(dfs(0), dfs(1))

# Dp
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = prev2 = 0
        for i in range(len(cost) - 1, -1, -1):
            tmp = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, tmp

        return min(prev1, prev2)
