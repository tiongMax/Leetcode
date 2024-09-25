# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = res = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])

        return res