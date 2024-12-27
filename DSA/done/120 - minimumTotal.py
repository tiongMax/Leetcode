# https://leetcode.com/problems/triangle/submissions/

from typing import List

# Approach 1: Dp
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            temp = [0] * len(triangle[i])
            for j in range(len(triangle[i])):
                down = triangle[i][j] + prev[j]
                right_diag = triangle[i][j] + prev[j + 1]
                temp[j] = min(down, right_diag)
            prev = temp

        return prev[0]
    
# Approach 2: Memo
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}

        def memo(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            if (i, j) in dp:
                return dp[(i, j)]

            down = triangle[i][j] + memo(i + 1, j)
            right_diag = triangle[i][j] + memo(i + 1, j + 1) 
            dp[(i, j)] = min(down, right_diag)
            return dp[(i, j)]

        return memo(0, 0)
    
"""
Since the base case is a list in approach 2, when we use dp, our base case is also a list.
"""