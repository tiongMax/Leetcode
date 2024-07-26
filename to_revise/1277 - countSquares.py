# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [row.copy() for row in matrix]
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    # all 3 directions will be either the same or 1 to 2 of them 
                    # having a smaller value. This means that how many squares can
                    # be formed will be limited by them.
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                count += dp[i][j]
        
        return count
