# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            fish_count = grid[r][c]
            grid[r][c] = 0
            fish_count += dfs(r + 1, c)  
            fish_count += dfs(r - 1, c)  
            fish_count += dfs(r, c + 1) 
            fish_count += dfs(r, c - 1)  
            
            return fish_count
        
        max_fish = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0: 
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish
