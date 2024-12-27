# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if target == arr[mid]:
                    return True
                elif target > arr[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                
            return False

        l, r = 0, len(matrix) - 1 
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][-1] >= target >= matrix[mid][0]:
                return bs(matrix[mid])
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1

# Treat matrix as a list
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        n = len(matrix)
        m = len(matrix[0])
        high = (m * n) - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid//m][mid%m] == target:
                return True
            elif matrix[mid//m][mid%m] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return False