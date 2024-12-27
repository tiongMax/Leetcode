# https://leetcode.com/problems/kth-distinct-string-in-an-array/

from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        for s in arr:
            if cnt[s] == 1:
                if k == 1: 
                    return s
                else:
                    k -= 1
        return ""