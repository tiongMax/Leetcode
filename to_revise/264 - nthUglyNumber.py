from collections import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0

        limit = [2, 3, 5]
        minHeap = []
        heapq.heappush(minHeap, 1)
        visited = set()
        visited.add(1)

        ugly_number = 1

        for _ in range(n):
            ugly_number = heapq.heappop(minHeap)
            for factor in limit:
                # Ugly number * 2 or 3 or 5 will still result in an ugly number.
                new_ugly = ugly_number * factor
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heapq.heappush(minHeap, new_ugly)

        return ugly_number
