# https://leetcode.com/problems/car-fleet/

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            cur = (target - p) / s
            if stack and cur <= stack[-1]:
                continue
            else:
                stack.append(cur)
        return len(stack) 

