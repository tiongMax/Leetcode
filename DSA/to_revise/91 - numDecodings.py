# https://leetcode.com/problems/decode-ways/
 
# Approach 1: dp
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
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
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                res += dfs(i + 2)
            
            memo[i] = res
            return res
        
        return dfs(0)    

"""
The pointer will point to the first index for 2 digits number and to the only digit for 1 digit number
to check if the first index is 0. 

If i is ok, we proceed to i + 1 for 1 digit number. As for 2 digit number, we check if i + 1 will be a 
valid number when combine with i. If yes, we proceed to i + 2 else i + 1.
i is the index.
"""   