# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        dp = {}
        rows, cols = len(matrix), len(matrix[0])

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or \
               matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            left = dfs(r, c - 1, matrix[r][c])
            right = dfs(r, c + 1, matrix[r][c])
            top = dfs(r - 1, c, matrix[r][c])
            bottom = dfs(r + 1, c, matrix[r][c])
            dp[(r, c)] = 1 + max(left, right, top, bottom)

            return dp[(r, c)]

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, -1))  # use -1 as a placeholder for the initial prev value

        return res
