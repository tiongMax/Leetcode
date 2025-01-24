# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 0, 0)])  
        visited = set([(0, 0, 0)])  
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            steps, r, c, cost = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return steps
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    new_cost = cost + grid[nr][nc]
                    if new_cost <= k and (nr, nc, new_cost) not in visited:
                        visited.add((nr, nc, new_cost)) 
                        q.append((steps + 1, nr, nc, new_cost))
        return -1  
