# https://leetcode.com/problems/longest-palindromic-subsequence/

# Approach 1: Using lcs
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def lcs(s1, s2):
            n = len(s1)
            m = len(s2)
            prev = [0] * (m + 1)

            for i in range(1, n + 1):
                cur = [0] * (m + 1)
                for j in range(1, m + 1):
                    if s1[i - 1] == s2[j - 1]:
                        cur[j] = 1 + prev[j - 1] 
                    else:
                        cur[j] = max(cur[j - 1], prev[j])
                prev = cur

            return prev[m]
        return lcs(s, s[::-1])