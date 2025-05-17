# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = i = 0
        two = len(nums) - 1

        while i <= two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            else:
                i += 1
