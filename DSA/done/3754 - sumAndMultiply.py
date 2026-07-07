# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sum = 0
        for c in str(n):
            d = int(c)
            sum += d
            if d > 0:
                x = x * 10 + d
        return x * sum