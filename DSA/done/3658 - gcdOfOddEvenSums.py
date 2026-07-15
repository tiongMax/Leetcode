# https://leetcode.com/problems/gcd-of-odd-and-even-sums/

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(x: int, y: int) -> int:
            return x if y == 0 else gcd(y, x % y)

        return gcd(n * n, n * (n + 1))