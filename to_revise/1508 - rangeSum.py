# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

from typing import List
import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        min_heap = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(min_heap)

        ans = 0
        for k in range(1, right + 1): 
            x, i = heapq.heappop(min_heap)
            if k >= left: 
                ans += x
            if i + 1 < n: 
                # x + nums[i + 1] is the prefix sum till i + 1
                heapq.heappush(min_heap, (x + nums[i + 1], i + 1))

        return ans % (10 ** 9 + 7)