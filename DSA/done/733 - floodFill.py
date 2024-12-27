# https://leetcode.com/problems/flood-fill/

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        filled = [r.copy() for r in image]
        prev = image[sr][sc]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) \
                or image[r][c] != prev:
                return
            if filled[r][c] == color:
                return

            filled[r][c] = color
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        dfs(sr, sc) 
        return filled