# https://leetcode.com/problems/01-matrix/

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])
        res = [[-1] * COL for _ in range(ROW)] 
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if mat[r][c] == 0:
                    q.append((r, c))
                    res[r][c] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            r, c = q.popleft()
            current_distance = res[r][c]
            
            for dx, dy in directions:
                dr, dc = r + dx, c + dy
                if (
                    0 <= dr < ROW and 
                    0 <= dc < COL and 
                    res[dr][dc] == -1  
                ):
                    res[dr][dc] = current_distance + 1
                    q.append((dr, dc))

        return res
