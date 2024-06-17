from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        for i in range(1, n + 1):
            adjList[i] = []

        for s, d, w in times:
            adjList[s].append([d, w])
            
        shortest = {}
        minHeap = [[0, k]]
        t = 0
        while minHeap:
            curWeight, curNode = heapq.heappop(minHeap)
            if curNode in shortest:
                continue
            shortest[curNode] = curWeight
            # The last weight popped out will have the greater weight as the dest is the furthest from 
            # from the source among all other dests.
            t = curWeight

            for nextNode, nextWeight in adjList[curNode]:
                if nextNode not in shortest:
                    heapq.heappush(minHeap,  [curWeight + nextWeight, nextNode])

        return t if len(shortest) == n else -1