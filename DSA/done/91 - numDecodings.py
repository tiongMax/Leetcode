# https://leetcode.com/problems/decode-ways/
 
# Approach 1: dp
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
                
            dp[i] = dp[i + 1]
            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2]
                
        return dp[0]

# Approach 2: Memo
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1)
            if i + 1 < len(s) and (10 <= int(s[i : i + 2]) <= 26):
                res += dfs(i + 2)
            
            memo[i] = res
            return res
        
        return dfs(0)