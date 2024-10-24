# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        hs = set()
        for r in range(len(nums)):
            if abs(r - l) > k:
                hs.remove(nums[l])
                l += 1

            if nums[r] in hs:
                return True
            hs.add(nums[r])

        return False 