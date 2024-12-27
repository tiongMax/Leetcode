# https://leetcode.com/problems/minimum-cost-for-tickets/submissions/

from typing import List
from collections import defaultdict

# Approach 1: Dp
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = defaultdict(int)
        
        for i in range(len(days) - 1, -1, -1):
            dp[i] = float('inf')
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp[j])
            
        return dp[i]
    
# Approach 2: Memo
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = defaultdict(int)
        
        def memo(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = float('inf')
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + memo(j))
            return dp[i]

        return memo(0)