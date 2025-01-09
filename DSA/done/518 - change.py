# https://leetcode.com/problems/coin-change-ii/

from typing import List

# Memo
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, cur):
            if cur == amount:
                return 1
            if i == len(coins):
                return 0
            if (i, cur) in dp:
                return dp[(i, cur)]

            dp[(i, cur)] = dfs(i + 1, cur) 
            dp[(i, cur)] += dfs(i, cur + coins[i]) if cur + coins[i] <= amount else 0
            return dp[(i, cur)]
        return dfs(0, 0)

# Dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0] * (amount + 1)
        prev[amount] = 1
        for i in range(len(coins) - 1, -1, -1):
            cur = [0] * (amount + 1)
            cur[amount] = 1
            for j in range(len(prev) - 2, -1, -1):
                cur[j] = prev[j] 
                cur[j] += cur[j + coins[i]] if j + coins[i] <= amount else 0
            prev = cur
        return prev[0]
    
# Space optimized
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0] * (amount + 1)
        prev[amount] = 1
        for i in range(len(coins) - 1, -1, -1):
            for j in range(len(prev) - 2, -1, -1):
                prev[j] += prev[j + coins[i]] if j + coins[i] <= amount else 0
        return prev[0]