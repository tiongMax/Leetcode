# https://leetcode.com/problems/koko-eating-bananas/

from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def speed(r):
            t_taken = 0
            for p in piles:
                t_taken += ceil(p / r)

            return t_taken

        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + (r - l) // 2 
            if speed(mid) > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1

        return res