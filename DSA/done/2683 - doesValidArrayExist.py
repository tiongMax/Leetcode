# https://leetcode.com/problems/neighboring-bitwise-xor/

from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        tmp = 0 
        for i in range(1, len(derived)):
            tmp ^= derived[i]
        return derived[0] == tmp