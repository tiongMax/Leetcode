# https://leetcode.com/problems/find-greatest-common-divisor-of-array

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx, mn = max(nums), min(nums)
        
        # Helper function for recursive GCD
        def gcd_recursive(a: int, b: int) -> int:
            if b == 0:
                return a
            return gcd_recursive(b, a % b)
            
        return gcd_recursive(mx, mn)