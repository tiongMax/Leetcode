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