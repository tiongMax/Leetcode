# https://leetcode.com/problems/trapping-rain-water/submissions/1606524145/

from typing import List

# 2 pointers approach
class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = maxR = l = res = 0
        r = len(height) - 1
        while l <= r:
            if maxL <= maxR:
                x = maxL - height[l]
                res += x if x > 0 else 0
                maxL = max(maxL, height[l])
                l += 1
            else:
                x = maxR - height[r]
                res += x if x > 0 else 0
                maxR = max(maxR, height[r])
                r -= 1
        return res
    
# O(n) space approach
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
        
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i + 1])
        
        res = 0
        for i in range(n):
            x = min(leftMax[i], rightMax[i]) - height[i]
            res += x if x >= 0 else 0

        return res