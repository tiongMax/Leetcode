# https://leetcode.com/problems/network-delay-time/

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, w in times:
            graph[s].append((d, w))

        min_heap = [(0, k)]
        visited = set()
        t = 0
        while min_heap:
            cur_w, cur_n = heapq.heappop(min_heap)
            if cur_n in visited:
                continue

            t = cur_w
            visited.add(cur_n)
            for nei, weight in graph[cur_n]:
                if nei not in visited:
                    heapq.heappush(min_heap, (weight + cur_w, nei))

        return t if len(visited) == n else -1