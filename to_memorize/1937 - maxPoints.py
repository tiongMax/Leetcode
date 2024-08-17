# https://leetcode.com/problems/maximum-number-of-points-with-cost/

from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])
        
        # Initialize a dp array to store the maximum points up to the current row.
        dp = [0] * cols
        
        # Start by setting dp to the points in the first row
        dp = points[0][:]
        
        # Iterate over each row starting from the second one
        for i in range(1, rows):
            # Create a new dp array to store the maximum points for the current row
            new_dp = [0] * cols
            
            # Calculate left maxes
            left_max = [0] * cols
            left_max[0] = dp[0]
            for j in range(1, cols):
                left_max[j] = max(left_max[j - 1], dp[j] + j)
            
            # Calculate right maxes
            right_max = [0] * cols
            right_max[cols - 1] = dp[cols - 1] - (cols - 1)
            for j in range(cols - 2, -1, -1):
                right_max[j] = max(right_max[j + 1], dp[j] - j)
            
            # Calculate the maximum points for each column in the current row
            for j in range(cols):
                new_dp[j] = max(left_max[j] - j, right_max[j] + j) + points[i][j]
            
            # Update dp with the results from the current row
            dp = new_dp
        
        # The result is the maximum value in the last dp array
        return max(dp)
