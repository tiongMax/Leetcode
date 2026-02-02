# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        small = small2 = 51
        for i in range(1, len(nums)):
            if nums[i] < small:
                small2 = small
                small = nums[i]
            elif nums[i] < small2:
                small2 = nums[i]
        return nums[0] + small + small2