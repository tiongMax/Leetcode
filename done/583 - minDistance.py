# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        def lcs(s, t):
            nonlocal n, m
            prev = [0] * (m + 1)

            for i in range(1, n + 1):
                cur = [0] * (m + 1)
                for j in range(1, m + 1):
                    if s[i - 1] == t[j - 1]:
                        cur[j] = 1 + prev[j - 1]
                    else:
                        cur[j] = max(prev[j], cur[j - 1])
                prev = cur

            return prev[m]

        LCS = lcs(word1, word2)
        return n - LCS + m - LCS