# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

from typing import List
from math import sqrt

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag = area = 0
        for l, w in dimensions:
            square_root = sqrt(l * l + w * w)
            cur_area = l * w
            if square_root > diag:
                diag = square_root
                area = cur_area
            elif square_root == diag and cur_area > area:
                area = cur_area
        return area