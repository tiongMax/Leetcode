# https://leetcode.com/problems/minimum-height-trees/

from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        leaves = deque()
        edge_count = {}
        for src, nei in adj.items():
            if len(nei) == 1:
                leaves.append(src)
            edge_count[src] = len(nei)

        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1

                # We use edge count to simulate undirected edges. Although the edge count is deducted, 
                # the node is still connected due to adj hm.
                for nei in adj[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)