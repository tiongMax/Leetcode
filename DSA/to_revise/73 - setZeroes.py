# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_col_0 = any(matrix[r][0] == 0 for r in range(rows))
        first_row_0 = any(matrix[0][c] == 0 for c in range(cols))

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_0:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_0:
            for r in range(rows):
                matrix[r][0] = 0