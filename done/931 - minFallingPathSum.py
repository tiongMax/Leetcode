# https://leetcode.com/problems/minimum-falling-path-sum/

from typing import List

# Approach 1: Dp
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        prev = matrix[0][:]
        for i in range(1, len(matrix)):
            temp = [0] * len(matrix[0]) 
            for j in range(len(matrix[0])):                
                up = matrix[i][j] + prev[j]
                left_diag = matrix[i][j] + prev[j - 1] if j >= 1 else float('inf')
                right_diag = matrix[i][j] + prev[j + 1] if j < len(matrix[0]) - 1 else float('inf')
                temp[j] = min(up, left_diag, right_diag)
            prev = temp
        
        res = float('inf')
        for i in range(len(matrix[0])):
            res = min(res, prev[i])

        return res

# Approach 2: Memo
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = {}

        def memo(i, j):
            if j < 0 or j >= len(matrix[0]):
                return float('inf')
            if i == 0:
                return matrix[i][j]
            if (i, j) in dp:
                return dp[(i, j)]

            up = matrix[i][j] + memo(i - 1, j)
            left_diag = matrix[i][j] + memo(i - 1, j - 1)
            right_diag = matrix[i][j] + memo(i - 1, j + 1)
            dp[(i, j)] = min(up, left_diag, right_diag)
            return dp[(i, j)]

        res = float('inf')
        for i in range(len(matrix)):
            res = min(res, memo(len(matrix) - 1, i))

        return res