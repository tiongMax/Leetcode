# https://leetcode.com/problems/path-with-maximum-probability/

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        max_heap = [(-1, start_node)]
        visited = set()
        while max_heap:
            cur_prob, cur_node = heapq.heappop(max_heap)
            if cur_node == end_node:
                return -cur_prob

            visited.add(cur_node)
            for nei, w in graph[cur_node]:
                if nei not in visited:
                    heapq.heappush(max_heap, (cur_prob * w, nei))

        return 0.0