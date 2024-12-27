# https://leetcode.com/problems/binary-subarrays-with-sum/

from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def slidWind(g):
            l = count = cur_sum = r = 0
            while r < len(nums):
                cur_sum += nums[r]
                while l <= r and cur_sum > g:
                    cur_sum -= nums[l]
                    l += 1
                count += r - l + 1
                r += 1
            return count
        
        return slidWind(goal) - slidWind(goal - 1)
