# https://leetcode.com/problems/maximum-total-importance-of-roads/

from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge_cnt = [0] * n

        for s, d in roads:
            edge_cnt[s] += 1
            edge_cnt[d] += 1

        res = 0
        label = 1
        for count in sorted(edge_cnt):
            res += label * count
            label += 1

        return res

        
