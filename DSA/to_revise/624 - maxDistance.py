# https://leetcode.com/problems/maximum-distance-in-arrays/

from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min, cur_max = arrays[0][0], arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            # Cant do it only after the loop as we might get the min and max
            # from the same array
            res = max(res, arr[-1] - cur_min, cur_max - arr[0])
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])

        return res

