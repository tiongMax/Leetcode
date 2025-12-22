# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)

        arr = []
        for num, v in cnt.items():
            arr.append([v, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
