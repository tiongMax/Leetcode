# https://leetcode.com/problems/powx-n/

# Iterative approach
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            if n % 2:
                res *= x
            n >>= 1
            x *= x
        return res
    
# Recursive approach
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: 
                return 0
            if n == 0:
                return 1

            mul = helper(x * x, n // 2)
            return mul * x if n % 2 else mul 

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
            