# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List
import math
from collections import defaultdict, deque

# Approach 1: Modified Dijkstra (BFS with path relaxation)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [math.inf] * n
        cost[src] = 0

        graph = defaultdict(list)

        for a,b, price in flights:
            graph[a].append((b, price))

        queue = deque()
        queue.append((src, 0))

        # We will break after k stops
        stops = 0
        while queue:
            ln = len(queue)
            for _ in range(ln):
                dest, pr = queue.popleft()                
                
                for nxt, nxt_pr in graph[dest]:
                    if nxt_pr + pr < cost[nxt]:
                        cost[nxt] = nxt_pr + pr
                        queue.append((nxt, cost[nxt]))
            
            stops += 1
            if stops == k + 1:
                break
        
        return cost[dst] if cost[dst] < math.inf else -1

# Approach 2: Bellman Ford
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            # Use a copy to make sure only nodes that are i hops away from the source will be updated
            # correctly to simulate the algo.
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        # There is always a way to reach the destination if it is within k + 1 hops away from
        # the source, however, it might not be shortest as the shortest path might take more hops.
        return -1 if prices[dst] == float("inf") else prices[dst]