# https://leetcode.com/problems/count-servers-that-communicate/

from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        row_count, col_count = [0] * (ROW), [0] * (COL)
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]:
                    row_count[i] += 1
                    col_count[j] += 1

        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] and (row_count[r] > 1 or col_count[c] > 1):
                    res += 1
        
        return res