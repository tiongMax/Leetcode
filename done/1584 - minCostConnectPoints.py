# https://leetcode.com/problems/min-cost-to-connect-all-points/description/

import heapq
from typing import List

# Approach 1: Prims's
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

# Approach 2: Kruskal's

class UnionFind:
    def __init__(self, edges):
        self.par = {}
        self.rank = {}
        for e in edges:
            self.par[e] = e
            self.rank[e] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: 
                    continue
                p1, p2 = tuple(points[i]), tuple(points[j])
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                heapq.heappush(minHeap, [dist, p1, p2])

        uf = UnionFind([tuple(p) for p in points])
        mst = 0
        res = 0
        while mst < len(points) - 1:
            w, s, d = heapq.heappop(minHeap)
            if not uf.union(s, d):
                continue
            res += w
            mst += 1

        return res