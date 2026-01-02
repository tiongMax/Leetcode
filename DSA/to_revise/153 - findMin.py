# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        res = nums[0]

        while start <= end:
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break

            mid = start + ((end - start) // 2)
            res = min(res, nums[mid])

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
 
        return res