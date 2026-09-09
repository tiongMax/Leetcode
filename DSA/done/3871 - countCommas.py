# https://leetcode.com/problems/count-commas-in-range-ii/description/

class Solution:
    def countCommas(self, n: int) -> int:
        p = 1000
        res = 0
        while p <= n:
            res += n - p + 1
            p *= 1000
        return res