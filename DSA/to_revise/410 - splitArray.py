# https://leetcode.com/problems/split-array-largest-sum/description/

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum_allowed):
            subarray_count = 1
            current_sum = 0
            for n in nums:
                if current_sum + n > max_sum_allowed:
                    # Start a new subarray
                    subarray_count += 1
                    current_sum = n
                else:
                    current_sum += n
            return subarray_count <= k

        # Lower bound: the largest single element (must be able to fit it)
        # Upper bound: the sum of the whole array (one big subarray)
        l, r = max(nums), sum(nums)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            if can_split(mid):
                ans = mid
                r = mid - 1 # Try to find a smaller "maximum sum"
            else:
                l = mid + 1 # Sum is too small, need to allow a larger limit
        return ans