from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Edge case: thieves at the start or end
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0
            
        # ---------------------------------------------------------
        # PHASE 1: Multi-source BFS to calculate safeness
        # ---------------------------------------------------------
        dist = [[-1] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    dist[r][c] = 0
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        # ---------------------------------------------------------
        # PHASE 2: Binary Search + Validation BFS
        # ---------------------------------------------------------
        def can_reach(target_safeness: int) -> bool:
            # If the start itself doesn't meet the target, path is impossible
            if dist[0][0] < target_safeness:
                return False
                
            q = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            
            while q:
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                    
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Only step on cells that meet the target safeness
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                        if dist[nr][nc] >= target_safeness:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                            
            return False

        # Binary search range
        low = 0
        high = min(dist[0][0], dist[n-1][n-1])
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_reach(mid):
                ans = mid       # This safeness is possible, record it
                low = mid + 1   # Try to find a higher one
            else:
                high = mid - 1  # Too greedy, lower the requirement
                
        return ans