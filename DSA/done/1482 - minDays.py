# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Edge case: Not enough flowers total
        if m * k > len(bloomDay):
            return -1
            
        def possible(days):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    # If we reach k adjacent flowers, make a bouquet
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        l, r = min(bloomDay), max(bloomDay)
        ans = r
        
        while l <= r:
            mid = l + (r - l) // 2
            if possible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans