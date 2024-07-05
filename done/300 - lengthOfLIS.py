# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

# Approach 1: Dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])

        return res
    
# Approach 2: Memoization
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def lis_ending_at(index: int) -> int:
            if index in memo:
                return memo[index]
            
            max_len = 1
            for prev_index in range(index):
                if nums[prev_index] < nums[index]:
                    max_len = max(max_len, lis_ending_at(prev_index, memo) + 1)
            
            memo[index] = max_len
            return max_len

        if not nums:
            return 0
        return max(lis_ending_at(i) for i in range(len(nums)))
