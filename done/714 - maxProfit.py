# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import List

# Approach 1: Dp
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        prev = [0] * 2

        for i in range(n - 1, -1, -1):
            cur = [0] * 2
            for j in range(2):
                if j == 0:
                    cur[j] = max(prev[0], prev[1] - prices[i])
                else:
                    cur[j] = max(prev[1], prev[0] + prices[i] - fee)
            prev = cur

        return prev[0]

# Approach 2: Memo
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
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
                selling = memo(i + 1, not buy) + prices[i] - fee
                dp[(i, buy)] = max(hold, selling)
            return dp[(i, buy)]

        return memo(0, True)
