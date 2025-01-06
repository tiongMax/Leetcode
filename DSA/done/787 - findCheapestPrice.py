# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List
from collections import defaultdict, deque

# Approach 1: Modified Dijkstra (BFS with path relaxation)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))

        dist = [float('inf')] * n
        dist[src] = 0
        q = deque()
        q.append((src, 0))
        layer = 0
        while q:
            for _ in range(len(q)):
                cur_n, cur_w = q.popleft()
                for next_n, next_w in graph[cur_n]:
                    if next_w + cur_w < dist[next_n]:
                        dist[next_n] = next_w + cur_w
                        q.append((next_n, dist[next_n]))

            layer += 1
            if layer == k + 1:
                break

        return dist[dst] if dist[dst] < float('inf') else -1

# Approach 2: Bellman Ford
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights: 
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
            
        return -1 if prices[dst] == float("inf") else prices[dst]
    