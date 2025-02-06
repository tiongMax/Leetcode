# https://leetcode.com/problems/tuple-with-same-product/

from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hm = defaultdict(int)  
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                hm[product] += 1
        
        res = 0
        for count in hm.values():
            if count >= 2:
                res += (count * (count - 1) // 2) * 8  # Combination formula C(n, 2) * 8

        return res
