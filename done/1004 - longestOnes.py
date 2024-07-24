# https://leetcode.com/problems/max-consecutive-ones-iii/

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = maxl = zero = 0
        while r < len(nums):
            if nums[r] == 0:
                zero += 1
            
            if zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            if zero <= k:
                maxl = max(maxl, r - l + 1)
            r += 1

        return maxl