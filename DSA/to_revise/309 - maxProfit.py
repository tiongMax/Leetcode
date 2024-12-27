# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List

# Approach 1: Memo
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def memo(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]

            if buy:
                buying = memo(i + 1, not buy) - prices[i]
                hold = memo(i + 1, buy)
                dp[(i, buy)] = max(buying, hold)
            else:
                selling = memo(i + 2, not buy) + prices[i]
                hold = memo(i + 1, buy)
                dp[(i, buy)] = max(selling, hold)
            
            return dp[(i, buy)]

        return memo(0, True)
    
# Approach 2: Dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][0] - prices[i])
            dp[i][1] = max(dp[i + 1][1], (dp[i + 2][1] if i + 2 < n else 0) + prices[i])

        return dp[0][0]
