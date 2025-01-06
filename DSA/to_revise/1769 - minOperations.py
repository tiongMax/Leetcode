# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)

        balls, moves = 0, 0
        for i in range(len(boxes)):
            res[i] = balls + moves
            moves += balls
            balls += int(boxes[i])

        balls, moves = 0, 0
        for i in reversed(range(len(boxes))):
            res[i] += balls + moves
            moves += balls
            balls += int(boxes[i])

        return res
