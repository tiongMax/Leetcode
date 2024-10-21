# https://leetcode.com/problems/baseball-game/

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == '+':
                stack.append(stack[-1] + stack[-2])
            elif o == 'D':
                stack.append(2 * stack[-1])
            elif o == 'C':
                stack.pop()
            else:
                stack.append(int(o))

        return sum(stack)
