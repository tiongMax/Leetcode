# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

# Time: o(n), space: o(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0 # Start from the first index.

        while True: # There is a cycle.
            slow = nums[slow] # We treat element as a number when we reach and as an index when proceed.
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow