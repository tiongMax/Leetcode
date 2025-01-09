# https://leetcode.com/problems/target-sum/

from typing import List
from collections import defaultdict

# Approach 1: Dp
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
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

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            return dp[(i, total)]

        return backtrack(0, 0)

