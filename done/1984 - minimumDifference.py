# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores//

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, res = 0, float('inf')  
        for r in range(k - 1, len(nums)):
            res = min(res, nums[r] - nums[l])
            l += 1
        return res
            