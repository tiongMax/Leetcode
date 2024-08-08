# https://leetcode.com/problems/spiral-matrix-iii/description/

from typing import List

# Neetcode
from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1
        direction_index = 0
        r, c = rStart, cStart
        result = [[r, c]]
        
        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    r += directions[direction_index][0]
                    c += directions[direction_index][1]
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                direction_index = (direction_index + 1) % 4
            steps += 1
        
        return result

# Mine
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        cnt = rows * cols
        left = up = 2
        down = r1 = r2 = 1
        res = [[rStart, cStart]]
        cnt -= 1  # Decrement the count for the starting cell

        while cnt > 0:
            # Move right
            for r in range(r1):
                cStart += 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    cnt -= 1
            r1 += 1
            
            # Move down
            for d in range(down):
                rStart += 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    cnt -= 1
            down += 2

            # Move left
            for l in range(left):
                cStart -= 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    cnt -= 1
            left += 2

            # Move up
            for u in range(up):
                rStart -= 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    cnt -= 1
            up += 2

            # Move right again
            for r in range(r2):
                cStart += 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    cnt -= 1
            r2 += 1

        return res
