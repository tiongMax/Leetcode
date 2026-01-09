# https://leetcode.com/problems/find-a-peak-element-ii/

from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        start_row, end_row = 0, len(mat) - 1
        
        while start_row <= end_row:
            # Find the middle row
            mid_row = start_row + (end_row - start_row) // 2
            
            # Find the index of the maximum element in the middle row
            # This ensures it's already greater than its left and right neighbors
            max_col = 0
            for col in range(len(mat[mid_row])):
                if mat[mid_row][col] > mat[mid_row][max_col]:
                    max_col = col
            
            # Check neighbors in the rows above and below
            is_greater_than_top = mid_row == 0 or mat[mid_row][max_col] > mat[mid_row - 1][max_col]
            is_greater_than_bottom = mid_row == len(mat) - 1 or mat[mid_row][max_col] > mat[mid_row + 1][max_col]
            
            # If it's greater than both, we found a peak
            if is_greater_than_top and is_greater_than_bottom:
                return [mid_row, max_col]
            
            # If the element above is larger, move the search to the upper half
            elif not is_greater_than_top:
                end_row = mid_row - 1
            
            # Otherwise, move to the lower half
            else:
                start_row = mid_row + 1
                
        return []