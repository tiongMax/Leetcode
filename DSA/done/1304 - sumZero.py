# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, n, 2):
            res.append(i)
            res.append(-i)
        if n % 2:
            res.append(0)
        return res