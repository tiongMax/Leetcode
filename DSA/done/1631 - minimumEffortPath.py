from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minHeap = [[0, 0, 0]]
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()

        while minHeap:
            e, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                return e
            
            for dr, dc in direction:
                nextR, nextC = r + dr, c + dc
                if nextR < 0 or nextC < 0 or nextR >= len(heights) or nextC >= len(heights[0]) \
                    or (nextR, nextC) in visited:
                    continue
                diff = max(e, abs(heights[nextR][nextC] - heights[r][c]))
                heapq.heappush(minHeap, [diff, nextR, nextC])
