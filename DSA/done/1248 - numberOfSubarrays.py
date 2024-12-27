# https://leetcode.com/problems/count-number-of-nice-subarrays/

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def slidWind(g):
            l = r = count = oddc = 0
            while r < len(nums):
                if nums[r] % 2 == 1:
                    oddc += 1
                while l <= r and oddc > g:
                    if nums[l] % 2 == 1:
                        oddc -= 1
                    l += 1
                count += r - l + 1
                r += 1
            return count

        return slidWind(k) - slidWind(k - 1)