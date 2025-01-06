# https://leetcode.com/problems/swim-in-rising-water/

from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0], 0, 0]]
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == len(grid) - 1 and c == len(grid) - 1:
                return t
            if (r, c) in visited:
                continue

            visited.add((r, c))
            for dr, dc in direction:
                nextR, nextC = r + dr, c + dc
                if 0 <= nextR < len(grid) and 0 <= nextC < len(grid) and \
                     (nextR, nextC) not in visited:
                    heapq.heappush(minHeap, [max(grid[nextR][nextC], t), nextR, nextC])
       
        return -1