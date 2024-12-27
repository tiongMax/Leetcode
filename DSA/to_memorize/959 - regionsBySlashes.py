# https://leetcode.com/problems/regions-cut-by-slashes/

from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ROWS = COLS = len(grid)
        ROWS2 = COLS2 = 3 * len(grid)
        upscaled_grid = [[0] * COLS2 for _ in range(ROWS2)]

        for r in range(ROWS):
            for c in range(COLS):
                dr, dc = r * 3, c * 3
                if grid[r][c] == '/':
                    upscaled_grid[dr][dc + 2] = 1
                    upscaled_grid[dr + 1][dc + 1] = 1
                    upscaled_grid[dr + 2][dc] = 1
                elif grid[r][c] == '\\':
                    upscaled_grid[dr][dc] = 1
                    upscaled_grid[dr + 1][dc + 1] = 1
                    upscaled_grid[dr + 2][dc + 2] = 1

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]   
        visited = set()  
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS2 or c >= COLS2 or (r, c) in visited or \
                upscaled_grid[r][c] == 1:
                return

            visited.add((r, c))
            for dr, dc in directions:
                dfs(dr + r, dc + c)

        res = 0
        for r in range(ROWS2):
            for c in range(COLS2):
                if (r, c) not in visited and upscaled_grid[r][c] == 0:
                    dfs(r, c)
                    res += 1

        return res
        