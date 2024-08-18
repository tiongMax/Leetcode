# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        l = res = 0
        for r in range(len(nums)):
            while max_deque and nums[r] > max_deque[-1]:
                max_deque.pop()
            while min_deque and nums[r] < min_deque[-1]:
                min_deque.pop()

            max_deque.append(nums[r])
            min_deque.append(nums[r])

            while max_deque[0] - min_deque[0] > limit:
                if nums[l] == max_deque[0]:
                    max_deque.popleft()
                if nums[l] == min_deque[0]:
                    min_deque.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res
            
