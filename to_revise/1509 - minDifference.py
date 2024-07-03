# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

from typing import List
import heapq

# Approach 1: Use 2 heaps
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        # First and last 4 elements are sorted as we can only remove / replace 3 elements.
        smallest = heapq.nsmallest(4, nums)
        largest = heapq.nlargest(4, nums)
        
        return min(
            largest[0] - smallest[3],
            largest[1] - smallest[2],
            largest[2] - smallest[1],
            largest[3] - smallest[0]
        )

# Approach 2: Sort it 
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        nums.sort()
        f3_b0 = nums[-1] - nums[3]
        f2_b1 = nums[-2] - nums[2]
        f1_b2 = nums[-3] - nums[1]
        f0_b3 = nums[-4] - nums[0]
        return min(f3_b0, f2_b1, f1_b2, f0_b3)
    
"""
To get the min difference, we need to get the biggest small element and smallest large element, so that 
their distance in between is as short as possible.
We need to first sort or partially sort the array.

[0, 6, 6, 6, 10]
In this case, we need to get the "center" elements. 
"""