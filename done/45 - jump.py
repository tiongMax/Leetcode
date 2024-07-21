# https://leetcode.com/problems/jump-game-ii/

from typing import List

# Approach 1: Memo
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}

        def memo(i):
            if i >= len(nums) - 1:
                return 0
            if i in dp:
                return dp[i]
            
            mini = float('inf')
            max_jump = min(nums[i], len(nums) - 1 - i)
            for j in range(1, max_jump + 1):
                mini = min(mini, 1 + memo(i + j))
            
            dp[i] = mini
            return mini

        return memo(0)
