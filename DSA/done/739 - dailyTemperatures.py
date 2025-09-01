# https://leetcode.com/problems/daily-temperatures/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                tmp, ind = stack.pop()
                res[ind] = i - ind
            stack.append((v, i))
        return res