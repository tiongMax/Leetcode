# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hm = set()  
        res = [0] * len(A)
        common_count = 0  
        for i in range(len(A)):
            if A[i] in hm:
                common_count += 1
            else:
                hm.add(A[i])

            if B[i] in hm:
                common_count += 1
            else:
                hm.add(B[i])

            res[i] = common_count
        return res
