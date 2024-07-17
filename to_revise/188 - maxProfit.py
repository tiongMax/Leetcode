# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

from typing import List

# Approach 1: Dp
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        prev = [[0] * (k + 1) for _ in range(2)]
        n = len(prices)
        for i in range(n - 1, -1, -1):
            cur = [[0] * (k + 1) for _ in range(2)]
            # True or False
            for j in range(2):
                # n
                for l in range(k + 1):
                    if j == 0:
                        buying = 0
                        if l > 0:
                            buying = prev[1][l - 1] - prices[i]
                        cur[j][l] = max(buying, prev[0][l])
                    elif j == 1:
                        cur[j][l] = max(prev[0][l] + prices[i], 
                            prev[1][l])
            prev = cur
            
        return prev[0][-1]
    
# Approach 2: Memo
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = {}

        def memo(i, buy, n):
            if i == len(prices):
                return 0
            if (i, buy, n) in dp:
                return dp[(i, buy, n)]

            if buy:
                buying = 0
                if n > 0:
                    buying = memo(i + 1, not buy, n - 1) - prices[i]
                dp[(i, buy, n)] = max(buying, memo(i + 1, buy, n))
            else:
                dp[(i, buy, n)] = max(memo(i + 1, not buy, n) + prices[i], 
                    memo(i + 1, buy, n))
            return dp[(i, buy, n)]

        return memo(0, True, k)