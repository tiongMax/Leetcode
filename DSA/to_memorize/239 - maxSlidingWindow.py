# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []

        for r in range(len(nums)):
            # Remove elements from the front of the deque if they are out of the current window
            if r > 0 and d[0] < r - k + 1:
                d.popleft()

            # Remove elements from the back of the deque if they are smaller than the current element
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)

            # Once we have a valid window, append the maximum to the result list
            if r >= k - 1:
                res.append(nums[d[0]])

        return res
