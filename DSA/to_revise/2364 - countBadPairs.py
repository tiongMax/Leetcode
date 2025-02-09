# https://leetcode.com/problems/count-number-of-bad-pairs/

from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += i

        good = 0
        good_pair_count = defaultdict(int)
        for i in range(len(nums)):
            good += good_pair_count[nums[i] - i]
            good_pair_count[nums[i] - i] += 1
        
        return total - good