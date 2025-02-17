# https://leetcode.com/problems/subsets-ii/

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        power, cur_set = [], []
        self.dfs(0, nums, power, cur_set)
        return power

    def dfs(self, i, nums, power, cur_set):
        if i >= len(nums):
            power.append(cur_set.copy())
            return

        cur_set.append(nums[i])
        self.dfs(i + 1, nums, power, cur_set)

        cur_set.pop()
        # Check if this branch contains duplicate number, then exclude it.
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        self.dfs(i + 1, nums, power, cur_set)
