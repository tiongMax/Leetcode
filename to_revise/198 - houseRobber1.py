#

from typing import List

# My approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        h1, h2 = 0, nums[0]
        for i in range(1, len(nums)):
            cur = h1 + nums[i]
            nums[i] = max(cur, h2)
            h1, h2 = h2, nums[i]

        return h2

# Neetcode's approach (more concise)
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

"""
Note:
[4, 1, 2, 7]

We need to update 1 to 4 as when we choose to include 7 (skip 2), we can get the largest number
from the subarray of [4, 1], but we can't choose both, so we have to update the first pointer
to store the max of previous subarray.

Both pointers store the max value of the subarray from the start until the number pointed by itself.

P1, P2, curr, so we can only choose either p2 or P1 + curr.
"""