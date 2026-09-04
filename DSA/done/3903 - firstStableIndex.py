# https://leetcode.com/problems/smallest-stable-index-i/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        pre_max = [0] * n
        post_min = [0] * n

        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        post_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            post_min[i] = min(post_min[i + 1], nums[i])

        for i in range(n):
            if pre_max[i] - post_min[i] <= k:
                return i

        return -1