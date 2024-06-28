# https://leetcode.com/problems/find-center-of-star-graph/

from typing import List

class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        return e[0][0] if e[0][0]==e[1][0] or e[0][0]==e[1][1] else e[0][1]