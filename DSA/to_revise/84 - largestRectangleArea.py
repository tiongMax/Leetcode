# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def prevSmallerElementIndex(heights):
            stack = []
            res = []
            for i in range(len(heights)):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                ind = stack[-1] if stack else -1
                res.append(ind)
                stack.append(i)
            return res

        def nextSmallerElementIndex(heights):
            stack = []
            res = [0] * len(heights)
            for i in range(len(heights) - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                ind = stack[-1] if stack else len(heights)
                res[i] = ind
                stack.append(i)
            return res

        pse = prevSmallerElementIndex(heights)
        nse = nextSmallerElementIndex(heights)

        max_area = 0
        for i in range(len(heights)):
            width = nse[i] - pse[i] - 1
            cur_max = heights[i] * width
            max_area = max(max_area, cur_max)

        return max_area
