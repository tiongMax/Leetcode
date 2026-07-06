# https://leetcode.com/problems/remove-covered-intervals

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        max_end = cnt = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for s, e in intervals:
            if e > max_end:
                max_end = e
                cnt += 1
            
        return cnt