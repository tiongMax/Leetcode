# https://leetcode.com/problems/target-sum/

from typing import List
from collections import defaultdict

# Approach 1: Dp
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        if abs(target) > total_sum:
            return 0
        
        # Use dictionary as the x value of the table range from -target to target, and it is not a good idea to use a list to
        # represent.
        dp = defaultdict(int)
        dp[0] = 1 # There is one way to achieve the sum 0, which is by not choosing any elements.
        
        for num in nums:
            next_dp = defaultdict(int)      
            for sum_val in dp:
                # Means that it is possible to get this sum value.
                if dp[sum_val] != 0:
                    """
                    If there are dp[sum_val] ways to achieve sum_val, there will be also be dp[sum_val] ways to achieve 
                    sum_val + num by adding num to each of dp[sum_val] ways.

                    For example there are 3 ways to sum up to 4, then we can +2 for each of the way to get a sum of 6.
                    However, to get to 6, we might have other ways (8 - 2) instead of 4 + 2, so we use += to the next dp to 
                    account for the total possible ways to reach 6 instead of just using =.

                    Same thing for subtract.
                    """
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

