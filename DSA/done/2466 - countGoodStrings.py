# // https://leetcode.com/problems/count-ways-to-build-good-strings/

# Memo
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        MOD = 10**9 + 7 

        def dfs(i):
            if i > high:
                return 0
            if i in dp:
                return dp[i]

            res = 0
            if i >= low:
                res += 1

            res += dfs(i + zero) 
            res %= MOD
            res += dfs(i + one)
            res %= MOD
            dp[i] = res
            return res

        return dfs(0) % MOD
    
# Dp
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + max(zero, one) + 1)
        MOD = 10**9 + 7 

        for i in range(high, -1, -1):
            dp[i] = 0 if i < low else 1
            dp[i] += dp[i + zero] 
            dp[i] %= MOD
            dp[i] += dp[i + one]
            dp[i] %= MOD

        return dp[0] % MOD