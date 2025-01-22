# https://leetcode.com/problems/map-of-highest-peak/

from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(isWater), len(isWater[0])
        res = [[-1] * COL for i in range(ROW)] 
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if isWater[r][c]:
                    q.append((r, c))
                    res[r][c] = 0

        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        while q:
            r, c = q.popleft()
            h = res[r][c]
            
            for dx, dy in directions:
                dr, dc = r + dx, c + dy
                if (
                    0 <= dr < ROW and 
                    0 <= dc < COL and
                    res[dr][dc] == -1
                ):
                    q.append((dr, dc))
                    res[dr][dc] = h + 1

        return res