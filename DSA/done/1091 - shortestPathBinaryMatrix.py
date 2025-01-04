# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        visited = set()
        q = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        visited.add((0, 0))
        q.append((0, 0))
        length = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length

                for dr, dc in directions:
                    nextr, nextc = r + dr, c + dc

                    if 0 <= nextr < len(grid) and 0 <= nextc < len(grid[0]) and grid[nextr][nextc] == 0 and (nextr, nextc) not in visited:
                        q.append((nextr, nextc))
                        visited.add((nextr, nextc))

            length += 1

        return -1
