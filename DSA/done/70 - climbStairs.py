#https://leetcode.com/problems/climbing-stairs/

# Approach 1: Bottom up
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
    
# Approach 2: Memoization (top down)
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def memo(i):
            if i > n:
                return 0
            if i in cache:
                return cache[i]
            if i == n: 
                return 1

            cache[i] = memo(i + 1) + memo(i + 2)
            return cache[i]

        return memo(0)