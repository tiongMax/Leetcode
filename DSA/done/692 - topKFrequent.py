# https://leetcode.com/problems/top-k-frequent-words/

from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hm = Counter(words)
        max_heap = [(-count, word) for word, count in hm.items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]