# https://leetcode.com/problems/find-eventual-safe-states/

from typing import List 

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            # backtrack and try each node
            visited[node] = False
            for n in graph[node]:
                if not dfs(n):
                    return False
            visited[node] = True
            return True

        res = []
        for n in range(len(graph)):
            if dfs(n):
                res.append(n)

        return res