# https://leetcode.com/problems/house-robber-ii/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(arr):
            r1, r2 = 0, 0
            for n in arr:   
                temp = r1 + n
                r1 = r2
                r2 = max(temp, r2)
            return r2
        return max(nums[0], rob_helper(nums[:-1]), rob_helper(nums[1:]))