# https://leetcode.com/problems/interleaving-string/

# Approach 1: Dp
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        n = len(s1)
        m = len(s2)
        prev = [True] * (m + 1)
        for j in range(m):
            prev[j + 1] = s2[j] == s3[j] and prev[j]

        for i in range(1, n + 1):
            cur = [False] * (m + 1)
            cur[0] = prev[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, m + 1):
                k = i + j - 1
                first = False
                second = False 

                if s1[i - 1] == s3[k]:
                    first = prev[j]
                if s2[j - 1] == s3[k]:
                    second = cur[j - 1]

                cur[j] = first or second
            prev = cur
        return prev[m]
    
# Approach 2: Memo
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        
        def memo(i, j):
            if i < 0 and j < 0:
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            k = i + j + 1
            result = False

            if i >= 0 and s1[i] == s3[k]:
                result = memo(i - 1, j)
            if not result and j >= 0 and s2[j] == s3[k]:
                result = memo(i, j - 1)

            dp[(i, j)] = result
            return result

        return memo(len(s1) - 1, len(s2) - 1)