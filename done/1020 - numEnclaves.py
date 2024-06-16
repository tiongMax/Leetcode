from typing import List

# Recursion using stack
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            stack = [[r, c]]
            while stack:
                dr, dc = stack.pop()
                if dr < 0 or dc < 0 or dr >= len(grid) or dc >= len(grid[0]) or grid[dr][dc] != 1:
                    continue

                grid[dr][dc] = 2
                stack.append([dr, dc + 1])
                stack.append([dr + 1, dc])
                stack.append([dr - 1, dc])
                stack.append([dr, dc - 1])

        # def dfs(r, c):
        #     if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] != 1:
        #         return
                
        #     grid[r][c] = 2
        #     dfs(r + 1, c)
        #     dfs(r - 1, c)
        #     dfs(r, c + 1)
        #     dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r in [0, len(grid) - 1] or c in [0, len(grid[0]) - 1]):
                    dfs(r, c)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res += 1

        return res