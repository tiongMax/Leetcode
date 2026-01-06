# https://leetcode.com/problems/single-element-in-a-sorted-array/

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # Handle the cases where the mid pointer is at the start or end of the list
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-2] != nums[-1]:
            return nums[-1]

        l, r = 1, len(nums) - 2
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]
            elif (m % 2 == 0 and nums[m] == nums[m + 1])\
                or (m % 2 == 1 and nums[m] == nums[m - 1]): 
                l = m + 1
            else:
                r = m - 1
        return -1