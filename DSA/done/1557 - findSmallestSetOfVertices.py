# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * (n)
        for s, d in edges:
            in_degree[d] += 1

        res = []
        for i in range(n):
            if in_degree[i] == 0:
                res.append(i)
        
        return res