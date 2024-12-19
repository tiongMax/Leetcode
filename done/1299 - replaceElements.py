# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        curr_max = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            res[i] = curr_max
            curr_max = max(curr_max, arr[i])

        res[-1] = -1
        return res