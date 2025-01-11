# https://leetcode.com/problems/longest-common-subsequence/

# Approach 1: Dp
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev = [0] * (len(text2) + 1)  
        for i in range(len(text1) - 1, -1, -1):  
            cur = [0] * (len(text2) + 1)  
            for j in range(len(text2) - 1, -1, -1): 
                if text1[i] == text2[j]:  
                    cur[j] = 1 + prev[j + 1]
                else:  
                    cur[j] = max(prev[j], cur[j + 1])
            prev = cur  
        return prev[0]  

# Approach 2: Memo
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = 0
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = max(dfs(i, j + 1), dfs(i + 1, j))
            return dp[(i, j)]
        return dfs(0, 0)