# https://leetcode.com/problems/2-keys-keyboard/

# Neetcode, time: O(n^2), space: O(n)
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [1000] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, 1 + i // 2):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]
    
# mine, time: O(n^2), space: O(n^2)
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        dp = {}
        def memo(i, val):
            if i == n:
                return 0
            elif i > n:
                return float('inf')
            if (i, val) in dp:
                return dp[(i, val)]

            cop = memo(i, i) if i != val else float('inf')
            paste = float('inf')
            if val:
                paste = memo(i + val, val)
            dp[(i, val)] = 1 + min(cop, paste)
            return dp[(i, val)]

        return memo(1, 0)
    