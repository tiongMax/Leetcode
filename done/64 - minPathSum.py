# https://leetcode.com/problems/minimum-path-sum/

from typing import List

# Approach 1: Dp
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        prev = [0] * len(grid[0])
        for i in range(len(grid)):
            temp = [0] * len(grid[0])
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    temp[j] = grid[i][j]
                else:
                    up = prev[j] if i > 0 else float('inf')
                    left = temp[j - 1] if j > 0 else float('inf')
                    temp[j] = min(up, left) + grid[i][j]
            prev = temp

        return prev[-1]

# Approach 2: Memo
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}

        def memo(i, j):
            if i == j == 0:
                return grid[i][j]
            if (i, j) in dp:
                return dp[(i, j)]

            up = memo(i - 1, j) if i > 0 else float('inf')
            left = memo(i, j - 1) if j > 0 else float('inf')
            dp[(i, j)] = min(up, left) + grid[i][j]
            return dp[(i, j)]

        return memo(len(grid) - 1, len(grid[0]) - 1)
    
"""
Since the base case is a grid in memo approach, we then handle the base case of dp approach as a grid.
"""