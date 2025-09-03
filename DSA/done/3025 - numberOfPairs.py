# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i

from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        
        # Check every pair of points
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                    
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Check if point i is upper-left of point j
                # A is upper-left of B if: A.x <= B.x AND A.y >= B.y
                if x1 <= x2 and y1 >= y2:
                    # Define rectangle boundaries
                    left = min(x1, x2)
                    right = max(x1, x2)
                    bottom = min(y1, y2)
                    top = max(y1, y2)
                    
                    # Check if rectangle is empty (no other points inside or on border)
                    is_empty = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        
                        x3, y3 = points[k]
                        
                        # Check if point k is inside or on the rectangle border
                        if left <= x3 <= right and bottom <= y3 <= top:
                            is_empty = False
                            break
                    
                    if is_empty:
                        count += 1
        
        return count