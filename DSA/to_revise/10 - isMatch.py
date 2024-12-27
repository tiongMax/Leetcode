# https://leetcode.com/problems/regular-expression-matching/

# Approach 1: Dp
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize previous and current row arrays
        prev = [False] * (len(p) + 1)
        prev[0] = True  # both s and p are empty

        # Initialize prev for patterns that can match an empty string (x* where x can be any char)
        for j in range(2, len(p) + 1):
            if p[j - 1] == "*":
                prev[j] = prev[j - 2]

        # Fill dp table using cur and prev rows
        for i in range(1, len(s) + 1):
            cur = [False] * (len(p) + 1)
            # cur[0] = False  # Only an empty pattern matches an empty string
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                    cur[j] = prev[j - 1]
                elif p[j - 1] == "*":
                    cur[j] = cur[j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        cur[j] = cur[j] or prev[j]
                else:
                    cur[j] = False
            prev = cur

        return prev[len(p)]

# Approach 2: Memo
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def memo(i, j):
            if i < 0 and j < 0:
                return True
            if j < 0:
                return False
            if i < 0:
                # Check if the remaining pattern can match an empty string
                return all(p[k] == '*' for k in range(j, -1, -2))
            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            if s[i] == p[j] or p[j] == ".":
                res = memo(i - 1, j - 1)
            elif p[j] == "*":
                # Check zero occurrence of the element before '*'
                res = memo(i, j - 2)
                # Check one or more occurrences of the element before '*'
                if j > 0 and (s[i] == p[j - 1] or p[j - 1] == "."):
                    res = res or memo(i - 1, j)
                
            dp[(i, j)] = res
            return res

        return memo(len(s) - 1, len(p) - 1)
