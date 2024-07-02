# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Just in case we have one 0 in between 1 negative number
        # at both left and right, we will get 0 as the largest num with using max
        # If we set up res with any num, we will get the largest num at the left
        # or right of 0, which is always lesser than 0. 
        # [-1, 0, -1]
        res = max(nums)
        # We maintain cur_max (asked by ques) and cur_min (it is usually negative
        # and if the next num is negative, we will get a large positive number to
        # be compared with the cur_max).
        cur_min, cur_max = 1, 1

        for n in nums:
            if n == 0:
                cur_min = cur_max = 1
                continue

            # Use Kadane's algo but we keep track of cur_min to counter against
            # next negative num
            temp = n * cur_max
            cur_max = max(temp, n * cur_min, n)
            cur_min = min(temp, n * cur_min, n)
            res = max(res, cur_max)

        return res