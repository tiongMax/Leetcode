# https://leetcode.com/problems/implement-router/?envType=daily-question&envId=2025-09-20

from collections import deque, defaultdict, Counter
from typing import List, Tuple

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.q = deque()  # store packets in FIFO order
        self.seen = set()  # avoid duplicates
        self.dest_timestamps = defaultdict(list)  # destination -> sorted timestamps
        self.processed_idx = Counter()  # how many timestamps already removed per destination

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        # Duplicate check
        if packet in self.seen:
            return False

        # Memory full → remove oldest
        if len(self.q) == self.memoryLimit:
            self._remove_oldest()

        # Add new packet
        self.q.append(packet)
        self.seen.add(packet)
        self.dest_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        src, dst, ts = self.q.popleft()
        self.seen.remove((src, dst, ts))
        self.processed_idx[dst] += 1  # logically remove from that dest
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_timestamps:
            return 0
        lst = self.dest_timestamps[destination]
        start_i = self.processed_idx.get(destination, 0)

        L = self.lower_bound(lst, startTime, start_i)
        R = self.upper_bound(lst, endTime, start_i)
        return R - L

    def _remove_oldest(self):
        if not self.q:
            return
        src, dst, ts = self.q.popleft()
        self.seen.remove((src, dst, ts))
        self.processed_idx[dst] += 1

    # ----- Binary search helpers -----
    def lower_bound(self, arr, target, lo):
        """Return first index i >= lo such that arr[i] >= target"""
        hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upper_bound(self, arr, target, lo):
        """Return first index i >= lo such that arr[i] > target"""
        hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

