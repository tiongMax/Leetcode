# https://leetcode.com/problems/longest-common-subsequence/

# Approach 1: Dp
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        prev = [0] * (m + 1)

        for i in range(1, n + 1):
            cur = [0] * (m + 1)
            for j in range(1, m + 1):              
                if text1[i - 1] == text2[j - 1]:
                    cur[j] = 1 + prev[j - 1]
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur

        return prev[m]

# Approach 2: Memo
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def memo(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            res = 0
            if text1[i] == text2[j]:
                res = 1 + memo(i - 1, j - 1)
            else:
                res = max(memo(i - 1, j), memo(i, j - 1))
            dp[(i, j)] = res
            return res

        return memo(len(text1) - 1, len(text2) - 1)