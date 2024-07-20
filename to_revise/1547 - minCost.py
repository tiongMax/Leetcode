# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

from typing import List

# Approach 1: Dp
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c = len(cuts)
        cuts = [0] + cuts + [n]
        cuts.sort()
        dp = [[0] * (c + 2) for _ in range(c + 2)]

        for i in range(c, 0, -1):
            for j in range(1, c + 1):
                if i > j:
                    continue
                mini = float('inf')
                for k in range(i, j + 1):
                    cost = cuts[j + 1] - cuts[i - 1] + dp[i][k - 1] + dp[k + 1][j]
                    mini = min(mini, cost)
                dp[i][j] = mini

        return dp[1][c]

# Approach 2: Memo
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        cuts.sort()
        dp = {}

        def memo(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            mini = float('inf')
            for k in range(i, j + 1):
                cost = cuts[j + 1] - cuts[i - 1] + memo(i, k - 1) + memo(k + 1, j)
                mini = min(cost, mini)

            dp[(i, j)] = mini
            return mini
        
        return memo(1, len(cuts) - 2)
            
