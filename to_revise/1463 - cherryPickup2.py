# https://leetcode.com/problems/cherry-pickup-ii/

from typing import List

# Approach 1: Dp
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        prev = [[0] * m for _ in range(m)]

        # Initialize the last row
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    prev[j1][j2] = grid[n - 1][j1]
                else:
                    prev[j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

        # Process from the second-last row to the top
        for i in range(n - 2, -1, -1):
            cur = [[0] * m for _ in range(m)]
            for j1 in range(m):
                for j2 in range(m):
                    res = float('-inf')
                    for d1 in range(-1, 2):
                        for d2 in range(-1, 2):
                            ans = 0
                            if j1 == j2:
                                ans = grid[i][j1]
                            else:
                                ans = grid[i][j1] + grid[i][j2]

                            if 0 <= j1 + d1 < m and 0 <= j2 + d2 < m:
                                ans += prev[j1 + d1][j2 + d2]
                            else:
                                ans += int(-1e9)  # A large negative value if out of bounds
                            res = max(res, ans)
                    cur[j1][j2] = res
            prev = cur
        
        return prev[0][m - 1]

# Approach 2: Memo
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = {}
        n = len(grid)
        m = len(grid[0])

        def memo(i, j1, j2):
            if j1 < 0 or j2 < 0 or j1 >= m or j2 >= m:
                return float('-inf')
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            if (i, j1, j2) in dp:
                return dp[(i, j1, j2)]
                
            res = float('-inf')
            for d1 in range(-1, 2):
                for d2 in range(-1, 2):
                    temp = 0
                    if j1 == j2:
                        temp = grid[i][j1] + memo(i + 1, j1 + d1, j2 + d2)
                    else:
                        temp = grid[i][j1] + grid[i][j2] + memo(i + 1, j1 + d1, j2 + d2)
                    res = max(res, temp)
            dp[(i, j1, j2)] = res
            return res

        return memo(0, 0, m - 1)