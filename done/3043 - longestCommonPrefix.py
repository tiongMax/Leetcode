# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        hm = set()
        for n in arr1:
            while n and n not in hm:
                hm.add(n)
                n //= 10 

        result = 0
        for n in arr2:
            while n:
                if n in hm:
                    result = max(result, len(str(n)))
                n //= 10

        return result