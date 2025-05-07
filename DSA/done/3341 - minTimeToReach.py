# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        visited = set()
        dist = [[float('inf')] * len(moveTime[0]) for _ in range(len(moveTime))]
        minHeap = [(0, 0, 0)]
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while minHeap:
            t, x, y = heapq.heappop(minHeap)
            if (x, y) == (len(moveTime) - 1, len(moveTime[0]) - 1):
                return t
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(moveTime) and 0 <= ny < len(moveTime[0]):
                    d = max(moveTime[nx][ny], t) + 1
                    if d < dist[nx][ny]:
                        dist[nx][ny] = d
                        heapq.heappush(minHeap, (d, nx, ny))

          