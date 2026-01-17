# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        
        for r in range(len(nums)):
            # Remove the element that is out of the window from the front of the deque
            if r >= k and d[0] == nums[r - k]:
                d.popleft()
                
            # Remove elements from the back of the deque if they are smaller than the current element
            while d and d[-1] < nums[r]:
                d.pop()
            
            # Add the current element to the deque
            d.append(nums[r])

            # Once we have a valid window, append the maximum to the result list
            if r >= k - 1:
                res.append(d[0])

        return res
