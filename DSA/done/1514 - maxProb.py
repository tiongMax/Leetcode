# https://leetcode.com/problems/path-with-maximum-probability/

from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], 
        start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []

        for i in range(len(edges)):
            s = edges[i][0]
            d = edges[i][1]
            w = succProb[i]
            adj[s].append([d, w])
            adj[d].append([s, w])

        maxHeap = [[-1, start_node]]
        visited = set()
        while maxHeap:
            curProb, curNode = heapq.heappop(maxHeap)
            visited.add(curNode)
            if curNode == end_node:
                return -curProb

            for nextNode, nextProb in adj[curNode]:
                if nextNode not in visited:
                    heapq.heappush(maxHeap, [curProb * nextProb, nextNode])

        return 0