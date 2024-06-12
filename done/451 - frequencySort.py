class Solution:
    def frequencySort(self, s: str) -> str:
        hm = Counter(s)
        maxHeap = []
        for key in hm.keys():
            heapq.heappush(maxHeap, [-hm[key], key * hm[key]])

        result = ""
        while maxHeap:
            count, s = heapq.heappop(maxHeap)
            result += s

        return result