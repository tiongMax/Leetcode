# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N = len(moveTime)
        M = len(moveTime[0])
        DIRECTION = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        min_heap = [(0, 1, 0, 0)]
        visited = set()
        dist = [[float('inf')] * M for _ in range(N)]

        while min_heap:
            t, s, x, y = heapq.heappop(min_heap)
            if (x, y) == (N - 1, M - 1):
                return t
            if (x, y) in visited:
                continue

            visited.add((x, y))
            for dy, dx in DIRECTION:
                ny, nx = y + dy, x + dx
                if 0 <= nx < N and 0 <= ny < M:
                    d = max(moveTime[nx][ny], t) + s
                    if d < dist[nx][ny]:
                        dist[nx][ny] = d
                        heapq.heappush(min_heap, (d, 1 if s != 1 else 2 , nx, ny))