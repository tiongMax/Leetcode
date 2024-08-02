# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total1 = nums.count(1)
        win1 = l = swap = 0
        n = len(nums)
        for r in range(2 * n):
            if nums[r % n] == 1:
                win1 += 1

            if r - l + 1 > total1:
                win1 -= nums[l % n]
                l += 1
            
            swap = max(swap, win1)

        return total1 - swap

