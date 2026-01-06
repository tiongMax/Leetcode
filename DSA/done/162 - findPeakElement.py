# https://leetcode.com/problems/find-peak-element/

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[-2] < nums[-1]:
            return len(nums) - 1

        l, r = 1, len(nums) - 2
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            elif nums[m - 1] > nums[m]:
                r = m - 1
            elif nums[m + 1] > nums[m]:
                l = m + 1
            # To handle case where left and right value is greater than the mid one 
            # (happens when there are multiple peaks)
            else:
                l = m + 1

        return -1