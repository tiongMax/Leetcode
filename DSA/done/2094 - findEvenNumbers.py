# https://leetcode.com/problems/finding-3-digit-even-numbers/

from collections import Counter
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        for i in range(100, 999):
            cnt = Counter(digits)
            can_form = True
            for j in str(i):
                j = int(j)
                if j not in cnt:
                    can_form = False
                    break
                else:
                    cnt[j] -= 1
                    if not cnt[j]:
                        del cnt[j]
            if can_form and i % 2 == 0:
                res.append(i)
        return res

            