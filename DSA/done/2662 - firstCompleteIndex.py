# https://leetcode.com/problems/first-completely-painted-row-or-column/

from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROW, COL = len(mat), len(mat[0])
        val_to_pos = {}
        for r in range(ROW):
            for c in range(COL):
                val_to_pos[mat[r][c]] = (r, c)

        row_match = [0] * ROW
        col_match = [0] * COL
        for i in range(len(arr)):
            r, c = val_to_pos[arr[i]]
            row_match[r] += 1
            col_match[c] += 1

            if row_match[r] == COL or col_match[c] == ROW:
                return i
