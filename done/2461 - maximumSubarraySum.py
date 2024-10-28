# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        sum = 0
        res = 0
        window = set()

        for r in range(len(nums)):
            while nums[r] in window:
                window.remove(nums[l])
                sum -= nums[l]
                l += 1

            window.add(nums[r])
            sum += nums[r]

            if r - l + 1 == k:
                res = max(res, sum)
                window.remove(nums[l])
                sum -= nums[l]
                l += 1

        return res
