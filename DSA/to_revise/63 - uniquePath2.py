# https://leetcode.com/problems/unique-paths-ii/

from typing import List

# Approach 1: Dp
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        prev = [0] * m
        for i in range(len(obstacleGrid)):
            cur = [0] * m
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                elif i == j == 0:
                    cur[j] = 1
                else:
                    up = prev[j]
                    left = cur[j - 1] if j >= 1 else 0
                    cur[j] = up + left
            prev = cur

        return prev[m - 1]

# Approach 2: Memo
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}

        def memo(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]

            up = memo(i - 1, j) if i >= 1 else 0
            left = memo(i, j - 1) if j >= 1 else 0
            dp[(i, j)] = up + left
            return dp[(i, j)]

        return memo(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)