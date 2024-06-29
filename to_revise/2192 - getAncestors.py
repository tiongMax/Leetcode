# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

from typing import List
from collections import defaultdict, deque

# Approach 1: O(n ^ 2),  O(n ^ 2)
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)

        res = [[] for _ in range(n)]
        def dfs(node, i, visited):
            visited.add(node)
            for n in adj[node]:
                if n in visited:
                    continue
                res[n].append(i)
                dfs(n, i, visited)

        for i in range(n):
            dfs(i, i, set())

        return res
    
# Approach 2: 
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestors = [set() for _ in range(n)]
        incoming = [0]*(n)

        for start, end in edges:
            graph[start].append(end)
            ancestors[end].add(start)
            incoming[end]+=1
        
        q = deque()
        for node in range(n):
            if not incoming[node]:
                q.append(node)
                
        while q:
            node = q.popleft()
            for adjacent_node in graph[node]:
                ancestors[adjacent_node].update(ancestors[node])
                incoming[adjacent_node] -=1
                if not incoming[adjacent_node]:
                    q.append(adjacent_node)

        result = []
        for node in range(n):
            result.append(sorted(ancestors[node]))
        return result