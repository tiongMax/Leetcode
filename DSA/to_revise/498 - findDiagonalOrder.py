from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                diagonals[i+j].append(mat[i][j])
        result = []
        for k in range(rows + cols - 1):
            if k % 2 == 0:
                result.extend(diagonals[k][::-1])
            else:
                result.extend(diagonals[k])
        return result
 