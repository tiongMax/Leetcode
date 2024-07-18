# https://leetcode.com/problems/distinct-subsequences/

# Approach 1: Dp
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        prev = [0] * (m + 1)
        prev[0] = 1

        for i in range(1, n + 1):
            cur = [0] * (m + 1)
            cur[0] = 1
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    cur[j] = prev[j] + prev[j - 1]
                else:
                    cur[j] = prev[j]
            prev = cur
        return prev[m]

# Approach 2: Memo
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = {}

        def memo(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == t[j]:
                dp[(i, j)] = memo(i - 1, j) + memo(i - 1, j - 1)
            else:
                dp[(i, j)] = memo(i - 1, j)
            return dp[(i, j)]

        return memo(n - 1, m - 1)
