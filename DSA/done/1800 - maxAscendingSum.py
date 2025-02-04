# https://leetcode.com/problems/maximum-ascending-subarray-sum/

from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp = res = nums[0]
        for r in range(1, len(nums)):
            if nums[r] <= nums[r - 1]:
                temp = 0
            temp += nums[r]
            res = max(res, temp)
        return res
            
                