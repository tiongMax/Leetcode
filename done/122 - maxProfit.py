# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

# Approach 1: Dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prev = [0] * 2

        for i in range(n - 1, -1, -1):
            cur = [0] * 2
            hold = prev[0]
            buying = prev[1] - prices[i]
            cur[0] = max(hold, buying)

            hold = prev[1]
            selling = prev[0] + prices[i]
            cur[1] = max(hold, selling)

            prev = cur

        return prev[0]
    
# Approach 2: Memo
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def memo(i, buy):
            if i == len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]

            hold = memo(i + 1, buy)
            if buy:
                buying = memo(i + 1, not buy) - prices[i]
                dp[(i, buy)] = max(hold, buying)
            else:
                selling = memo(i + 1, not buy) + prices[i]
                dp[(i, buy)] = max(hold, selling)
            return dp[(i, buy)]

        return memo(0, True)
    
# Approach 3: Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ahead_buy = ahead_sell = cur_buy = cur_sell = 0

        for i in range(n - 1, -1, -1):
            cur_buy = max(ahead_buy, ahead_sell - prices[i])
            cur_sell = max(ahead_sell, ahead_buy + prices[i])
            ahead_buy, ahead_sell = cur_buy, cur_sell

        return ahead_buy
