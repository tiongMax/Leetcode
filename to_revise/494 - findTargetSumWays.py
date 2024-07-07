# https://leetcode.com/problems/target-sum/

from typing import List
from collections import defaultdict

# Approach 1: Dp
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Check if the target is reachable
        if abs(target) > total_sum:
            return 0
        
        # Initialize dp dictionary
        dp = defaultdict(int)
        dp[0] = 1  # Starting point
        
        for num in nums:
            next_dp = defaultdict(int)
            for sum_val in dp:
                if dp[sum_val] != 0:
                    next_dp[sum_val + num] += dp[sum_val]
                    next_dp[sum_val - num] += dp[sum_val]
            dp = next_dp
        
        return dp[target]

# Approach 2: Memo
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)

