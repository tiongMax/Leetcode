from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0' or \
                (r, c) in visited:
                return 

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    dfs(r, c)

        return res