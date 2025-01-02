# https://leetcode.com/problems/longest-cycle-in-a-graph/

from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        path = {}
        visited = set()
        def dfs(node, dist):
            if node in path:
                return dist - path[node]
            if node in visited:
                return -1
            if edges[node] == -1: 
                return -1

            visited.add(node)
            path[node] = dist
            return dfs(edges[node], dist + 1)

        ans = -1
        for i in range(len(edges)):
            if i not in visited:
                ans = max(ans, dfs(i, 0))
                path.clear()

        return ans
            
            