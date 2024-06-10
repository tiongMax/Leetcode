class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(nums)
        # Maintain a min Heap of size k, so the min will be kth largest.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # Pop the min out if the size exceed k, the min could the val that was just pushed in.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # The min is stored in the first index
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)