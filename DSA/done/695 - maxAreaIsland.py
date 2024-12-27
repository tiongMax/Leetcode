from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            cur_area = 1
            grid[r][c] = 0
            for dr, dc in direction:
                cur_area += dfs(r + dr, c + dc)

            return cur_area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))

        return res
