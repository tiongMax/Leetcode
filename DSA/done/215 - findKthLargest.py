# https://leetcode.com/problems/kth-largest-element-in-an-array/description

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        res = None
        for _ in range(k):
            res = heapq.heappop(maxHeap)

        return -res