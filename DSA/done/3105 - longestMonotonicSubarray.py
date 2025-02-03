# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_len = dec_len = 1
        inc = dec = 0
        for r in range(1, len(nums)):
            if nums[r] <= nums[r - 1]:
                inc = r
            inc_len = max(inc_len, r - inc + 1)

            if nums[r] >= nums[r - 1]:
                dec = r
            dec_len = max(dec_len, r - dec + 1)

        return max(inc_len, dec_len)
