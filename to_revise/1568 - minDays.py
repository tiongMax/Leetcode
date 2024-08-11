# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, visited):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited
                or grid[r][c] == 0):
                return

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited)
            
        def countIsland():
            visited = set()
            count = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if (r, c) not in visited and grid[r][c] == 1:
                        dfs(r, c, visited)
                        count += 1
            return count

        if countIsland() != 1:
            return 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                if countIsland() != 1:
                    return 1
                grid[r][c] = 1

        # We only need to remove at most 2 squares to split any island into 2.
        # through diagonal cut 
        return 2