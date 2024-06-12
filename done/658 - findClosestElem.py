import heapq
from typing import List

# Approach 1: heap
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        for n in arr:
            heapq.heappush(minHeap, [abs(n - x), n])
        
        res = []
        for _ in range(k):
            diff, n = heapq.heappop(minHeap)
            res.append(n)

        res.sort()
        return res
    
# Approach 2: Binary search