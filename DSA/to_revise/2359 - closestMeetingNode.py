# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        visited1, visited2 = [False] * n, [False] * n
        dist1, dist2 = [float('inf')] * n, [float('inf')] * n
        dist1[node1] = 0
        dist2[node2] = 0

        def dfs(i, visited, dist):
            visited[i] = True
            if edges[i] != -1 and not visited[edges[i]]:
                dist[edges[i]] = 1 + dist[i]
                dfs(edges[i], visited, dist)
            return 

        dfs(node1, visited1, dist1)
        dfs(node2, visited2, dist2)

        res, curMin = -1, float('inf')
        for i in range(n):
            if curMin > max(dist1[i], dist2[i]):
                res = i
                curMin = max(dist1[i], dist2[i])
        return res