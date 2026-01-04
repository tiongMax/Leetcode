# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        # Ensure the first array is the smaller one
        if len(a) > len(b):
            a, b = b, a

        n1, n2 = len(a), len(b)
        low, high = 0, n1 # Not index of a, but how many elems to taken from a to form left partition

        # Perform binary search on the smaller array
        while low <= high:
            # Calculate cut points in both arrays
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1

            # Handle edge elements using -inf and inf
            l1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else b[cut2 - 1]
            r1 = float('inf') if cut1 == n1 else a[cut1]
            r2 = float('inf') if cut2 == n2 else b[cut2]

            # Check if partition is correct
            if l1 <= r2 and l2 <= r1:
                # Even total length: take average of max left and min right
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    # Odd length: take max of left side (mid elem is included in left partition)
                    return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else: # l2 > r1
                low = cut1 + 1

        return 0.0  
