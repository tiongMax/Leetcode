from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0], 0, 0]]
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == len(grid) - 1 and c == len(grid) - 1:
                return t

            for dr, dc in direction:
                nextR, nextC = r + dr, c + dc
                if nextR < 0 or nextC < 0 or nextR >= len(grid) or nextC >= len(grid) \
                    or (nextR, nextC) in visited:
                    continue
                heapq.heappush(minHeap, [max(grid[nextR][nextC], t), nextR, nextC])

        return -1
