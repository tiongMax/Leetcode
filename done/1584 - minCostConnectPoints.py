# https://leetcode.com/problems/min-cost-to-connect-all-points/description/

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [tuple(p) for p in points]
        adj = {p: [] for p in points}

        # Build the adjacency list with correct Manhattan distances
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if i == j:
                    continue
                p1, p2 = points[i], points[j]
                weight = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
                adj[p1].append((weight, p2))
                adj[p2].append((weight, p1))

        minHeap = [(0, points[0])]  # (weight, point)
        mst = 0
        visited = set()

        while len(visited) < len(points):
            weight, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            visited.add(point)
            mst += weight

            for nei_weight, nei in adj[point]:
                if nei not in visited:
                    heapq.heappush(minHeap, (nei_weight, nei))

        return mst



