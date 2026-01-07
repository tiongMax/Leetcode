# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            # Returns True if we can ship everything within 'days'
            days_spent = 1
            total = 0
            for w in weights:
                if total + w > capacity:
                    days_spent += 1
                    total = 0
                total += w
            return days_spent <= days

        # Lower bound: max weight (must be able to carry the heaviest item)
        # Upper bound: sum of all weights (shipping everything in 1 day)
        l, r = max(weights), sum(weights)
        res = r
        
        while l <= r:
            m = l + (r - l) // 2
            if can_ship(m):
                res = m
                r = m - 1 # Try to find a smaller capacity
            else:
                l = m + 1 # Need more capacity
        return res