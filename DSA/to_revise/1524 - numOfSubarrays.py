# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = cur_sum = odd = even = 0
        MOD = 10 ** 9 + 7
        for n in arr:
            cur_sum += n
            if cur_sum % 2:
                res = (res + 1 + even) % MOD
                odd += 1
            else:
                res = (res + odd) % MOD
                even += 1
        return res