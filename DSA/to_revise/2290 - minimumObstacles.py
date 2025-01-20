# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

from typing import List
from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        deq = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while deq:
            obstacles, r, c = deq.popleft()
            if (r, c) == (ROW - 1 , COL - 1):
                return obstacles
            
            for dx, dy in neighbors:
                dr, dc = dx + r, dy + c
                if (dr, dc) not in visited and 0 <= dr < ROW and 0 <= dc < COL:
                    if grid[dr][dc]:
                        deq.append((obstacles + 1, dr, dc))
                    else:
                        deq.appendleft((obstacles, dr, dc))
                    visited.add((dr, dc))