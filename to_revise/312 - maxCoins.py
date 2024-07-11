# https://leetcode.com/problems/burst-balloons/

from typing import List

# Approach 1: Memo
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add 1 before and after nums
        nums = [1] + nums + [1]
        dp = {}

        def memo(left, right):
            # Base case: no more balloons to burst
            if left + 1 == right:
                return 0
            
            # If already computed, return the value
            if (left, right) in dp:
                return dp[(left, right)]
            
            # Max coins we can collect by bursting all balloons in (left, right)
            max_coins = 0
            for i in range(left + 1, right):
                # nums[i] is the last balloon to burst in (left, right)
                coins = nums[left] * nums[i] * nums[right]
                coins += memo(left, i) + memo(i, right)
                max_coins = max(max_coins, coins)
            
            dp[(left, right)] = max_coins
            return max_coins

        # Calculate the maximum coins we can get by bursting all balloons except the added ones
        return memo(0, len(nums) - 1)


# Approach 2: Dp