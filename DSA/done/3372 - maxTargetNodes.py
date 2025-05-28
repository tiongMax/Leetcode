# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

from collections import defaultdict
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_adj(edges):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def dfs(node, depth, adj, visited):
            if depth < 0:
                return 0
            visited.add(node)
            count = 1
            for neighbor in adj[node]:
                if neighbor not in visited:
                    count += dfs(neighbor, depth - 1, adj, visited)
            return count

        adj1 = build_adj(edges1)
        adj2 = build_adj(edges2)

        max2 = 0
        for i in range(len(edges2) + 1):
            max2 = max(max2, dfs(i, k - 1, adj2, set()))

        res = []
        for i in range(len(edges1) + 1):
            res.append(dfs(i, k, adj1, set()) + max2)
        return res
