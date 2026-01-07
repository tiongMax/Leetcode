# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def get_sum(divisor):
            total = 0
            for n in nums:
                # Ceiling division: (n + divisor - 1) // divisor
                total += (n + divisor - 1) // divisor
            return total
        
        # Binary search for the smallest divisor
        l, r = 1, max(nums)
        res = r
        
        while l <= r:
            m = l + (r - l) // 2
            if get_sum(m) <= threshold:
                res = m      # This works! Try to find a smaller one.
                r = m - 1
            else:
                l = m + 1    # Sum is too big, we need a bigger divisor.
                
        return res