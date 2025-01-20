# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        direction = {
            1: [0, 1],  # right
            2: [0, -1], # left
            3: [1, 0],  # down
            4: [-1, 0]  # up
        }
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 0)])  # r, c, cost
        min_cost = {(0, 0): 0}  # (r, c) -> min cost
        while q:
            r, c, cost = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return cost
            
            for d in direction:
                dr, dc = direction[d]
                nr, nc = r + dr, c + dc
                n_cost = cost if d == grid[r][c] else cost + 1
                
                if (
                    nr < 0 or nc < 0 or
                    nr >= ROWS or nc >= COLS or
                    n_cost >= min_cost.get((nr, nc), float("inf"))
                ):
                    continue
                
                min_cost[(nr, nc)] = n_cost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))
