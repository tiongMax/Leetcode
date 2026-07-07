# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        atl, pac = set(), set()
        
        def flow(r, c, visited, prev_h):
            if (r, c) in visited or r < 0 or c < 0 or r == ROW or c == COL or heights[r][c] < prev_h:
                return

            visited.add((r, c))
            flow(r + 1, c, visited, heights[r][c])
            flow(r, c + 1, visited, heights[r][c])
            flow(r - 1, c, visited, heights[r][c])
            flow(r, c - 1, visited, heights[r][c])

        for r in range(ROW):
            flow(r, 0, pac, -1)
            flow(r, COL - 1, atl, -1)

        for c in range(COL):
            flow(0, c, pac, -1)
            flow(ROW - 1, c, atl, -1)

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res