# https://leetcode.com/problems/unique-paths/

# Approach 1: Dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n
        for i in range(m - 1, -1, -1):
            cur = [0] * n
            cur[n - 1] = 1
            for j in range(n - 2, -1, -1):  
                cur[j] = cur[j + 1] + prev[j]
            prev = cur

        return prev[0]
    
# Approach 2: Memo
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        def helper(x, y):
            if x == m - 1 and y == n - 1:
                return 1
            if x >= m or y >= n:
                return 0
            if memo[x][y] != -1:
                return memo[x][y]

            memo[x][y] = helper(x + 1, y) + helper(x, y + 1)
            return memo[x][y]

        return helper(0, 0)
