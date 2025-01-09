# https://leetcode.com/problems/house-robber/

from typing import List

# Memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return dp[i]
        return dfs(0)
    
# Dp
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = prev2 = 0
        for i in range(len(nums) - 1, -1, -1):
            tmp = max(nums[i] + prev2, prev1)
            prev2, prev1 = prev1, tmp
        return prev1