# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = l = 0
        r = len(height) - 1
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        return res