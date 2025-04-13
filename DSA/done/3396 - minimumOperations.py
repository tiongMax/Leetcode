# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = [False] * 101
        for i in range(len(nums) - 1, -1, -1):
            if seen[nums[i]]:
                return i // 3 + 1
            seen[nums[i]] = True
        return 0