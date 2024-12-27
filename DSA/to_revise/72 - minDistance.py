# https://leetcode.com/problems/edit-distance/

# Approach 1: Dp
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        prev = [0] * (m + 1)
        for i in range(m + 1):
            prev[i] = i

        for i in range(1, n + 1):
            cur = [0] * (m + 1)
            cur[0] = i
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(cur[j - 1], prev[j], prev[j - 1])
            prev = cur
        return prev[m]
    
# Approach 2: Memo
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = {}

        def memo(i, j):
            if j < 0:
                return i + 1
            if i < 0:
                return j + 1
            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = memo(i - 1, j - 1)
            else:
                dp[(i, j)] = 1 + min(memo(i, j - 1), memo(i - 1, j), memo(i - 1, j - 1))
            return dp[(i, j)]

        return memo(n - 1, m - 1)