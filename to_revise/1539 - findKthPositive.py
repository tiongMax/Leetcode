# https://leetcode.com/problems/kth-missing-positive-number/

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = low + ((high - low) // 2)
            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid - 1

        # low is the number of elements in arr that are less than the k-th missing number
        return low + k
