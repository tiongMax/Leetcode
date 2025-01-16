# https://leetcode.com/problems/bitwise-xor-of-all-pairings/

from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = n2 = 0
        if len(nums1) % 2 == 1:
            for i in range(len(nums2)):
                n2 ^= nums2[i]

        if len(nums2) % 2 == 1:
            for i in range(len(nums1)):
                n1 ^= nums1[i]

        return n1 ^ n2
