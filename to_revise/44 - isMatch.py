# https://leetcode.com/problems/wildcard-matching/submissions/

# Approach 1: Dp
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        prev = [False] * (n + 1)
        prev[0] = True

        for j in range(1, n + 1):
            prev[j] = prev[j - 1] and (p[j - 1] == '*')

        for i in range(1, m + 1):
            cur = [False] * (n + 1)
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    cur[j] = prev[j] or cur[j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = False

            prev = cur
        return prev[n]
    
# Approach 2: Memo
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def memo(i, j):
            if j < 0 and i < 0:
                return True
            if j < 0:
                return False
            if i < 0:
                tmp = ["*"] * (j + 1)
                if p[:j + 1] == "".join(tmp):
                    return True
                return False
            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            if s[i] == p[j] or p[j] == "?":
                res = memo(i - 1, j - 1)
            if p[j] == "*":
                res = memo(i - 1, j) or memo(i, j - 1)
            dp[(i, j)] = res
            return res

        return memo(len(s) - 1, len(p) - 1)