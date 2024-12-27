# https://leetcode.com/problems/baseball-game/

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for o in operations:
            if o == '+':
                sum = stack[-1] + stack[-2]
                stack.append(sum)
                res += sum
            elif o == 'C':
                res -= stack.pop()
            elif o == 'D':
                double = stack[-1] * 2
                stack.append(double)
                res += double
            else:
                res += int(o)
                stack.append(int(o))
        return res                
