# https://leetcode.com/problems/smallest-stable-index-ii/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pre_max, post_min = [0] * n, [0] * n

        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(nums[i], pre_max[i - 1])

        post_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            post_min[i] = min(nums[i], post_min[i + 1])

        for i in range(n):
            if pre_max[i] - post_min[i] <= k:
                return i

        return -1