# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

# Standard bs
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(findFirst: bool):
            l, r = 0, len(nums) - 1
            res = -1
            
            while l <= r:
                mid = l + (r - l) // 2
                
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    # We found the target! 
                    res = mid
                    # Standard BS would return here. 
                    # Instead, we keep searching to find the 'outer' edge.
                    if findFirst:
                        r = mid - 1 # Look left for earlier occurrence
                    else:
                        l = mid + 1 # Look right for later occurrence
            return res

        return [binarySearch(True), binarySearch(False)]
    
# lower and upper bound
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] >= target:
                    if nums[m] == target: res = m
                    r = m - 1 # Keep looking left
                else:
                    l = m + 1
            return res

        def find_last():
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] <= target:
                    if nums[m] == target: res = m
                    l = m + 1 # Keep looking right
                else:
                    r = m - 1
            return res

        return [find_first(), find_last()]