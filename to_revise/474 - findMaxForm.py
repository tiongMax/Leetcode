# https://leetcode.com/problems/ones-and-zeroes/

from typing import List

# Approach 1: Dp
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize the dp table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            
            # Create a temporary dp table to hold updates
            next_dp = [row[:] for row in dp]
            
            # Update the dp table from top-left to bottom-right
            for i in range(m + 1):
                for j in range(n + 1):
                    if i >= zeros and j >= ones:
                        next_dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
            
            # Update the main dp table with the temporary dp table
            dp = next_dp
        
        return dp[m][n]

# Approach 2: Memo
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Count zeros and ones for each string
        counts = [(s.count('0'), s.count('1')) for s in strs]
        
        # Use a dictionary for memoization
        memo = {}
        
        def dp(i: int, zeros: int, ones: int) -> int:
            # Base case: If no items left or no capacity left
            if i == len(strs):
                return 0
            
            # Check if the result is already in the memo
            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]
            
            # Option 1: Skip the current string
            skip = dp(i + 1, zeros, ones)
            
            # Option 2: Include the current string (if possible)
            include = 0
            if zeros >= counts[i][0] and ones >= counts[i][1]:
                include = 1 + dp(i + 1, zeros - counts[i][0], ones - counts[i][1])
            
            # Take the maximum of both options
            memo[(i, zeros, ones)] = max(skip, include)
            return memo[(i, zeros, ones)]
        
        # Start the recursion from the first string with full capacity
        return dp(0, m, n)
