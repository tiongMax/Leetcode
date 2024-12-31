# https://leetcode.com/problems/find-eventual-safe-states/

from typing import List 

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        cycle, visited = set(), set()
        def dfs(i):
            if i in visited:
                return True
            if i in cycle:
                return False

            cycle.add(i)
            for n in graph[i]:
                if not dfs(n):
                    return False
            cycle.remove(i)

            visited.add(i)
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res