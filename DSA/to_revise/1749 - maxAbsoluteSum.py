# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre = res = max_pre = cur = 0
        for n in nums:
            cur += n
            res = max(res, abs(cur - min_pre), abs(cur - max_pre))
            min_pre = min(min_pre, cur)
            max_pre = max(max_pre, cur)
        return res
