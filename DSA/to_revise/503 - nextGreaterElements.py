# https://leetcode.com/problems/next-greater-element-ii/

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        stack = []
        for i in range((2 * len(nums)) - 1, -1, -1):
            while stack and stack[-1] <= nums[i % len(nums)]:
                stack.pop()
            greater = stack[-1] if stack else -1
            if i < len(nums):
                res.append(greater)
            stack.append(nums[i % len(nums)])

        return res[::-1]