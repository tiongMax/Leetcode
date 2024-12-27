# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

from typing import List
from collections import defaultdict

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        cnt = defaultdict(int)
        for i in range(len(target)):
            cnt[target[i]] += 1
            cnt[arr[i]] -= 1

        for n in cnt:
            if cnt[n] != 0:
                return False

        return True
